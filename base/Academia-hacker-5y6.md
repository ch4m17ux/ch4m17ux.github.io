# Academia Hacker Incibe - #writeUp - 5 y 6 semana

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---

## **Reto 21**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>En clases de informática, el profesor está distribuyendo unos binarios que necesitan de una cadena mágica como parámetro para probar las habilidades de los alumnos.
>
>Pregunta
>¿Puedes encontrar la cadena mágica que devuelve la flag?
>
>**Datos proporcionados:**
>
>Flag.

Arrancamos IDA Pro para ver cómo funciona el binario y empezar a investigar:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto21-1.png)

Revisando el codigo, vemos que para que nos de la salida esperada:

-   Nos pide que el valor a añadir lo incluyamos como parámetro despues del nombre del binario: Ej: “flag XXXXXXXXXXXXX”.
    
-   Por otra parte vemos que hay 2 compares “cmp”. Uno donde nos dice que el parámetro ha de contener 21 digitos/caracteres y el otro que la suma de esos digitos/caracteres pasados a char ha de sumar 929 en Hexadecimal, 2345 en decimal.

Ahora probamos a ver si IDA nos puede dar el código:

(En IDA con F5 vemos el codigo en formato mas legible. (OJO solo se ve cuando no esta prótegido el codigo)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto22-1.png)

Cogemos la tabla ascii para ver valores char hasta completar una suma de 2345 en decimal con 21 valores:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto23-1.png)

Y pasarlos a formato ASCII sabiendo el char() correspondiente.

En Excel tenemos la posibilidad de hacer uso de la formula CODIGO() para que nos devuelva el valor char() de cualquier codigo ascii. Jugamos un poco con ellos y vemos que podemos probar con uno al azar:

|||
|--|--|
|  {|123  |
|{|123|
|v|118|
|e|101|
|x|120|
|t|116|
|r|114|
|a|97|
|c|99|
|t|116|
|t|116|
|h|104|
|e|101|
|f|102|
|l|108|
|a|97|
|g|103|
|v|118|
|w|119|
|}|125|
|}|125|
|||
||2345|

```bash
┌──(kali㉿kali)-[~/Descargas/incibe/5 semana/reto21]
└─$ ./flag {{vextracttheflagvw}}
Aquí tienes la flag:
flag{la_tabla_ASCII}
```

Y obtenemos la flag que nos estan pidiendo:
***flag{la_tabla_ASCII}***

---
## **Reto 22**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Las clases de manualidades e informática han preparado de manera conjunta un problema para los alumnos en el que se esconde un mensaje en un collage.
>
>Pregunta
>¿Eres capaz de encontrar el mensaje oculto?
>
>**Datos proporcionados:**
>
>Flag.jpg

Despues de verificar los strings, los metadatos, ver si hay alguna informacion oculta, a Dany se le ha ocurrido que la flag esta a simple vista; esto es que si codificamos cada imagen que compone el collage podemos sacar la flag en hexadecimal, teniendo en cuenta que:

"flag{" corresponde en Hex a "66 6C 61 67 7B"

Asi que tenemos la imagen que nos entregan:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto22-1.png)

Y al irla codificando obtenemos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto22-2.png)

Que si lo pasamos a hexadecimal obtenemos (haciendo un poco de maquillaje y guessing):

*66 6c 61 67 7b 68 65 78 61 64 65 63 69 6d 61 6c 2d 63 6f 6e 76 65 72 74 69 64 30 2d 65 6e 2d 63 2a 6c 6c 61 67 65 2d 64 65 2d 69 6d 61 67 65 6e 7d*

Que al decodificarlo obtenemos la flag:

***flag{hexadecimal-convertid0-en-c*llage-de-imagen}***

---
## **Reto 23**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En clase de informática te piden que compruebes qué hace el siguiente trozo de código.
>
>Aparentemente no realiza ninguna acción
>
>Pregunta
>
>¿Puedes hacerlo funcionar o extraer información de este?
>
>**Datos proporcionados:**
>
>Flag.js

Nos entregan un fichero javascript que parece estar ofuscado, asi que lo pasamos por un desofuscador y obtenemos:

