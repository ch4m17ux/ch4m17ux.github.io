# OverPass3 - Hosting (Writeup - TryHackMe) 

![Reto Overpass3 - TryHackMe](https://ch4m17ux.github.io/img/posts/overpass3/tryhackme-overpass3.jpg)

Tenemos una maquina denominada [OverPass3 - Hosting](https://tryhackme.com/room/overpass3hosting), un reto de nivel medio.

> *En esta maquina se nos indica que debemos lanzar la maquina y esperar a que inicie, tardara cerca de 5 minutos, de otro modo no podremos acceder a la misma.  Se ha establecido que la maquina tenga un nivel intermedio de expertiz, y esta bien denominada, ya que hay que trabajar un poco para poder escalar privilegios, las vulnerabilidades para poder hacerlo solo podran ser explotadas casi al final del desarrollo de la misma*.

## Recoleccion de información

Como generalmente creo que se deberia comenzar, es realizando un un escaneo de puertos; asi podremos saber que puertos abiertos tiene la maquina y poder tener un panorama general de los pasos a realizar.

### NMAP

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-1.png)

Podemos ver que tenemos 3 puertos abiertos:
> - 21
 >- 22
 >- 80
 
Asi que vamos a seguir recolectando información. Ya que tenemos un sitio web, verificamos si podemos ver algo dentro del sitio, dentro del codigo fuente y demas.  Lo mas interesante de reseñar es que tenemos algunos nombres que nos podrian ayudar a tratar de probar accesos a traves de SSH o algun administrador del sitio que pueda tener, asi que tomamos nota:

>* Paradox
>* Elf
>* MuirlandOracle
>* NinjaJc01

Vamos a ejecutar un escaneo de directorios sobre el sitio web, verificamos si encuentra alguna zona de administracion o similar.

### Gobuster

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-2.png)

Observamos que nos ha encontrado un directorio interesante (`/backups`), ya que no es comun que se tenga en un sitio web.  Al verificar este directorio encontramos que tiene un fichero `ZIP`, que nos lo descargaremos y verificaremos que contiene.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-3.png)

### Unzip&Decrypt

Una vez que lo hemos descargado encontramos que hay dos ficheros: 

> * Un fichero excel encriptado con `GPG`
> * Una llave que suponemos que seria la que nos permita descencriptar el fichero.


![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-4.png)

Lo que debemos hacer primero es importar esta llave que hemos obtenido (y que seguro nos vendra muy bien)

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-5.png)

Posteriormente desencriptamos el fichero excel encriptado.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-6.png)

Obtenemos un fichero excel que podemos visualizar, bien sea con algun editor que tengas en tu maquina (*como `LibreOffice`*) o utilizar un visor online.  De un modo u otro, podremos ver que hay una tabla con algunos datos interesantes: Nombre de Cliente, **Nombre de Usuario**, **Contraseña**, Numero de tarjeta de credito y CVC (*No os emocioneis, los numeros de tarjeta no son validos*).  Verificaremos si con estos datos podemos acceder via `SSH`.

| Customer Name | Username |Password |Credit card number | CVC|
|--|--|--|--|--|
| Par. A. Doxx | paradox | ShibesAreGreat123 | 4111 1111 4555 1142 | 432 |
| 0day Montgomery | 0day | OllieIsTheBestDog | 5555 3412 4444 1115 | 642 |
| Muir Land | muirlandoracle |A11D0gsAreAw3s0me | 5103 2219 1119 9245 | 737 |

### Login Attempts

Ya que tenemos algunos usuarios y contraños, probaremos el acceso a traves de `SSH` ; en este caso he comenzado con el primer usuario, que para mi tiene mas sentido de que exista un usuario con ese nombre.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-7.png)

No obtenemos acceso, y segun el mensaje todo indica que el acceso a traves de `SSH` con **usuario** y **contraseña** no esta habilitado y se requiere un par de claves.

Hemos intentado con los otros usuarios, y tampoco obtenemos acceso.

Vimos que el *puerto 21 (ftp)* tambien estaba abierto, voy a intentar el acceso a traves de este puerto `FTP`, pero nos encontramos con que no hay acceso con usuario **anonimo**, de nuevo, intentaremos el acceso acceso con los datos que hemos obtenido del fichero excel, veremos si hay suerte.

>*En muchas ocasiones encontramos que se reutilizan usuarios y contraseñas para varios servicios.*

Podemos encontrar que obtenemos acceso con el usuario paradox, y la ubicacion donde nos situa es donde podemos encontrar los archivos que componen el sitio web. He tratado de moverme hacia una ubicacion diferente y al parecer este usuario en `FTP` esta enjaulado.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-8.png)
### Acceso a la maquina remota

