# #FromZeroToLynx - CTF writeUp - Silver

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/banner.png)

En los este (y los siguientes) post quiero traer los retos que se estan desarrollando en el CTF desarollado por [ZeroLynx](https://www.zerolynx.com/es/home), donde se nos presentan retos enmarcados en el evento de ESL España CS:Go.

En esta entrada abordaré los retos del nivel basico o Silver.

Si quieres participar tienes información [ [Aquí](https://www.fromzerotolynx.gg/) ]

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 
---

## **Farm**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> La noche se te fue de las manos y te has quedado encerrado… ¡en una granja de pollos!
>
>¿Encontrarás la flag de salida?
>

Nos entregan un fichero con extensión `.bsp` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/granja.bsp))

Lo primero que hago siempre, es verificar que el fichero entregado sea lo que presuntamente nos dicen que es, asi que lo verificamos a traves del comando `file`:

```console
kali@kali:~/ZeroToLynx$ file granja.bsp
granja.bsp: data
```

Vemos que es un fichero con informacion de datos, asi que procedemos a verificar si encontramos algo entre sus `strings`. (*Aqui yo he ido aumentado el numero de caracteres que quiero que busque, debido a que me salia mucha información*)

```console
kali@kali:~/ZeroToLynx$ strings -n 45 granja.bsp
"axis" "512 -226.05 -27.8, 502.89 -223.53 -27.8"
"message" "ESL{MuyBienMatasteAlPolloCorrecto}"
materials/maps/granja/cubemapdefault.hdr.vtfVTF
materials/maps/granja/cubemapdefault.hdr.vtfPK
```
Hemos encontrado la flag que nos han solicitado: **ESL{MuyBienMatasteAlPolloCorrecto}**

*Otra opcion podria ser haber copiado el mapa en Counter Strike: Global Offensive y cargarlo para matar a los pollos, y de entrada jugar un rato.*

---

## **Pretorianos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> ¿Txh kdb pdv ohjhqgdulr txh od jxdugld suhwruldqd gh Mxolr Fhvdu?
>
>Y nos entregan una imagen:
>
>![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/pretorianos.png)

Tenemos que identificar que dice el mensaje que para estar codificado de alguna forma, asi que lo pasare por CyberChef y trataremos de obtener el mensaje.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/pretorianos_2.png)

Vemos que se descifra con Rot23 o lo que es lo mismo con cifrado Cesar.


---
## **Bomb has been planted **


Nos entregan la descripción del reto:

> **_OBJETIVO_**:  
> ¡La bomba ha sido plantada! ¿Serás capaz de desactivarla?
> 
> `nc challenges.fromzerotolynx.gg 2000`

**_Este reto es de #Reversing._**

En este reto nos adjuntan un fichero binario con extension `.bin` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/bomb.bin))

Como siempre hago, vamos a ver que efectivamente sea un binario:

    kali@kali:~/ZeroToLynx$ file bomb.bin
    bomb.bin: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6fa25e40bff22bdfd718b2d1fdbdc7c3dc2b1553, for GNU/Linux 3.2.0, stripped
    

En principio es un binario ELF, asi que lo podriamos ejecutar haber que nos muestra.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/bomb_bin.png)

**_spoiler_**: he tratado de resolverlo a traves de `Radare2` pero no lo veia muy claro, asi que he utilizado la alternativa de `OSINT` y buscar si, ya que esta ambientado en _Counter Strike:Global Offensive_, encuentro el codigo que solicitan, a traves de una busqueda en internet.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/bomb_bin_2.png)  

