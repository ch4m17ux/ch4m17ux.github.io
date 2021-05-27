# #FromZeroToLynx - CTF writeUp

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

```bash
kali@kali:~/ZeroToLynx$ file granja.bsp
granja.bsp: data
```

Vemos que es un fichero con informacion de datos, asi que procedemos a verificar si encontramos algo entre sus `strings`. (*Aqui yo he ido aumentado el numero de caracteres que quiero que busque, debido a que me salia mucha información*)

```bash
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

```bash
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
```

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

```bash
    kali@kali:~/ZeroToLynx$ file tcpdump.pcap
    tcpdump.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Linux cooked v1, capture length 262144)
```

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

---
## **Secretos no tan secretos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Hemos encontrado dos documentos con información confidencial que contiene la localización de la bomba.
>
>¿Podrás descifrarla?


Nos entregan dos ficheros: confidential y secret. Los puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/confidential) y [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/secret)
Confidential: es un fichero cifrado.
Secret: es un fichero que contiene una llave RSA privada rota.

Verificamos los ficheros y vemos que la llave RSA privada que nos entregan esta rota, hay secciones que no tenemos y debemos por ende tratar de reconstruirla.

```code
┌──(kali㉿kali)-[~/CTF-Zerotolynx/rsa-challenge]
└─$ cat secret  
-----BEGIN RSA PRIVATE KEY-----
MIIG4wIBAAKCAYEAnq48eqHsUugZkz4rFqROVvPa9fvxqoJx6b81MuigBe9ANavd
YYNCrN8zryxHBo+l2Z0EkA11p1mF/swa0SFUfYnUsuZpfqjDvELrsWf+jmtxRrk4
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[----------REDACTED--------]AoHBANAiZPCv9AHjyhOJOBJBu1Ul1B0PPaBk
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-------------REDACTED---------]nQKBwQDDLFM+elj7PMd3hCd1Mv61OppQ
Fr9UNQ94zQ8XBba008u7UDrS2VaVxrT3jpCPTQvklqnZqN4aJnBII6Seb/2Io99M
7TA/ByqgxSnRst+M1F+xR68ghHOr6GKPO6oxc2abYZkIKd9LoERZjgXId9P+Y0GN
QHkUMhWFTOUh05hJLA+quaKxP+cylQMVFgLxWMql2wJ5aiR9MIkqovpugMBdKNiq
SoZclykLs2ZD1WtrC5zSN26ZDmm9yxMs3xi5ip8CgcBgt3rcdYcX0bg3d848fZsF
qDx2/HwQqmS5m25ufy31PJshUIyvw2u9NBVnnItVGSrdB1MvMDJFoSVpJVGx/6A2
eMsXp3UWIZwxc2yWYc/VHb0ACmuuF3VRR4cj4o6ZeEn+n6yRSIWry05bRTi7OdZg
J0412cx0EwA2qqc95HuHqLBOQ+Hd+UExj9q7MQKGJHa3iGdaxiHVMKeThD55qiiX
QeRick+jH6EKfU/dYg5/fqgug4C1TDlZovZY3R5n2+kCgcBShmiAb302ZkG1QHTq
snBOswPSv3uRIIp1OseZpXnWxgNMJaVpyCo7VHTqhCaN4TcZJbeV6DhZeE1bw250
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------------------]
[-----------------------REDACTED-------------------]
-----END RSA PRIVATE KEY-----
```

Lo arreglamos y quitamos las secciones que no tenemos para tratar de pasar de Base64 a Hexadecimal, para analizarlo y obtenemos:

#### PEM que nos dan
```code
-----BEGIN RSA PRIVATE KEY-----
MIIG4wIBAAKCAYEAnq48eqHsUugZkz4rFqROVvPa9fvxqoJx6b81MuigBe9ANavd
YYNCrN8zryxHBo+l2Z0EkA11p1mF/swa0SFUfYnUsuZpfqjDvELrsWf+jmtxRrk4
AoHBANAiZPCv9AHjyhOJOBJBu1Ul1B0PPaBk
nQKBwQDDLFM+elj7PMd3hCd1Mv61OppQ
Fr9UNQ94zQ8XBba008u7UDrS2VaVxrT3jpCPTQvklqnZqN4aJnBII6Seb/2Io99M
7TA/ByqgxSnRst+M1F+xR68ghHOr6GKPO6oxc2abYZkIKd9LoERZjgXId9P+Y0GN
QHkUMhWFTOUh05hJLA+quaKxP+cylQMVFgLxWMql2wJ5aiR9MIkqovpugMBdKNiq
SoZclykLs2ZD1WtrC5zSN26ZDmm9yxMs3xi5ip8CgcBgt3rcdYcX0bg3d848fZsF
qDx2/HwQqmS5m25ufy31PJshUIyvw2u9NBVnnItVGSrdB1MvMDJFoSVpJVGx/6A2
eMsXp3UWIZwxc2yWYc/VHb0ACmuuF3VRR4cj4o6ZeEn+n6yRSIWry05bRTi7OdZg
J0412cx0EwA2qqc95HuHqLBOQ+Hd+UExj9q7MQKGJHa3iGdaxiHVMKeThD55qiiX
QeRick+jH6EKfU/dYg5/fqgug4C1TDlZovZY3R5n2+kCgcBShmiAb302ZkG1QHTq
snBOswPSv3uRIIp1OseZpXnWxgNMJaVpyCo7VHTqhCaN4TcZJbeV6DhZeE1bw250
-----END RSA PRIVATE KEY-----
```
#### Codigo hexadecimal

308206e302010002820181009eae3c7aa1ec52e819933e2b16a44e56
f3daf5fbf1aa8271e9bf3532e8a005ef4035abdd618342acdf33af2c470
68fa5d99d04900d75a75985fecc1ad121547d89d4b2e6697ea8c3bc42
ebb167fe8e6b7146b938**0281c100**d02264f0aff401e3ca1389381241b
b5525d41d0f3da0649d**0281c100**c32c533e7a58fb3cc77784277532fe
b53a9a5016bf54350f78cd0f1705b6b4d3cbbb503ad2d95695c6b4f78
e908f4d0be496a9d9a8de1a26704823a49e6ffd88a3df4ced303f072aa
0c529d1b2df8cd45fb147af208473abe8628f3baa3173669b61990829
df4ba044598e05c877d3fe63418d4079143215854ce521d398492c0f
aab9a2b13fe7329503151602f158caa5db02796a247d30892aa2fa6e8
0c05d28d8aa4a865c97290bb36643d56b6b0b9cd2376e990e69bdcb1
32cdf18b98a9f**0281c060**b77adc758717d1b83777ce3c7d9b05a83c76
fc7c10aa64b99b6e6e7f2df53c9b21508cafc36bbd3415679c8b55192a
dd07532f303245a125692551b1ffa03678cb17a77516219c31736c96
61cfd51dbd000a6bae177551478723e28e997849fe9fac914885abcb4
e5b4538bb39d660274e35d9cc74130036aaa73de47b87a8b04e43e1d
df941318fdabb3102862476b788675ac621d530a793843e79aa28974
1e462724fa31fa10a7d4fdd620e7f7ea82e8380b54c3959a2f658dd1e6
7dbe9**0281c052**8668806f7d366641b54074eab2704eb303d2bf7b912
08a753ac799a579d6c6034c25a569c82a3b5474ea84268de1371925b
795e83859784d5bc36e74

La llave privada esta codificada en PEM (Privacy-Enhanced Mail) y los parametros que podemos encontrar en orden son: **n, e, d, p, q, dmod(p−1), dmod(q−1) and q−1modp.**

(https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/secretos-1.png)

Por lo que debemos buscar estos valores en lo que tenemos, y tratar de identificar cual de estos valores tenemos, para que a partir de estos podamos reconstruir la llave privada.

Teniendo en cuenta el encabezado ASN.1 para los valores entero es 02 82 01 01, que se descompone de la siguiente manera:

- **02** para el tipo de datos, aquí Integer.
- **82**, lo que significa que la longitud del valor entero se codificará en los 2 bytes siguientes.
- **0101**, la longitud real, cuyo valor entero es 257, lo que significa que el valor entero se codificará en los siguientes 257 bytes. Recuperar los siguientes 257 bytes en Big Endian y tomar sus valores enteros produce los valores rsa que estamos buscando.

Si buscamos en el hexadecimal que tenemos podemos ubicar los distintos valores que nos han dado:

**d**
308206e302010002820181009eae3c7aa1ec52e819933e2b16a44e56
f3daf5fbf1aa8271e9bf3532e8a005ef4035abdd618342acdf33af2c470
68fa5d99d04900d75a75985fecc1ad121547d89d4b2e6697ea8c3bc4
2ebb167fe8e6b7146b9384440c00931034440c00931034440c00931
034440c00931034440c00931034440c00931034440c00931034440
c00931034440c00931034440c00931034440c00931034440c00931
034440c00931034440c00931034440c0093103

**0281c1 p** 00d02264f0aff401e3ca1389381241bb5525d41d0f3da
0644440c00931034440c00931034440c00931034440c00931039d

**0281c1  q (base 64)** 00c32c533e7a58fb3cc77784277532feb53a9a5016bf54350f78cd0f1
705b6b4d3cbbb503ad2d95695c6b4f78e908f4d0be496a9d9a8de1a2
6704823a49e6ffd88a3df4ced303f072aa0c529d1b2df8cd45fb147af2
08473abe8628f3baa3173669b61990829df4ba044598e05c877d3fe6
3418d4079143215854ce521d398492c0faab9a2b13fe73295031516
02f158caa5db02796a247d30892aa2fa6e80c05d28d8aa4a865c9729
0bb36643d56b6b0b9cd2376e990e69bdcb132cdf18b98a9f

**0281c0 dmod(p-1)** 60b77adc758717d1b83777ce3c7d9b05a83c76fc7c10aa64b99b6e6e
7f2df53c9b21508cafc36bbd3415679c8b55192add07532f303245a1
25692551b1ffa03678cb17a77516219c31736c9661cfd51dbd000a6
bae177551478723e28e997849fe9fac914885abcb4e5b4538bb39d6
60274e35d9cc74130036aaa73de47b87a8b04e43e1ddf941318fdab
b3102862476b788675ac621d530a793843e79aa289741e462724fa
31fa10a7d4fdd620e7f7ea82e8380b54c3959a2f658dd1e67dbe9

**0281c0 dmod(q-1)**
528668806f7d366641b54074eab2704eb303d2bf7b91208a753ac7
99a579d6c6034c25a569c82a3b5474ea84268de1371925b795e83
859784d5bc36e744440c00931034440c00931034440c00931034
440c00931034440c00931034440c00931034440c0093103

Tenemos los valores completos de q y dmod(p-1).  Tomando un script que hemos conseguido para poder calcular p y N:

```code
##Python3
#import gmpy
from sympy import isprime