```js
var _0x30de = ['mZa1ntnUsLrKCKG', 'zwPLyW', 's3jjsG', 'ota2ntjHELPsvg4', 'm21yBvviDG', 'nJC4ouHKwfDzuq', 'zNvUyW', 'ndDzrLnir0S', 'E25VxW', 'odm3ndvzAuTPreS', 'mtm1m1rXCg5rCG', 'zMXHzW', 'Aw9UFq', 'mtK2oti1y1jSBgzT', 'mti3sMnMCg9K', 'DxrHCG', 'mtnru2HKB2m', 'mNfkBe9Nta', 'Bg9N', 'mta3nJG5wfrMEeHk', 'B2X2Aq'];
var _0x45c1 = function (_0x41d678, _0x5378d3) {
    _0x41d678 = _0x41d678 - (0x11 * -0x79 + 0x2420 * -0x1 + -0x2d07 * -0x1);
    var _0x6f67ce = _0x30de[_0x41d678];
    if (_0x45c1['iTqplC'] === undefined) {
        var _0x1f4261 = function (_0x1d2e0e) {
            var _0x18535e = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
            var _0x4d38ea = '';
            for (var _0x1f83ef = -0x2 * 0x126a + -0x17e2 + 0x3cb6, _0x40eab8, _0x4cab8c, _0x9867a0 = -0xa * -0x52 + 0x5 * -0x10 + 0x4a * -0xa; _0x4cab8c = _0x1d2e0e['charAt'](_0x9867a0++); ~_0x4cab8c && (_0x40eab8 = _0x1f83ef % (0x12c6 + 0x52 * -0xd + -0xe98) ? _0x40eab8 * (0xcb * -0x1c + 0x1 * -0x803 + 0x1e77) + _0x4cab8c : _0x4cab8c, _0x1f83ef++ % (-0x89 * 0xd + -0x12 * -0xdc + -0x57 * 0x19)) ? _0x4d38ea += String['fromCharCode'](0x23ce + 0x1cd8 + 0x5 * -0xcbb & _0x40eab8 >> (-(-0xde8 + -0x4ae * -0x3 + 0x2 * -0x10) * _0x1f83ef & 0x211b * -0x1 + 0x240d * 0x1 + 0x44 * -0xb)) : -0x230 * -0x5 + -0x52 * -0x1e + -0x148c) {
                _0x4cab8c = _0x18535e['indexOf'](_0x4cab8c);
            }
            return _0x4d38ea;
        };
        _0x45c1['OpkxWb'] = function (_0x1cd694) {
            var _0x19aed2 = _0x1f4261(_0x1cd694);
            var _0x682b5b = [];
            for (var _0x10887a = -0x1f59 + -0x142f * 0x1 + 0x11 * 0x308, _0x5616e7 = _0x19aed2['length']; _0x10887a < _0x5616e7; _0x10887a++) {
                _0x682b5b += '%' + ('00' + _0x19aed2['charCodeAt'](_0x10887a)['toString'](-0x695 + -0x1241 * -0x2 + 0x37 * -0x8b))['slice'](-(0x11f * -0x22 + -0xd * 0x11 + 0xcff * 0x3));
            }
            return decodeURIComponent(_0x682b5b);
        }, _0x45c1['FVpRax'] = {}, _0x45c1['iTqplC'] = !![];
    }
    var _0x3cf3d8 = _0x30de[-0x1b65 + -0x2118 + 0x3c7d],
        _0x541f8e = _0x41d678 + _0x3cf3d8,
        _0x1d915e = _0x45c1['FVpRax'][_0x541f8e];
    return _0x1d915e === undefined ? (_0x6f67ce = _0x45c1['OpkxWb'](_0x6f67ce), _0x45c1['FVpRax'][_0x541f8e] = _0x6f67ce) : _0x6f67ce = _0x1d915e, _0x6f67ce;
};
(function (_0x41153a, _0x2421b4) {
    var _0x2618b3 = _0x45c1;
    while (!![]) {
        try {
            var _0x5c9249 = parseInt(_0x2618b3(0xf0)) * parseInt(_0x2618b3(0xee)) + -parseInt(_0x2618b3(0xe2)) * -parseInt(_0x2618b3(0xe4)) + -parseInt(_0x2618b3(0xea)) + parseInt(_0x2618b3(0xe1)) * -parseInt(_0x2618b3(0xe6)) + -parseInt(_0x2618b3(0xe0)) + -parseInt(_0x2618b3(0xed)) * -parseInt(_0x2618b3(0xf2)) + -parseInt(_0x2618b3(0xe7)) * parseInt(_0x2618b3(0xeb));
            if (_0x5c9249 === _0x2421b4) break;
            else _0x41153a['push'](_0x41153a['shift']());
        } catch (_0x44fefa) {
            _0x41153a['push'](_0x41153a['shift']());
        }
    }
}(_0x30de, 0xe1a6 * -0x5 + 0x56ea2 + -0x37 * -0xaed));

function _146154141147() {
    var _0x52e3c3 = _0x45c1,
        _0x4699b4 = {};
    _0x4699b4[_0x52e3c3(0xdf) + 'D'] = _0x52e3c3(0xe8) + _0x52e3c3(0xe5) + _0x52e3c3(0xf1) + 'des_' + _0x52e3c3(0xde) + _0x52e3c3(0xec) + '_la_' + _0x52e3c3(0xe3) + _0x52e3c3(0xe9);
    var _0x2a9b51 = _0x4699b4;
    console[_0x52e3c3(0xef)](_0x2a9b51[_0x52e3c3(0xdf) + 'D']);
}
```
Que nos dice pocas cosas, pero revisando en un depurador de javascript (https://jshint.com/) menciona aparte de algunas alertas, que hay una funcion que nunca se hace uso de ella.  Asi que procedemos a ejecutar el javascript desde un navegador, y verificamos que nos dice dicha funcion.

Abrimos la consola del navegador (con F12) y pegamos alli el codigo (hay otra forma de hacerlo, que me lo explicaron pero no lo entendi, y era importando el fichero directamente)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto23-1.png)