Sin embargo, el hecho de que no podamos movernos no quiere decir que no podamos hacer nada, mas aun que estamos ubicados en la carpeta donde estan los ficheros del sitio web, podemos comenzar nuestras acciones de acceso y *escalado de privilegios*.

Podemos en esta ocasion, de forma realmente sencilla, subir ficheros y ejecutarlos desde el sitio web, asi que intentare subir un archivo `PHP` que contiene una ***shell reversa*** y acceder al servidor.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-9.png)

Como vemos, al listar los ficheros del servidor podemos ver el fichero *PHP* que hemos subido con la ***shell reversa***.

> Recuerda que en el fichero PHP donde tenemos la shell reversa debemos modificarlo con la IP de nuestra maquina local y el puerto local donde escuchara, de esta forma se podra establecer la comunicacion.

En nuestra maquina local, ejecutamos `netcat` para que escuche en el puerto que hemos configurado en el fichero `PHP` y ejecutamos desde la web el fichero para activar la ***shell reversa***.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-10.png)

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-11.png)

Tenemos de esta forma establecida la comunicacion a traves de `netcat` y tenemos una ***shell*** en el servidor remoto; pero es una shell un poco limitada, asi que ejecutaremos algunos comandos para poder tener mayores funcionalidades.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-12.png)

Estos comando nos permiten tener autocompletado, buscar a traves del uso de las flechas del teclado y algunas opciones mas dentro de la *shell*.

Verificamos con qué usuario nos "loguea" en esta shell (*lo mas comun es **www** o **apache***)

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-13.png)
### Flag de Web

La primera flag que nos piden que debemos buscar esta relacionada con este mismo usuario, asi que buscaremos donde puede estar la flag.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-14.png)

A traves de ensayo/error hemos encontrado un fichero denominado web.flag, que suponemos que es nuestra primera flag.  

>En estos casos, es ir probando opciones:
>* Buscar por el nombre apache
>* Buscar por la palabra flag como nombre
>* Buscar por la palabra flag como extension
>* Etc

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-15.png)
### Flag de Usuario

La siguiente pista que nos dan, es que la ***flag de usuario*** se encuentra bajo el usuario `"james"`, cuando revisamos qué usuarios tienen un `home` creado encontramos dos: ***Paradox y James***.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-16.png)

Pero al intentar acceder a la carpeta de usuarios nos pone que no tenemos permisos.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-17.png)

Vamos a reutilizar accesos, no tenemos de forma sencilla o clara un posible acceso como `James`; podríamos realizar una análisis de fuerza bruta a traves de `Hydra` pero hemos visto con el usuario `Paradox` que el acceso a traves de `SSH` se realiza con alguna clave privada, asi que esta no es una buena opcion.  Dicho lo anterior reutilizaremos el acceso de `Paradox` que teniamos para el acceso a `FTP`, veremos si podemos cambiar de usuario, desde `Apache` hacia `Paradox`.

 ![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-18.png)
 
Vemos que podemos acceder con este usuario, verificamos si podemos tener acceso como `sudo` o `superuser`.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-19.png)

Este usuario es un usuario normal, es decir no tiene permisos especiales, no esta dentro del grupo *`sudoers`*, que permita ejecutar acciones como usuario `root`, y que quiza podamos vulnerar. 

Verificamos si podemos acceder a la carpeta home de **`James`**, que es el usuario que nos interesa y donde esta la flag.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-20.png)
### Escalado de privilegios

No me gusta utilizar herramientas automatizadas, que en muchas ocasiones nos puede ayudar pero que nos da mucha informacion, sin embargo, para esta maquina utilizare **`Linpeas`**, que nos hara una busqueda total de vulnerabilidades, y veremos si encuentra algo interesante.

Lo primero, debemos descargar el bash de `Linpeas` desde su repositorio oficial, en nuestra maquina local.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-21.png)

De nuevo, accedemos por `FTP` con el acceso que ya tenemos y subiremos el `bash` de **Linpeas** para poder ejecutarlo en la maquina remota.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-22.png)

Sabemos que el `FTP` nos deja ubicado en la carpeta del sitio web, asi que nos posicionaremos en esta carpeta, le damos permisos de ejecucion al `bash` y verificamos que información nos va arrojando.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-23.png)

Dentro de toda la información que nos arroja, que es bastante extenso, podemos ver que ha encontrado una vulnerabilidad en el montaje de un recurso **`NTFS`**

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-24.png)