e = 65537
q = 0x00c32c533e7a58fb3cc77784277532feb53a9a5016bf54350f78cd0f1
705b6b4d3cbbb503ad2d95695c6b4f78e908f4d0be496a9d9a8de1a26704823
a49e6ffd88a3df4ced303f072aa0c529d1b2df8cd45fb147af208473abe8628
f3baa3173669b61990829df4ba044598e05c877d3fe63418d4079143215854c
e521d398492c0faab9a2b13fe7329503151602f158caa5db02796a247d30892
aa2fa6e80c05d28d8aa4a865c97290bb36643d56b6b0b9cd2376e990e69bdcb
132cdf18b98a9f
dp = 0x60b77adc758717d1b83777ce3c7d9b05a83c76fc7c10aa64b99b6e6e
7f2df53c9b21508cafc36bbd3415679c8b55192add07532f303245a12569255
1b1ffa03678cb17a77516219c31736c9661cfd51dbd000a6bae177551478723
e28e997849fe9fac914885abcb4e5b4538bb39d660274e35d9cc74130036aaa
73de47b87a8b04e43e1ddf941318fdabb3102862476b788675ac621d530a793
843e79aa289741e462724fa31fa10a7d4fdd620e7f7ea82e8380b54c3959a2f
658dd1e67dbe9