Hacemos el llamado a la funcion y obtenemos la flag:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto23-2.png)

Obtenemos la flag:
***flag{no_olvides_ejecutar_la_funcion}***

---
## **Reto 24**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>En clase de lengua se ha estudiado la táctica a seguir para optimizar juegos del tipo de la ruleta de la fortuna.
>
>Pregunta
>¿Podrás aplicar esos conocimientos al siguiente texto para encontrar el mensaje oculto?
>
>**Datos proporcionados:**
>
>text.txt

Tenemos un fichero que contiene un texto que al leerlo no parece tener sentido, asi que lo he pasado por un analisis de cifrados (http://web.archive.org/web/20120624074941/http://home.comcast.net/~acabion/refscore.html) y desde alli encuentro que es un cifrado Patristocrat.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto24-1.png)

Que en otras web lo llaman, cifrado de sustitucion monoalfabetica. Podriamos resolverlo con esta web. (https://www.boxentriq.com/code-breaking/cryptogram) y nos arroja la solucion:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto24-2.png)

Asi que le damos a la lupa y podemos ver como lo ha resuelto:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto24-3.png)

Revisando ya el texto descifrado encontramos la fla al final:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto24-4.png)

Obtenemos la flag:
***flag{analizando_la_frecuencia_en_un_texto}***

---
## **Reto 25**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>La profesora de música ha reproducido una canción que será el himno oficial de final de curso. Para conseguir aprobar la asignatura es necesario descubrir un código oculto en el mismo.
>
>Pregunta:
>¿Podrías descubrir el mensaje oculto?
>
>**Datos proporcionados:**
>
>Fichero de audio en formato wav descargable

Tenemos un fichero wav, que nos confunde mucho, ya que no vemos nada entre sus string y su espectograma, lo cual es desconcertante.

Revisando los metadatos encontramos un comentario:

```bash
kali@kali:~/incibe$ exiftool reto25.wav
ExifTool Version Number         : 11.88
File Name                       : reto25.wav
Directory                       : .
File Size                       : 38 MB
File Modification Date/Time     : 2021:06:04 13:38:43+02:00
File Access Date/Time           : 2021:06:04 13:38:55+02:00
File Inode Change Date/Time     : 2021:06:04 13:38:55+02:00
File Permissions                : rw-r--r--
File Type                       : WAV
File Type Extension             : wav
MIME Type                       : audio/x-wav
Encoding                        : Microsoft PCM
Num Channels                    : 2
Sample Rate                     : 44100
Avg Bytes Per Sec               : 176400
Bits Per Sample                 : 16
Comment                         : ynDnHK6ZGwxXcz2e
Duration        
                : 0:03:43
```