Observamos que la bomba que siempre plantan tiene el codigo: `7355608`. Asi que lo probaremos para ver que sucede.

    kali@kali:~/ZeroToLynx$ ./bomb.bin
    NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    XXXXXXXXXXXXXXXXXXXXXXXXXXddKXXXXXk0XXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXO00Ox0OcKXXXKoKXXKXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXX0XX0xKXdoXXXKoXXKOXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX0KXXKxKX0;XXX0dXK0OXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXOOOOOOkOkkxOO0;00OOdkkkkkkkkkkKXXXXXXXXXXXX
    XXXXXXXXXXXXXXKk0XKXKOOOOkO00:000OdOOOOOOOOOO0XXXXXXXXXXXX
    KXXXXXXXXXXXXKX00NXXXOO000kKKckKK0d000O0OKK000XXXXXXXXXXXX
    KKKKKKKKKKKK0k000XXXXOO0KXkKKOoKK0xKKKOKKKK000KKKKKKKKKKKK
    KKKKKKKKKKKK0OOO0XKXXOO0K0K0K0KKKKKK0K00O0OOK0KKKKKKKKKKKK
    KKKKKKKKKKKK0kkO0XKXX000K0K0K0K00K0K0K0K000000KKKKKKKKKKKK
    KKKKKKKKKKKKKKK0ONXdolodKNXKxxxxxxxxxdddddd000KKKKKKKKKKKK
    KKKKKKKKKKKKKKK0OKX:;;:lKNXKkkkkkkkkkkkkkkk000KKKKKKKKKKKK
    KKKKKKKKKKKKKKKOkXNNNOk0KKKKXXXXXXXX000OO000O0KKKKKKKKKKKK
    0000000000000000OONX0kkkxOO00KlccckOkkxkxOOOk0000000000000
    0000000000000000OOXX0kxkxOKKXXxdddKK00OkxOOOO0000000000000
    0000000000000000kKXNXkxkkKXNNNXXXXXNNXKOkOOOO0000000000000
    000000000000000Ok00KOOkkkKXXO0X0OX00KXKOkO00O0000000000000
    000000000000000Ok0OKKOOOOKXXOOX00X00KXKOk00OO0000000000000
    000000000000000OxkkkOOkOOKXXkxXkxKOk0XKOO00OO0000000000000
    OOOOOOOOOOOOOOOOxkkkkOOO0KXXKKXK0XKKKXX0OOOOO0OOOOOOOOOOOO
    OOOOOOOOOOOOOOOOxxkkkkkO0KXXkxXkxKOk0XX0O0OOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOkkkkkkkO0KXXOOX0OK0OKXX0OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOxkOOOOOOOKXX0OX00XK0KXX0000OOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOxxkkkkkkkO0KXKKKKKKKK00OOOOO0OOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOkOOkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
    La bomba ha sido plantada.
    ¿Serás capaz de desactivarla a tiempo?
    No tienes el kit para desactivar bombas por lo que solo dispones de 10 segundos... ¡date prisa!
    Quedan 08 segundos. Introduce el código para desactivar la bomba: 0856
    Quedan 07 segundos. Introduce el código para desactivar la bomba:
    ¡Bomba desactivada!
    
    Felicidades, la flag es ESL{S13mPr3_H4y_Qu3_Pl4nT4R_3n_lUg4R_S3gUr0}
    

Obtenemos la flag que nos han solicitado: **`ESL{S13mPr3_H4y_Qu3_Pl4nT4R_3n_lUg4R_S3gUr0}`**

* * *

**Shoot to kill!**
------------------

Nos entregan la descripción del reto:

> **_OBJETIVO_**:  
> Hemos recibido un modelo 3D de una AK, pero creemos que hay algo oculto…

**_Este reto es de #Stego._**

En este reto nos adjuntan un fichero con extension `.fbx` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/AK.FBX))

Como siempre hago, vamos a ver que tipo de fichero es:

    kali@kali:~/ZeroToLynx$ file AK.FBX
    AK.FBX: data
    

Parece que es un fichero de `datos` o `ascii`, verificando en internet que tipo de extension es esta podemos ver que se trata de un fichero de 3D y la primera referencia nos indica que se puede visualizar con `Autodesk`.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/shoot-to-kill.png)

Sin embargo, no he logrado visualizar nada en la imagen, asi que tratare de ver si tiene algo entre sus `strings`.

No he visualizado nada que pueda indicar algo acerca de la flag. Por esta razón, he buscado en internet con que software puedo visualizar la imagen y ver sus componentes; y he encontrado que podemos editarlo en Blender, lo he instalado y he abierto el fichero alli.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/shoot-to-kill_2.png)

Buscando y buceando en todas las opciones de Blender, he encontrado que hay una seccion de texturas o lo que es lo mismo, lo que se visualizara cuando lo veamos como la imagen anterior.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/shoot-to-kill_3.png)