for kp in range(3, e):
    p_mul = dp * e - 1
#    print(p_mul)
    if p_mul % kp == 0:
        p = (p_mul // kp) + 1
        #print(p)
        if isprime(p):
            print("Possible p: {p}",p)

N = p*q
print("Valor de N: ",N)
```

Obtenemos los valores buscados:

```code

┌──(kali㉿kali)-[~/CTF-Zerotolynx/rsa-challenge]
└─$ python3 ./valor-n-p.py                                                  2 ⨯
Possible p: {p} 195964381578986226110833125117530514759298142493
7067449078522285594265904984207481421078656448527888795205931747
5195663008364018849372466071481741734035866773849096466701355618
4590216656265587045951673586345884770571606579112278451950854832
5100203974972887206141652901059600819709195960157904901441145036
2504717985750356152683210542891831838859210286503107843668747046
2533988621202078983708788663481756417308702973620949447515128954
0864482712680217349281213963677
Valor de N:  180053090851894882732301169407688044244269066553850
6234099314469966058984294950625268808164132978996913571156672450
9354683909356194690555324288939766620853767325406439981124632300
2008358212752379191612652136029991294853595946965196859741693482
0844541290694937870456685613207109977124274791033934230885433366
7384370652352070526243748928994309627278413639278957898138253231
9578187104555913345998601137067929714713611164857078126384737972
8420156134487666987288893076405559256754948991010321131279294460
5540853177448150240294730287403030444639234606195492628873103241
8768422026294831853457742842942759603226816221575074755602497845
7605359841835918660749706837262991741437911176732730471182369717
6959129699258609116759701620500559738374393878152272283480587083
4118052431182458331750288353891570639295134432531692099111431060
3841685337972341155977070405578742478929353656298266043957770721
188343146984504242621578759640441761491089
```

Estos valores estan en decimal, asi que el valor de Q debemos obtenerlo en decimal para poder utilizar el script [rsatool.py](https://github.com/ius/rsatool) que nos reconstruye la llave privada que estamos buscando.

Para poder encontrar el valor de Q, utilizamos una web que hace calculos de numeros grandes. Denominada ![MobielFish](https://www.mobilefish.com/services/big_number/big_number.php), asi que tratamos de calcularlo y obtenemos el numero.

**Q** (decimal)
18376103800202275865357228549606411279158033976955282966053946531
65922753390937424680934606761000858840983344383776780002913018800
46124738297582288816281929253207328909858761430428397769220588616
91984073474531512332135168017871662286990517772251224132943733742
03401221716769706888739026994068967129949520741516120851758575959
74115869106450628140832286141623304564440090382235522452492733616
12532101822354359126371878569868307202194938398601705140954807080
74670751

Con este numero Q y el valor de P que hemos obtenido, podemos reconstruir nuestra llave, haciendo uso del script rsatool.py que hemos mencionado mas arriba. (Recordar que estos numeros son primos)

```code
┌──(kali㉿kali)-[~/CTF-Zerotolynx/rsa-challenge]
└─$ python3 rsatool.py -f PEM -p 1959643815789862261108331251175305147
59298142493706744907852228559426590498420748142107865644852788879520593
17475195663008364018849372466071481741734035866773849096466701355618459
02166562655870459516735863458847705716065791122784519508548325100203974
97288720614165290105960081970919596015790490144114503625047179857503561
52683210542891831838859210286503107843668747046253398862120207898370878
86634817564173087029736209494475151289540864482712680217349281213963677
-q 18376103800202275865357228549606411279158033976955282966053946531659
22753390937424680934606761000858840983344383776780002913018800461247
38297582288816281929253207328909858761430428397769220588616919840734
74531512332135168017871662286990517772251224132943733742034012217167
69706888739026994068967129949520741516120851758575959741158691064506
28140832286141623304564440090382235522452492733616125321018223543591
2637187856986830720219493839860170514095480708074670751 -o clave.pem
Using (p, q) to initialise RSA instance

n =
9eae3c7aa1ec52e819933e2b16a44e56f3daf5fbf1aa8271e9bf3532e8a005ef4035
abdd618342acdf33af2c47068fa5d99d04900d75a75985fecc1ad121547d89d4b2e
6697ea8c3bc42ebb167fe8e6b7146b938305e6264f1062d2437fbbac595369b0640
860f7df6e22b24534da385376fe8dccdc4245aec487211dd2af7cc8083b06873105
b1dfa4d27b5b11ae858bff4f66db4b888115e13883d9ab878e1e44aa40a6855c707
ced52bf87644bb1168164b03d8fb8475c40014676611d88f22c423939483e77c47c
a046671885b5562bc0490c2f6b6765c65403532f151c6d2780c737251f519943b5b
84bf4c476f6debae59c95fb6718ad88c605d8fccf2577ceed8e6df1bbd1d37b1e70b
13e06198067beaeac87b437697a116c18723d004e4d24ae2da069fb619cf85547581
9ed710f8184c48b71d4188c80d9fff997f844c830be9c429cf16577d6e451f974ff34
2258156c3959c8d94008421548e8a5d74d659d4d8ba6ba6096c099a62454830fadfa6
aa3fb95c9c9bbc6ebf844683

e = 65537 (0x10001)

d =
162a9ad23aba6b9e76ac25fc18ee9ceef2a3bcc7142c508a9f2f91bbe9d928db122a2d
3700bf385a33d7e1799af664acb36886d1a4bfb1c004c2e23a40ca9a25eb5226279fc
70cc6430f4a237f368528a72b4d06776347f577e1f7fe5e3fb10896de88eb67aa1291
f322070acd04447a8093068189d1038f1c00c6c68e11c989eccdf89faeab333f4dcee7
642f38660ab7cdfd7ab7cb2b5ed9b87ac8b84b5abf9b877dc0e270511c5b1d5646202
75bc683b6d185d912d19f2de120f88cbea374aafca922dedf8aff82c6eaf5314fcab152
c20a0be55b3833d0ffd21cc87f1ad169f0ad349867535702adb38821fa91d29f5c97e
033beedfc9288673a0190a8e40d247d8bcc9e1d9e6b6e2473d7964996ea41415ae2d
c7ad793b9770f62e8401f4d182ccb90dddd57f9c262bf2a0da9e46892002c532cf5d9
ba8994a9bcbf79fa212edaf094bb00cf5fcd99734b20ab1b883b9bd9cc2c0f6318896a
f9d1344e85794934934230458a58b50c421eb2a365404c14422a0b5c34400109e209dc
28d9

p =
d02264f0aff401e3ca1389381241bb5525d41d0f3da06483e8aa79f8e29965fce042008
e084e5fde5fc0363813a6878a3b5d98752d15fd2bafdbc697e045041a5ebbbab0106373
4477e6d517f1a934c96dae637578b0162190789b285a7bd462717f24e931e821183e9
8c93e1763fef0d52a5c18f7ff0dce261ee221158c6674a49dde57cf22e0dedf33a7ef7003
496485367aa7bb3e376682bbc1f229aa830be839779312fe3a820b2ee0213cb53fbeb2
d328bac1d1c145b915f8ddfb91dd9d

q =
c32c533e7a58fb3cc77784277532feb53a9a5016bf54350f78cd0f1705b6b4d3cbbb503
ad2d95695c6b4f78e908f4d0be496a9d9a8de1a26704823a49e6ffd88a3df4ced303f072
aa0c529d1b2df8cd45fb147af208473abe8628f3baa3173669b61990829df4ba044598e
05c877d3fe63418d4079143215854ce521d398492c0faab9a2b13fe7329503151602f1
58caa5db02796a247d30892aa2fa6e80c05d28d8aa4a865c97290bb36643d56b6b0b9c
d2376e990e69bdcb132cdf18b98a9f

Saving PEM as clave.pem

┌──(ch4m0㉿kali)-[~/Descargas/CTF-Zerotolynx/rsa-challenge]
└─$ cat clave.pem     
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

Con esta llave privada RSA podemos descrifrar el mensaje que nos han entregado, haciendo uso de openssl.

```code
┌──(kali㉿kali)-[~/CTF-Zerotolynx/rsa-challenge]
└─$ openssl rsautl -decrypt -inkey clave.pem -in confidential -out flag.txt

┌──(kali㉿kali)-[~/CTF-Zerotolynx/rsa-challenge]
└─$ cat flag.txt
La bomba está en B! GOGOGOGOGOGO
ESL{L0s_S3cR3t0s_d3b3n_P3rM4n3c3r_S13mPr3_0cUlT0$}
```

Y asi obtenemos nuestra flag:
**ESL{L0s_S3cR3t0s_d3b3n_P3rM4n3c3r_S13mPr3_0cUlT0$}**