Despues de dar muchas vueltas, probamos con steghide para ver si contenia algo, pero nos encontramos que solicitaba una contraseña; probamos con lo que aparecia en el comentario y vimos que habian ficheros ocultos:

```bash
kali@kali:~/incibe$ steghide --info reto25.wav
"reto25.wav":
  format: wave audio, PCM encoding
  capacity: 1.2 MB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded data:
    size: 644.8 KB
    encrypted: rijndael-128, cbc
    compressed: yes
```

Procedemos entonces a obtener la informacion adjunta:

```bash
kali@kali:~/incibe$ steghide extract -sf reto25.wav
Enter passphrase:
steghide: please specify a file name for the extracted data (there is no name embedded in the stego file).
```

Nos han adjuntado un fichero que debemos nosotros especificarle el nombre asi que lanzaremos un comando mas agradable para que nos lo copie. Y vemos que tipo de fichero nos extrae.

```bash
kali@kali:~/incibe$ steghide extract -sf reto25.wav -p ynDnHK6ZGwxXcz2e -xf flag
wrote extracted data to "flag".
kali@kali:~/incibe$ file flag
flag: Zip archive data, at least v2.0 to extract
```
Nos obtiene un fichero zip, procedemos a descomprimirlo:

```bash
kali@kali:~/incibe$ unzip flag
Archive:  flag
  inflating: file01.png
  inflating: file02.png
kali@kali:~/incibe$ ll
total 40060
drwxr-xr-x 1 ch4m0 ch4m0     4096 Jun  4 13:51 ./
drwxr-xr-x 1 ch4m0 ch4m0     4096 Jun  4 13:26 ../
-rwxrwxrwx 1 ch4m0 ch4m0   324134 Feb 19 14:37 file01.png*
-rwxrwxrwx 1 ch4m0 ch4m0   335675 Feb 19 14:37 file02.png*
-rw-r--r-- 1 ch4m0 ch4m0   660232 Jun  4 13:48 flag
-rw-r--r-- 1 ch4m0 ch4m0 39379096 Jun  4 13:38 reto25.wav
```

Ahora obtenemos dos ficheros png. Decidimos pasarlo por un web de Stego para ver si encontrabamos algo interesante, y en el fichero file01.png no habia nada que resaltar, pero en el fichero02.png, encontramos que jugando con los colores visualizabamos algun texto.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto25-1.png)

Esto se obtuvo con la opcion de LSB, y vemos en la parte superior izquierda la flag.

Obtenemos la flag:
***flag{LSB_reto_superado}***

---
## **Reto 26**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>El director se ha dejado olvidado en una clase un USB con un fichero dentro, los datos parecen no ser muy relevantes, pero... parece que esconde un mensaje.
>
>Pregunta:
>¿Cómo podemos obtener el mensaje?
>
>**Datos proporcionados:**
>
>Fichero de texto con peticiones HTTP