Y finalmente, cuando me fijo en las texturas, visualizo que hay una marca que parece ser la flag.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/shoot-to-kill_4.png)

Asi que la flag solicitada es:  
**`ESL{BANG!}`**

---

## **Canal… ¿seguro?**

Nos entregan la descripción del reto:

> **_OBJETIVO_**:  
> Hemos conseguido pinchar las comunicaciones de un ordenador de la base ct. Se piensan que sus comunicaciones son seguras…
> 
> ¿Crees que podrías encontrar algo interesante?

**_Este reto es de #Forense._**

En este reto nos adjuntan un fichero con extension `.pcap` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/tcpdump.pcap))

Como siempre hago, vamos a ver que el fichero es lo que nos indican que debe ser:

    kali@kali:~/ZeroToLynx$ file tcpdump.pcap
    tcpdump.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Linux cooked v1, capture length 262144)
    

En principio, el fichero si corresponde con una captura de red. Por lo que lo abrimos en WireShark.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/canal-seguro.png)  

Generalmente lo que hago antes estos retos es verificar si dentro de la comunicacion de red, se ha intercambiado algun fichero interesante, para esto, debemos ir al menu "`Archivo`" - "`Exportar Objetos`" - "`HTTP...`"

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/canal-seguro_2.png)

Y alli nos saldra una ventana con los objetos HTTP que podriamos descargar, procedemos a verificar si hay algo que nos sirva.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/canal-seguro_3.png)

Encontramos que justo tenemos un fichero _`flag.zip`_ que ha sido transmitido. Procedemos a descargarlo para poder revisarlo.

Verificamos si realmente es un fichero ZIP:

    kali@kali:~/ZeroToLynx$ file flag.zip
    flag.zip: Zip archive data, at least v2.0 to extract
    

Tenemos que es un fichero comprimido, tratamos de descomprimirlo para acceder a su contenido:

    kali@kali:~/ZeroToLynx$ unzip flag.zip
    Archive:  flag.zip
       creating: flag/
       creating: flag/.code/
      inflating: flag/.code/.core.bat
      inflating: flag/flag.bat.lnk
    

Nos crea una carpeta _`/flag`_ con algunos ficheros, que si los visualizamos en Windows estaran ocultos. Me interesa el fichero **_`.core.bat`_**, vamos a ver que contiene:

    kali@kali:~/ZeroToLynx$ cat flag/.code/.core.bat
    @echo off
    :loop
    SET /p pass="Introduzca la pass: "
    echo %pass%
    IF "%pass%" == "TUCeWprgc9rNJAgQnr8BNDqT" (
            ECHO ESL{TH1S_1S_TH3_FLAG_MY_FR13ND}
    ) ELSE (
            ECHO Vuelve a intentarlo...
    )
    GOTO loop
    

Encontramos la flag que estabamos buscando:  
**ESL{TH1S_1S_TH3_FLAG_MY_FR13ND}**

---
## **Pi Pi Piiii**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> En esta imagen se oculta algo que Vail conocía muy bien

***Este reto es de #Stego.***

En este reto nos adjuntan un fichero con extension `.jpg` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/cables.jpg))

Como siempre hago, vamos a ver que el fichero es lo que nos indican que debe ser:

```console
kali@kali:~/ZeroToLynx$ file cables.jpg
cables.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1280x720, components 3
```

Vemos que es una imagen JPG, asi que vamos a verificar si dentro de los strings podemos ver algo:

```console
kali@kali:~/ZeroToLynx$ strings -n 10 cables.jpg
1r&IO!9I2       7
AsUp{(4.X9
G'nM*fKo>o
-6v     -PJ{$>
KR[*BSzU%%Y
x:`p;L-a~7
. ... .-.. { ...-- ... - ----- ..--.- ...-- ...-..- -....- ..- -. ....- -...- ..-. .. ....- --. ..--.- ...- ....- .---- .. -.. ....- }
```

Los strings nos arroja que hay algo interesante, y por la pista del titulo del reto, suponems que es un codigo morse.

Lo copiamos y a traves de un decodificador de morse, tratamos de obtener la informacion:

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/pi.png)

De forma muy sencilla obtenemos la flag que nos solicitan:

**ESL{3ST0_3$-UN4=FI4G_V41ID4}**

---
## **Wallhacks**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Hemos jugado con un chetoso que usa wallhacks. ¿Lo encontraremos?
>
>`76561199151583346`
>
>Go go go!

***Este reto es de #OSINT.***

En este reto nos dan un numero, que debemos buscar o intentar descifrar a qué corresponde.

He supuesto, que como hablan de un "Chetoso" (usuario), entonces corresponderia a su nombre o codigo de usuario.  Asi que hago una busqueda para ver cuales son los foros mas activos de Counter Strike (recordad que el CTF esta enmarcado en un evento de este juego):

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/wallhacks.png)

En este caso, podemos decantarnos por el foro oficial de CS:GO, que se encuentra en SteamCommunity.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/wallhacks_2.png)

Revisamos como se esta codificando a los usuarios alli, y vemos si por alli encontramos el usuario que estamos buscando.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/wallhacks_3.png)

Encontramos que los usuarios (algunos) se codifican con un numero largo, por lo que podriamos suponer que este numero correspondera al usuario que nos estan solicitando. Probamos y veremos si lo conseguimos:

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/wallhacks_4.png)

Vemos un usuario, que tiene relacion con el evento que se esta desarrollando, vamos a investigar si encontramos algo en la descripcion de perfil:

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/wallhacks_5.png)

Encontramos la flag que nos estan solicitando:
**ESL{¡ElOSINTSeTeDaMuyBien!}**

---
## **Muerte en el jardín**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Ayer morí 64 veces en Cobblestone. Odio ese mapa.

***Este reto es de #Crypto.***

Nos entregan un fichero sin extensión (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/de_cobblestone))

No sabemos que tipo de fichero nos han entregado, por esta razon, podemos proceder a verificar de que tipo estamos tratando:

```console
kali@kali:~/ZeroToLynx$ file de_cobblestone
de_cobblestone: ASCII text
kali@kali:~/ZeroToLynx$ cat de_cobblestone
TGEgZmxhZyBlcyBFU0x7YmFzZTY0KGNvYmJsZXN0b25lKX0K
```

Nos encontramos frente a un fichero que contiene una cadena de texto.  La podemos copiar en cyberchef para que nos diga si esta cifrado y en que cifrado nos lo entregan.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/cobblestone.png)
La cadena de texto nos indica que la flag buscada es como se indica alli:
**ESL{base64(cobblestone)}**

Aunque no todo es tan sencillo, ya que esta realmente no es la flag buscada; y leyendo la descripcion podemos inferir que debemos ejecutar lo que nos pone alli, sacar el `Base64` de la palabra *cobblestone*.

Lo hacemos a traves de cyberchef:

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/cobblestone_2.png)
Pero al introducirlo como flag, nos pone que es incorrecto.  Asi que, no debemos confirnarnos de las paginas web, lo hare a traves de la consola.

```console
kali@kali:~/ZeroToLynx$ echo "cobblestone" | base64
Y29iYmxlc3RvbmUK
```

Lo intento con este que me arroja la consola y si que me la acepta.

Por lo tanto, encontramos la flag que nos estan solicitando:
**ESL{Y29iYmxlc3RvbmUK}**


---
## **Rush B!**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Hay un Comando en busca de una bomba, ¿Darás con ella sin perderte?

***Este reto es de #ComandoLinux.***

Nos entregan un fichero comprimido con extension `tar.gz` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/Rush.tar.gz))

Verificamos si efectivamente es un tar.gz y de serlo, procedemos a descomprimirlo:

```console
kali@kali:~/ZeroToLynx$ file Rush.tar.gz
Rush.tar.gz: gzip compressed data, was "Rush.tar", last modified: Wed Mar 31 09:00:21 2021, 
max speed, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 1106863616
```
Podemos observar que el tamaño del fichero original es: `original size modulo 2^32 1106863616`

Lo que significa que si lo tratamos de descomprimir se hara muy grande y puede que nos "cuelgue" el sistema operativo.  Incluso, tratando de hacerlo por linea de comandos, nos da errores:

```console
kali@kali:~/ZeroToLynx$ tar xzvf Rush.tar.gz
tar: a: Cannot mkdir: Permission denied
tar: a/a/a/a/a/a/a/a/a/a/a/b/a/c: Cannot mkdir: No such file or directory
a/a/a/a/a/a/a/a/a/a/a/b/a/c/a/
tar: a: Cannot mkdir: Permission denied
tar: a/a/a/a/a/a/a/a/a/a/a/b/a/c/a: Cannot mkdir: No such file or directory
a/a/a/a/a/a/a/a/a/a/a/b/a/c/a/a/
tar: a: Cannot mkdir: Permission denied
```

Lo que trata es de crear miles de subcarpetas, alcanzando el limite que podria llegar a manejar.  Esto es llamado "[Bomba Zip](https://es.wikipedia.org/wiki/Bomba_zip)"

>La **bomba zip,** también conocida como **zip de la muerte**, es un archivo malicioso diseñado para bloquear o inutilizar un programa o sistema que lo está leyendo. Este tipo de archivo malicioso explota el algoritmo de compresión de [ZIP](https://es.wikipedia.org/wiki/Formato_de_compresi%C3%B3n_ZIP "Formato de compresión ZIP") para guardar grandes cantidades de datos.

Debemos cambiar nuestro enfoque, nos piden que busquemos una bomba, suponemos que dentro de todos esos subdirectorios y lo que pueda crear hay un flag, por lo que debemos recurrir a un comando.  He tratado de utilizar `zgrep`, pero no me ha dado solucion, asi que recurro a `python` y encuentro un codigo que hace esto mismo usando el modulo `tarfile`.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/rushb.png)

Usamos este script, sabiendo cual es el formato de la flag y obtenemos:

```console
kali@kali:~/ZeroToLynx$ python3 buscar_tar.py "ESL" Rush.tar.gz
Cadena encontrada en los siguientes ficheros
a/a/a/a/a/a/a/a/a/a/a/b/a/c/a/a/a/b/d/a/a/b/c/d/c/c/d/b/b/c/b/d/b/d/c/c/b/b/c/d/c/d/a/b/b/Bombsite
```

Sabemos donde esta el fichero que contiene la flag, asi que podemos descomprimir este unico fichero y leerlo:

```console
kali@kali:~/ZeroToLynx$ sudo tar xzf Rush.tar.gz a/a/a/a/a/a/a/a/a/a/a/b/a/c/a/a/a/b/d/a/a/b/c/d/c/c/d/b/b/c/b/d/b/d/c/c/b/b/c/d/c/d/a/b/b/Bombsite
kali@kali:~/ZeroToLynx$ cat a/a/a/a/a/a/a/a/a/a/a/b/a/c/a/a/a/b/d/a/a/b/c/d/c/c/d/b/b/c/b/d/b/d/c/c/b/b/c/d/c/d/a/b/b/Bombsite
ESL{Bu3n_s1t10_p4rA_P1ant4R}
```

Por lo tanto, encontramos la flag que nos estan solicitando:
**ESL{Bu3n_s1t10_p4rA_P1ant4R}**

>Esta no es la unica solucion, y puede que haya otros caminos mas faciles, pero es el que me ha servidor a mi.


---
## **Victory's sound**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Nos hemos colado en el Discord del contrincante y hemos grabado sus planes, aunque con algunas interferencias de extraña procedencia que no logramos descifrar. ¿Puedes ayudarnos?

***Este reto es de #Stego.***

Nos entregan un fichero con extension `mp3` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/victory.mp3))

Como has podido ver en mi blog, siempre verifico que lo que nos entregan corresponde con lo que presuntamente nos dicen que debe ser.

```console
kali@kali:~/ZeroToLynx$ file victory.mp3
victory.mp3: Audio file with ID3 version 2.3.0, contains:MPEG ADTS, layer III, v2,  64 kbps, 22.05 kHz, JntStereo
```
Observamos que es un fichero mp3 como nos han indicado.

Procedemos a abrirlo y ver que podemos visualizar o escuchar. Escuchamos una musica, pero de un instante a otro hay una presunta interferencia. He decidido abrirlo en un decodificar de audio morse, para ver si me arroja algun mensaje. He usado [esta](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) pagina.

Y vemos que en el espectograma arroja unos caracteres, que si nos fijamos es la flag buscada.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/victory.png)
Por lo tanto, encontramos la flag que nos estan solicitando:
**ESL{H4CK_TH3_B0MB}**