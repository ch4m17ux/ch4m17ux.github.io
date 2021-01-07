
# Unbaked Pie TryHackMe WriteUp

![enter image description here](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-1.png)

Se nos presenta una maquina, donde encontraremos un `sitio web vulnerable` a la deserialización insegura de [`pickle`](https://davidhamann.de/2020/04/05/exploiting-python-pickle/), el proposito es explotar la vulnerabilidad y acceder a un contenedor docker como usuario root.  El nivel que se le ha dado a esta maquina es **Medio**, ya que debemos tener algunos conceptos para lograr acceder y encontrar la **`flag`**.

Como siempre en estos casos, lo primero que debemos hacer es realizar un escaneo de puertos, para identificar donde encontramos los servicios.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-nmap.png)

Vemos que hay un servicio web en el puerto `5300`, por esta razon vamos a la direrccion `IP:PORT` y vemos que esta alojado alli.

![TryHackMe - Unbacked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-2.png)

Hacemos una verificacion de cada enlace y formulario, vemos que "aparentemente" todo esta correcto, no hay forma de encontrar una vulnerabilidad, pero nos fijamos que los post hacen referencia a `Pickle`, una vulnerabilidad que tienen algunos sitios web realizados en python en una deseralizacion insegura de pickle, que permite la ejecucion remota de codigo.  Nos aprovecharemos de esto.

Vamos a utilizar `BurpSuite` para interceptar las peticiones y respuesta del servidor, y analizaremos si hay algo que podamos aprovechar en la vulnerabilidad que posiblemente tiene. 

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-3.png)

Observamos que cuando se realiza una busqueda, el servidor nos responde con una nueva cookie calle **search_cookie** que al parecer es un objeto python serializado.

Serializacion es usado para convertir un objeto python en un flujo de datos que se envia al backend del servidor donde se deserializa para obtener el objeto.  Pero si la entrada del usuario se deserializa sin sanitizar, podria causar muchos problemas.  Vamos a enviar un codigo para comprobar si el servidor sanitiza la entrada o la ejecuta tal como se la enviamos.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-4.png)

En el ejemplo anterior, lo que hemos hecho es cargar el modulo de `pickle`, asignamos un valor (el que obtenemos de la cookie anterior) a una variable `val`y lo decodificamos con el modulo `b64decode` de `base64`; posteriormente lo cargamos con el modulo pickle para ver como lo procesa pickle.  Esta prueba de concepto nos ayudara a entender cómo funciona y crearemos un script para que codifique el payload que queremos enviar al servidor (que tal una **`shell reversa`**?).  Si deseas mas informacion acerca de pickle, puedes ver esta informacion en este [blog](https://davidhamann.de/2020/04/05/exploiting-python-pickle/).

Vemos que las entradas se ejecutan tal como las enviamos, no hay una sanitizacion correcta, es por esto que vamos a aprovecharnos para tratar de acceder y obtener una shell reversa. Asi que, vamos a crear un pequeño script, que nos codificara la cookie que deberiamos introducir para poder lograr el objetivo.

![Script Pickle - Shell Reversa](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-5.png)

Ejecutamos el script que hemos creado y obtenemos la cookie que debemos reemplazar.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-6.png)

 Vamos a utilizar BurpSuite para enviar esta cookie modificada y que nos devuelva la shell, por esto en nuestra maquina abrimos un netcat para que escuche las peticiones y podamos obtener la shell remota.
 
![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-7.png)
Esto nos abre en nuestra maquina la shell.

![TryHackMe - Unbacked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-8.png)

Somos `root`, pero unicamente dentro del contenedor, debemos intentar acceder al servidor, pero primero vamos a obtener una shell mas completa, que nos permita utilizar las flechas del teclado, usar combinación de teclas como `CTRL + c` para matar los procesos o tener autocompletado.

Lo que debemos es en la shell que hemos obtenido lanzar el siguiente comando:

```shell
root@8b39a559b296:$ python3 -c "import pty;pty.spawn('/bin/bash')"
```
Oprimimos CTRL + z para poner la shell en "background" y nos lleva a nuestra consola o shell, desde donde lanzamos el siguiente comando.
```shell
local@local:~/TryHackMe/unbaked_pie$ stty raw -echo
```

Posteriormente escribimos `fg`, damos enter y volvemos a la shell remota que teniamos antes, desde alli digitamos por ultimo:

```shell
root@8b39a559b296:/home/site#  export TERM=xterm
```
Obtenemos finalmente una shell apropiada.

Vamos entonces a realizar un escalado de privilegios y obtener un usuario que nos permita salir del docker y saltar hacia el servidor que lo aloja.  Comenzamos por revisar el historial del bash:

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-9.png)

Podemos encontrar que alguien ha intentado acceder a traves de `SSH` utilizando el usuario `**ramsey**`, pero tambien podemos ver que han quitado el servicio `cliente de SSH`, asi que no hay forma desde el mismo docker de acceder, por lo que se debe pensar en otras opciones para lograrlo.  Revisamos que puertos tiene abiertos, lo haremos con `netcat`, debido a que al estar dockerizado, las comunicaciones hacia el mismo estan limitadas y no podriamos hacerlo desde nuestra maquina.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-10.png)

Muy bien, tenemos que el puerto `22` tiene un `SSH` corriendo, sabemos que alguien utilizo el usuario `ramsey`, nos hace falta obtener la contraseña de este usuario.

Hemos visto que el servido web esta basado en django, asi que enumeraremos para ver si encontramos la base de datos y alli este el usuario ramsey que hemos encontrado.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-11.png)