Analizamos el fichero:

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/6 semana/reto26]
└─$ exiftool access.log 
ExifTool Version Number         : 12.16
File Name                       : access.log
Directory                       : .
File Size                       : 92 KiB
File Modification Date/Time     : 2021:03:11 19:13:00+01:00
File Access Date/Time           : 2021:07:09 13:49:31+02:00
File Inode Change Date/Time     : 2021:07:09 13:49:31+02:00
File Permissions                : rwxrwxrwx
File Type                       : TXT
File Type Extension             : txt
MIME Type                       : text/plain
MIME Encoding                   : us-ascii
Newlines                        : Unix LF
Line Count                      : 595
Word Count                      : 11305
```
Importamos los datos a Excel y vemos que hay una secuencia entre las tramas, parecida al reto de Santa Clauss de Hackrock, pero s este caso solo tenemos tramas 200 y tramas 400.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto26-1.png)
Calculamos cuantas tramas 400 hay entre las tramas 200 y nos van dando valores en hexadecimal, en la captura del excel seria el comienzo: 757

Si seguimos contabilizando salen estos valores.

```bash
75736572732C666C616769642C666C616731666C61677B6C30675F346E346C797A33725F6733336B7D
```
Pasado por Cyberchef nos da la flag:

```bash
users,flagid,flag1flag{l0g_4n4lyz3r_g33k}
```
Pero el sistema no la da por buena. Se prueban estas:
**_flag{l0g_4n4lyz3r_g33k}_**
flag{l0g 4n4lyz3r g33k}
flag{log_analyzer_geek}

La flag final era **_flag{log_analyzer_g33k}_**. Desconocemos el motivo del cambio de la salida inicial.

---
## **Reto 27**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Hoy tenemos un examen de matemáticas, concretamente del temario de criptografía y codificación de mensajes. El examen consiste en descifrar el mensaje oculto.
>
>Pregunta:
>¿Serás capaz de aprobar?
>
>**Datos proporcionados:**
>
>Fichero de texto

Descargamos el fichero reto27.txt y vemos el contenido:

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/6 semana/reto27]
└─$ cat reto27.txt 
Vxoskx tobkr jk iolxgju_OPACQ3XGTHYCM2JVLWWM65JYT4WM42RCSBCIG3RHUTVW====KA2ZYPPCMKYZKSHLM4FYQTZMKA3MMPPCSEYZKSHLM4EYQTFBKA3JQPPCMWYZSSPLMOEIQTFBKA3MQPPCSEYZQFW=KA3JSPPCSSYZSSPLME3YQT3IKA2JUPPAMSYZOTFLMWFYQTHZKA2JIPPAMKYZOSPLMW3YQTHXKA2JMPPBMWYZQTHLMA2IQTHZKA2ZOPPBMWYZOTFLMWFYQTPAKA2JIPPAMSYZOSPLMWFYQTHZKA2JUPPAMKYZOSPLMA2IQTPAKA2JMPPAMKYZQTHLMA2IQTPAKA2JM===KA3AO===
```
Podemos observar un mensaje codificado. En los primeros caracteres aparecen espacios en blanco lo que nos puede inducir a pensar que son palabras y que pueden estar cifradas con el algoritmo del Cesar. Intentamos descifrar toda la cadena con tdas las posibles claves y con la clave igual a 6 obtenemos el siguiente texto: (https://cryptii.com/pipes/caesarcipher)

```bash
Primer nivel de
cifrado_IJUWK3RANBSWG2DPFQQG65DSN4QG42LWMVWCA3LBONPQ====EU2TSJJWGESTEM
BFG4ZSKNTGEU3GGJJWMYSTEMBFG4YSKNZVEU3DKJJWGQSTMMJFGIYCKNZVEU3GKJJWMYST
KZQ=EU3DMJJWMMSTMMJFGY3SKN3CEU2DOJJUGMSTINZFGQZSKNBTEU2DCJJUGESTIMJFGQ
3SKNBREU2DGJJVGQSTKNBFGU2CKNBTEU2TIJJVGQSTINZFGQZSKNJUEU2DCJJUGMSTIMJF
GQZSKNBTEU2DOJJUGESTIMJFGU2CKNJUEU2DGJJUGESTKNBFGU2CKNJUEU2DG===EU3UI=
==
```

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto27-1.png)

En la cadena resultante vemos unos primeros caracteres que nos muestra la frase “Primer nivel de cifrado_” loo que nos induce a pensar que los siguientes caracteres están cifrados/codificados con otro algoritmo. Por el formato parece base32 o base64, si decodificamos la cadena en base32 obtenemos el siguiente resultado:

```bash
┌──(root@kali)-[~/]
└─# base32 -d base32_data.txt > base32_decoded.txt
┌──(root@kali)-[~/]
└─# cat base32_decoded.txt
Bien hecho, otro nivel
mas_%59%61%20%73%6f%6c%6f%20%71%75%65%64%61%20%75%6e%6f%5f%66%6c%61%67
%7b%47%43%47%43%43%41%41%41%47%41%43%54%54%54%43%54%54%47%43%54%41%43%
41%43%43%47%41%41%54%54%43%41%54%54%54%43%7D
```
Obtenemos la cadena en claro “Bien hecho, otro nivel más”. El resto de la cadena parece estar codificado con URLencode, por lo que aplicando el algoritmo de descifrado obtenemos (https://www.urldecoder.org/):

```bash
Ya solo queda uno_flag{GCGCCAAAGACTTTCTTGCTACACCGAATTCATTTC}
```
Como indica el mensaje, parece que el contenido de la flag es “*GCGCCAAAGACTTTCTTGCTACACCGAATTCATTTC*”.

Si analizamos la cadena de caracteres está formada por las siguientes letras: “GCAT”, que coincide con las letras de las proteínas que forman el ADN (G:Guanina, C: Citosina, A:Adenina y T:Timina), por lo que podemos deducir que está cifrado con DNA Cypher. Con el siguiente script intentams descifrar el contenido:

```bash
┌──(root@kali)-[~/]
└─# cat dnadecode.py
mapping = {
'AAA':'a',
'AAC':'b',
'AAG':'c',
'AAT':'d',
'ACA':'e',
'ACC':'f',
'ACG':'g',
'ACT':'h',
'AGA':'i',
'AGC':'j',
'AGG':'k',
'AGT':'l',
'ATA':'m',
'ATC':'n',
'ATG':'o',
'ATT':'p',
'CAA':'q',
'CAC':'r',
'CAG':'s',
'CAT':'t',
'CCA':'u',
'CCC':'v',
'CCG':'w',
'CCT':'x',
'CGA':'y',
'CGC':'z',
'CGG':'A',
'CGT':'B',
'CTA':'C',
'CTC':'D',
'CTG':'E',
'CTT':'F',
'GAA':'G',
'GAC':'H',
'GAG':'I',
'GAT':'J',
'GCA':'K',
'GCC':'L',
'GCG':'M',
'GCT':'N',
'GGA':'O',
'GGC':'P',
'GGG':'Q',
'GGT':'R',
'GTA':'S',
'GTC':'T',
'GTG':'U',
'GTT':'V',
'TAA':'W',
'TAC':'X',
'TAG':'Y',
'TAT':'Z',
'TCA':'1',
'TCC':'2',
'TCG':'3',
'TCT':'4',
'TGA':'5',
'TGC':'6',
'TGG':'7',
'TGT':'8',
'TTA':'9',
'TTC':'0',
'TTG':' ',
'TTT':'.'
}

string = 'GCGCCAAAGACTTTCTTGCTACACCGAATTCATTTC'
def decode_dna( string ):
    pieces = []
    for i in range( 0, len(string), 3 ):
        piece = string[i:i+3]
        # pieces.append()
        pieces.append( mapping[piece] )
    return "".join(pieces)
print decode_dna(string)

┌──(root@kali)-[~/]
└─# python2 dnacode.py
Much0 Crypt0
```
Con este texto reconstruimos la flag:
**_flag{Much0 Crypt0}_**

---
## **Reto 28**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>El equipo del profesor de tecnología ha sido cifrado y no tiene acceso a sus datos. Tenemos el contenido de la memoria y el disco cifrado.
>
>Pregunta:
>¿Podríamos ayudarle a recuperar los datos?
>
>**Datos proporcionados:**
>
>Fichero comprimido en formato "rar" que contiene un fichero de volcado de memoria en formato ".raw" y otro ".vmdk"

1. Revisamos la imagen para ver que podemos extraer:

Revisando con la herramienta “passware kit Forensic” recuperamos la contraseña con la que esta encriptada, via BitLocker.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto28-1.png)

Esa contraseña la guardamos para poder desencriptar la imagen y ver que hay dentro:

BitLocker Master Key: **UW/1w6QYbMx5LV0/EDNa7i20zfXENrTBoby4Pz+nmLs=**

Recovery key:** 425777-567578-377586-013365-658427-126456-641872-309683**

2.  Ahora probaremos una utilidad para abrir imágenes:

Esta utilidad permite abrir imágenes encriptadas con BitLocker si tenemos la contraseña con las que se han firmado.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto28-2.png)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto28-3.png)

Abrimos ese archivo secret.txt

Obtenemos la flag:
**_flag{b1tl0ck3r_4cc3ss}_**

