# OverPass3 - Hosting (Writeup - TryHackMe) 

![Reto Overpass3 - TryHackMe](https://ch4m17ux.github.io/img/posts/overpass3/tryhackme-overpass3.jpg)

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

Una ves que lo hemos descargado encontramos que hay dos ficheros: 

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