Dentro de la carpeta site, podemos ver que esta la base de datos, la cual esta basada en `sqlite3`.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-12.png)

Me lo descargo a mi equipo para poder analizarlo, asi que utilizare `Netcat` para esta tarea.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-13.png)
## Analizamos la base de datos de sqlite

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-14.png)

### Tabla auth_user


![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-15.png)

Tenemos el hash de 5 usuarios diferente, uno de ellos es el de ramsey; esta es una buena noticia.  Revisando algunos sitios en internet y ejemplos de hashcat, encontramos que el modo de cifrado de django es 10000

Procedemos a crackearlos a traves de la herramienta `hashcat`, tardara unos minutos, depende de los recursos de nuestra maquina local y el diccionario que utilicemos, he usado el mas comun - `rockyou.txt`.


![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-16.png)

Obtenemos la contraseña que estabamos buscando:``

   > testing:lala12345


Suponemos que las credenciales se estan reutilizando, y que la misma contraseña de ramsey en django, es la misma que utiliza para acceder via SSH; pero viene lo mas interesante, y debido a que el puerto no es accesible desde fuera para poder establecer una conexion desde mi maquina local, intentaremos realizar un tunel de puerto utilizando [chisel](https://github.com/jpillora/chisel).

Teniendo chisel en nuestra maquina y haberlo transferido a la maquina remota, podemos realizar el tunel de puerto:

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-17.png)

Y tenemos establecida la conexion, a traves de una `redireccion de puertos`, utilizando nuestra maquina local, pero apuntando al puerto 22 de la maquina remota.

Procedemos a loguearnos con el usuario `ramsey` y la contraseña que hemos encontrado como `hashcat`.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-18.png)

Pero la contraseña no es la correcta, asi que aprovechamos el tunel de puerto que hemos realizado para tratar de hacer un ataque de fuerza bruta a SSH utilizando `Hydra`, y esperamos que la contraseña sea alguna conocida.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-19.png)

Y la contraseña la obtenemos en muy poco tiempo.

Procedemos a acceder finalmente a la maquina remota a traves de `SSH`.


![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-20.png)

## Leemos la flag del usuario ( User flag)

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-21.png)

Realizamos una enumeración del usuario a través de `sudo -l` y vemos que permisos tiene nuestro usuarios sobre el sistema:

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-22.png)

Este usuario puede correr un script de python denominado `vuln.py` el cual correo de forma impersonal como otro usuario llamado `oliver`, que parece tener mejores permisos sobre la maquina remota; verificamos si tenemos permisos de escritura sobre este fichero:

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-23.png)

Lo que haremos sera renombrar este fichero y crear uno nuevo llamado exactamente igual, donde escribiremos un script para copiar la clave publica `.ssh` que nos permita acceder como `oliver`.

Primero generamos el par de claves ssh como usuario oliver, seran los que utilizaremos en nuestro script.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-24.png)

Una vez que tenemos generado el par de claves, procedemos a crear (modificar) el fichero `vuln.py`, de acuerdo a nuestro proposito.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-25.png)

Procedemos a ejecutar el script que hemos creado como oliver y verificamos que nos ha copiado el fichero `.pub e`n el directorio .ssh del usuario `oliver`.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-26.png)

Comprobamos que ha creado el fichero que deseabamos.  Ahora, utilizaremos esta `clave publica` (que hemos copiado) y la `clave privada` que generamos para acceder a traves de SSH como usuario oliver.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-27.png)

Y como habeis visto, ya estamos como `oliver`, el cual hace parte del grupo `sysadmin` (esto esta bien para nuestros propositos)

Procedemos a hacer una enumeración del usuario y vemos que permisos impersonales tenemos.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-28.png)

Este usuario puede ejecutar un script python en `/opt/dockerScript.py` como `root` y tambien establecer variables de entorno.  Vamos a verificar que hace el script mencionado.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-29.png)

Vemos que el docker es importado pero usando un `path relativo`, durante la ejecucion `Python` busca los modulos importados en la ruta mencionada en la variable de entorno `PYTHONPATH`; como podemos establecer la variable de entorno durante la ejecución, podriamos crear nuestro propio módulo `docker.py` y establecer esa ruta como `PYTHONPATH` y durante la ejecución este archivo se ejecutará.

Procedemos a ubicarnos en el home del usuario `oliver`, y alli creamos un fichero `Python` para nuestro proposito denomina `docker.py`.  Lo que deseamos es establecer un `SUID bit` en el binario `/bin/bash`.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-30.png)

Ejecutamos el script `dockerScript.py`, pasandole el parametro en la variable de entorno `PYTHONPATH` en el home del usuario `oliver`, para que tome el `docker.py` que hemos creado, lo importe y ejecute nuestro proposito.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-31.png)

Aunque obtenemos un mensaje de error, podemos comprobar que en el binario `/bin/bash` tenga establecido el `SUID bit` que era nuestro proposito.

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-32.png)

Ejecutamos el binario `/bin/bash` y somo `root` (finalmente)

![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-33.png)


## Leemos la flag de root


![TryHackMe - Unbaked Pie](https://ch4m17ux.github.io/img/posts/unbaked-pie/unbaked-pie-THM-34.png)

Hemos obtenido las dos flags que nos pedia el reto.


## FIN

> ##### Doy gracias a [Shishir Subedi](https://shishirsubedi.com.np/) por su ayuda en este reto, su write-up y la conversacion que sostuvimos para aclarar algunos pasos y conceptos.