---
## **Reto 29**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Los datos del equipo del director han vuelto a ser robados, el método ha sido por DNS. El atacante ha intentado que estos datos no sean descubiertos y ha ofuscado todo el proceso.
>
>Pregunta:
>¿Podrías ayudarnos a conseguir los datos exfiltrados?
>
>**Datos proporcionados:**
>
>Fichero de log descargable

Descargamos el log y lo analizamos. Comprobamos que existen múltiples peticiones a subdominios de getdata.io con valores que parecen hexadecimales.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-1.png)

Si filtramos y nos quedamos solo con las peticiones a getdata.io, comprobamos que todos los subdominios solicitados son cadenas de caracteres que parecen estar codificados en base64:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-2.png)

Si decodificamos línea por línea de forma individual vemos que en la línea 29 tenemos el principio de un vector de números. El siguiente código en bash nos permite realizar esta operación:

```bash
#!/bin/bash
num=1
cat base64_data.txt | while read line
do
     echo $line > ./temp.txt
     echo $num
     base64 -d ./temp.txt
     num=$((num + 1))
done
```

Obteniendo como resultado:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-3.png)

Si unimos las líneas desde la 29 al final y decodificamos tenemos el siguiente vector de número enteros:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-4.png)

Analizando el vector de enteros los números van desde el 0 al 27, y teniendo en cuenta que en el log tenemos 32 líneas, podemos deducir que las últimas 4 se corresponden con este vector y las demás líneas a los datos exfiltrados.

El siguiente paso es ordenar las peticiones según el vector, de tal forma que el primer bloque de datos se encuentra en la línea 19, el segundo en la línea 4 y así sucesivamente. Con el siguiente código podemos ordenarlo para obtener el base64 final:

```bash
orden = [15,27,21,17,8,24,12,25,20,18,9,22,4,0,16,5,11,23,10,14,26,19,3,6,7,1,13,2]
b64list = open("./base64_data.txt","r").readlines()
base64_final = ""
for x in range(len(orden)):
     index = orden.index(x)
     base64_final += b64list[index].replace("\n","")
print base64_final
```
De esta forma obtenemos el siguiente bloque de datos:

```bash
root@kali:~# python base64_ordenar.py
UEsDBBQAAAAIAO9kWlK3tRNAYgEAAHcHAAAHABwAbG9nLnR4dFVUCQAD8d04YPndOGB1eAsAAQQAAAAABAAAAA
C9k0tPwjAAx+98it4JMHRBIeEwtsEgJO7hADUe5ihd92hr27mxTy/xVjhaPTXpob/+X6OSIkyGLGMgjtxwBjil
EgyAb0XR/il0ZmBtmFV2wsnl0rJtN4pAFP+cy3g77L057iJevQM/EaKh/AggSfmZSXgEDZYZCG1z2OuNrinJsc
JEwSxKl5S6MRIKVYxtmGbeh3opqL7GeC5CEzSfa8VgcqIKxSmattw86qVcklEhrjkpRk5HA6NeoQPRCqvO4rO8
0hRPC7/LJXIN2zP0aqsF5GodCmP6Fw5igoXkiaQqbr0LzNx/nt43mqtBeZKWUJUWB1k26lq6X+tlnSS78vClLf
peyyrNIIbVTZXBOH/VnBWrGYP/sN2ECPxxk5AxzvoPcdWJ5cHqb60oPcog5GkrxCYTej8A07vBTf2twkLlZWza
+/iVIJ4Q1VffDRr9vnY1hze6vF2AitrRvzOF8puXvwFQSwECHgMUAAAACADvZFpSt7UTQGIBAAB3BwAABwAYAA
AAAAABAAAApIEAAAAAbG9nLnR4dFVUBQAD8d04YHV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE0AAACjAQAA
AAA=
```
Descifrando el contenido en un fichero comprobamos que tenemos un fichero “.zip”:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-5.png)

A continuación, descomprimimos el “.zip” y obtenemos un fichero llamado “log.txt” con el siguiente contenido:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto29-6.png)