Buscando en algunos recursos de internet, que nos indique cómo realizar este montaje encuentramos que se puede realizar con una redireccion de puertos, asi que, como he mencionado en un [post anterior](https://ch4m17ux.github.io/2020/12/22/unbaked-pie-tryhackme-writeup.html), utilizare `Chisel`.

>Puedes encontrar mas informacion en: https://0xdf.gitlab.io/2020/08/10/tunneling-with-chisel-and-ssf-update.html

Lo que tenemos que hacer es ir al github oficial y descargar el ejecutable que necesitamos. Para que funcione la redireccion de puertos y poder montar el recurso, requerimos que `Chisel` este tanto en nuestra ***maquina local*** (server) como en la ***maquina remota*** (client), para poder copiar el binario en la maquina remota reutilizare el acceso FTP que ya tenemos.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-25.png)

Le damos permisos de ejecucional binario de `Chisel`, tanto en nuestra maquina local, como en la maquina remota.  Y una vez que se tiene permisos de ejecucion lo iniciamos, en nuestra maquina local como servidor y en la maquina remota como cliente.  

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-26.png)
>### Como informacion de aprendizaje
>$ chisel server --p 8000 --reverse
>En el lado del servidor (**`maquina local`**), el puerto *8000* es elegido aleatoriamente por nosotros para escuchar.
>
>$ ./chisel client 10.x.x.x:8000 R:2021:127.0.0.1:2021
*R:2021* significa que cuando la conexion es establecida en el puerto *8000* con tu servidor en la IP *10.x.x.x*, el servidor (**`maquina local`**), tambien abre el puerto *2021*. 
Luego cuando un paquete va hacia el puerto *2021* en tu lado, es redirigido al tunel en el puerto *8000* y enviado afuera a *127.0.0.1:2021* en la victima (**`maquina remota`**)
>
>Espero que hayas seguido el tema. (*y que haya podido ser claro*)

Una vez que tenemos conexión a traves de `Chisel`, vamos a tratar de montar el recurso `NFS` en nuestra maquina local.  Tal como hemos visto anteriormente al verificar ***/etc/exports***, podemos ver la configuracion para el *NFS*.  Cuando obtenemos ***fsid=0*** significa que la ubicacion ***/home/james*** como recurso raiz, sea igual a ***/*** .

En nuestra maquina local creamos una carpeta, donde montaremos el recurso *NFS* y ejecutamos el comando de montaje.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-27.png) 

Alli encontramos y obtenemos la flag de usuario.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-28.png)
### Flag de Root

Finalmente, nos hace falta realizar el ultimo escalado de privilegios y poder acceder al usuario `root`.  Podemos comenzar por obtener una `shell` como **James** y desde alli escalar hacia el usuario `root`.   Para esta finalidad, trataremos de obtener la llave privada SSH del usuario James, que parece tener mayores y mejores privilegios sobre la maquina.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-29.png)

Vamos a copiar el fichero **`id_rsa`** a nuestra maquina local, le asignaremos los permisos adecuados y accederemos como el usuario **James**.

 ![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-30.png)
 
Anteriormente habiamos visto que la vulnerabilidad era que que el recurso `NFS` lo podemos montar como root en nuestra maquina local y desde alli manipular todos los permisos.  

Vamos a seguir aprovechando esta vulnerabilidad y vamos a copiar un binario `bash` en el recurso `NFS` y cambiarle los permisos desde nuestra maquina local; de esta forma esperamos obtener una shell como root.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-31.png)

Ya hemos modificado los permisos, estableciendo un `SUID` y un permiso total; tambien hemos modificado el propietario para que sea `root`.  Lo podemos ver en nuestra maquina local y en la maquina remota.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-32.png)

Ejecutamos el binario bash que hemos modificado con estos permisos y obtenemos nuestra `shell` como ***`root`***

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-33.png)

### Flag de root

Ya que estamos como `root`, procedemos a sacar la ultima flag, que suponemos esta dentro de la carpeta **`/root`**

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-34.png)
## Conclusiones

Esta maquina, como hemos indicado al comienzo es una maquina de nivel medio, hay que comenzar a tener cierta expertiz y ciertos conocimientos para poder explotarla, hemos encontrado un camino que parecia sencillo, pero hemos podido comprobar que hay que realizar algo de **`"try Harder"`** para lograr escalar privilegios y alcanzar las flag propuestas.

Esperamos que esta guia haya sido clara y cualquier errata, duda o sugerencia, podeis hacernosla llegar por cualquiera de los medios aqui dispuestos.

# Fin