Analizando los datos vemos que se trata de un registro de accesos donde se guarda la contraseña cifrada en RC4. A continuación vamos a realizar una fuerza bruta sobre una de las contraseñas para intentar averiguar la clave de cifrado. Utilizaremos la función rc4.php del repositorio [https://github.com/cotdp/php-rc4.](https://github.com/cotdp/php-rc4.)

De todas las “contraseñas” cifradas nos fijamos en la que parece tener mayor longitud: “CU01h+7UmzsFXA+LAScdtQRrcxssJhs=” y filtramos los resultados que contienen la palabra flag:

```php
root@kali:~# cat bf_rc4.php
<?php
error_reporting(0);
require_once("./rc4.php");
$ciphertext = "CU01h+7UmzsFXA+LAScdtQRrcxssJhs=";
echo "Start date: ".date("Y M d H:i")."\n";
$fp = fopen("rockyou.txt", "r");
while (!feof($fp)){
     $linea = str_replace("\n","",fgets($fp));
     $data = "";
     try{
        $data = rc4($linea,base64_decode($ciphertext));
     }
     catch (DivisionByZeroError $e){
         continue;
     }
     $valid = strstr($data,"flag");
     if ($valid){
         echo "Clave: ".$linea." - Datos: ".$data;
     }
     $data="";
}
fclose($fp);
?>

root@kali:~/# php bf_rc4.php
Clave: 014789632587410014789632587410014789632587410014789632587410 - Datos: 
flag{DNS_3xf1ltr4t10n}
```

Obtenemos la flag:
***flag{DNS_3xf1ltr4t10n}***

---
## **Reto 30**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>El profesor de historia ha sido engañado y le han robado datos de su carpeta personal. Hemos capturado el tráfico de red durante el ataque.
>
>Pregunta:
>
>¿Podrás analizar y encontrar qué datos han sido robados?
>
>**Datos proporcionados:**
>
>Fichero pcap descargable

1. **Arrancamos wireshark para ver que contiene:**
![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto30-1.png)

Hay que extraer ese archivo EXE con nombre CruceroGratis.exe:

a. Revisamos que se trata de un binario de windows, podriamos probar a ver si esta hecho con .Net.

b. Buscamos utilidades que nos puedan decompilar este tipo de ejecutables.

2.  Probamos la utilidad dotPeek que permite decompilar archivos EXE creados con .NET.
    
[https://www.jetbrains.com/decompiler/](https://www.jetbrains.com/decompiler/)

Lo ejecutamos y abrimos el archivo EXE:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto30-2.png)

Podemos ver el codigo y se detalla como utiliza una clave para encriptar el mensaje que viene de un GET por HTTP.

1.- Buscamos en el PCAP que nos han dado en el reto para ver si aparece un dato asi por GET.

2.- Exportamos el exe decompilado para poder abrirlo como proyecto en Visual Studio.

3.  Lo montamos todo en Visual Studio.

Captura PCAP:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto30-3.png)

*o0ylbT4B146ILznhUFqBBkv9Cq+8VtR9Svr4Ux7Cnsg=*

En Visual Studio arrancamos el archivo “sln” que nos ha generado la exportación:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto30-4.png)

Cuando lo abrimos en VisualStudio vemos que no lo ejecuta bien si no tienes todo el pack instalado de VS, por lo que simplificamos el codigo inicial para que nos deje compilar de nuevo:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto30-5.png)

```bash
private static void Main(string[] args)
       {
            byte[] key = Program.GetKey("KHx4V2LSBsFKtAk8");
            ICryptoTransform decryptor = Aes.Create().CreateDecryptor(key, key);
            byte[] encrypted = Convert.FromBase64String("o0ylbT4B146ILznhUFqBBkv9Cq+8VtR9Svr4Ux7Cnsg=");
            string base64String = Convert.ToBase64String(decryptor.TransformFinalBlock(encrypted, 0, encrypted.Length));
            Console.WriteLine(base64String);
        }
		  }
```

Basicamente ese codigo se compila y volvemos a tener el EXE preparado para que extraiga la flag, pero SALE en BASE64.

```bash
c:\temp>CruceroGratis.exe
ZmxhZ3tQT1BfU01UUF80bjRsMXMxc19PS30=
```

Lo decodificamos y tenemos la flag.
Flag = **_flag{POP_SMTP_4n4l1s1s_OK}_**
