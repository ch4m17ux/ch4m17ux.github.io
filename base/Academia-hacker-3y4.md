# Academia Hacker Incibe - #writeUp - 3 y 4 semana

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---

## **Reto 11**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Después de conseguir sacar la contraseña del usuario bill, la profesora os felicita y os reenvía otro mensaje de antiguos alumnos que actualmente trabajan en el mundo de la ciberseguridad.
>
>Está segura de que todo el COLEGIO está muy contento con el trabajo de estos exalumnos.
>
>Pregunta:
>¿Qué mensaje enviaron estos antiguos alumnos?
>
>**Datos proporcionados:**
>
>Fichero imagen.

Se nos entrega una imagen con unos cuadrados y unos puntos, debemos tratar de descifrar lo que alli se muestra. Investigando encontramos que es un cifrado RosiCrucian.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto11.png)

Podemos hacer uso del sitio web: [www.dcode.fr](http://www.dcode.fr) y desde alli decodificar el mensaje. Al hacerlo obtenemos las letras:

NOQPGOSUZZWKFONIXRUACUGLPALOP

Un mensaje sin sentido, pero al ver la nota que nos han dejado, observamos que hay una palabra que resalta: **COLEGIO**

Asi que debemos usar esa palabra de alguna forma para poder descifrar el mensaje. Haciendo un poco de Brainstorming, encontramos que si utilizamos vigenere lo tenemos en claro.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto11-1.png)

Y obtenemos la flag que nos estan pidiendo:
***flag{LOSEXALUMNOSOSSALUDAN}***

---

## **Reto 12**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Te ha llegado un correo con el asunto "Codificación de mensajes en ficheros de audio". Te aseguran que en el fichero adjunto hay un mensaje. Al abrirlo hay un sonido muy extraño y te pitan los oídos.
>
>Estimado Alumno:
>
>El arte de esconder mensajes en múltiples formatos de fichero no es nuevo. La información está ahí, aunque no se vea ni se escuche. Para poder ganarte el primer premio de nuestro concurso anual, necesitamos conocer la flag. Como premio, recibirás algunos puntos.
>
>Pregunta:
>¿Serás capaz de decodificar la señal de audio?
>
>**Datos proporcionados:**
>
>Fichero de audio.

Se nos entrega un fichero de audio, que al revisarlo nos parece que son tonos DTMF. Este reto tiene varias posibilidades de resolucion, asi que aqui encontramos una de las tantas. (este write-up esta basado en: [http://g4ngli0s.logdown.com/posts/1422073-bsidessfctf-for-latlong](http://g4ngli0s.logdown.com/posts/1422073-bsidessfctf-for-latlong) y [https://github.com/bootplug/writeups/blob/master/2020/zh3r0-CTF/writeups.md#void)](https://github.com/bootplug/writeups/blob/master/2020/zh3r0-CTF/writeups.md#void))

Primero debemos instalar el paquete de Linux que nos permita Demodular la señal, este paquete segun la guia se denomina 'multimon-ng'.

```console
# sudo apt-get install libpulse-dev multimon-ng
````
  
Una vez que tenemos el paquete y las dependencias instaladas, procedemos a demodular la señal.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto12.png)

Obtenemos la flag:
***flag{intercepted_communication}***

---

## **Reto 13**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En una de las clases de informática a las que asistes te asignan la tarea de mirar el código de un fichero html que formará parte del aplicativo que están desarrollando otros compañeros. Revísalo y confirma las dudas que tiene el profesor.
>
>¿Cuál es la contraseña de acceso? El código parece ofuscado.
>
>**Datos proporcionados:**
>
>Fichero html

Nos entregan un fichero HTML que al ejecutarlo, nos solicita una contraseña. Colocamos cualquier calor y nos devuelve un mensaje de error.

Al analizar el codigo vemos que hay un JavaScript ofuscado, tratamos de desofuscarlo para ver mas claro, nos encontramos con que los nombre de las variables y los valores se han sustituido por codigo hexadecimal.

Hacemos algunos ajustes reemplazando el nombre de algunas variables para visualizarlo mejor y podriamos obtener el codigo siguiente:

```html
<script
  src="https://code.jquery.com/jquery-2.2.4.min.js"
  integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
  crossorigin="anonymous"></script>
  
  <script>
  var Cadena=['Incorrect\x20password','OK\x20,\x20flag{password}','1414812FnzZML','2ZuZoOq','720827WQlMog','password','granted1337','25459OvNsVk','1359268dQuzsW','647302iqoESf','getElementById','1407845XbPGsA','access','1163212MgQrRV','value','5eMgJYX'];
  var Valor_1=function(Valor_4,Valor_5){
    Valor_4=Valor_4-0x14a;
    var Valor_6=Cadena[Valor_4];
    return Valor_6;};
    
    alert(Valor_2(0x14b)+Valor_3)

    (function(_0x1d7e2f,_0x1e9b0f){
        var Valor_8=Valor_1;
        while(!![]){
            try{
                var Valor_7=parseInt(Valor_8(0x14e))*parseInt(Valor_8(0x156))+-parseInt(Valor_8(0x153))+-parseInt(Valor_8(0x14c))+-parseInt(Valor_8(0x151))+parseInt(Valor_8(0x152))*parseInt(Valor_8(0x158))+parseInt(Valor_8(0x157))+parseInt(Valor_8(0x14a));
                if(Valor_7===_0x1e9b0f)break;
                else _0x1d7e2f['push'](
                    _0x1d7e2f['shift']());
                }
                catch(_0x192125){
                    _0x1d7e2f['push'](_0x1d7e2f['shift']());}}}(Cadena,0xd9531));
                    function verify(){
                        var Valor_2=Valor_1;
                        password=document[Valor_2(0x159)](Valor_2(0x154))[Valor_2(0x14d)];
                        var Valor_3=Valor_2(0x155);
        password==Valor_2(0x14b)+Valor_3?alert(Valor_2(0x150)):alert(Valor_2(0x14f));}
    </script>
  <form>
    <label>Clave</label>
    <input type="password" name="password" id="password" placeholder="Clave" class="form-control" />
    <input type="submit" value="Login" class="form-control btn btn-success formulario" onclick="javascript:verify();"/>
</form>
		<div id="tagreply"></div>
```
  
Llama la atencion la parte del codigo que pone:

```bash
password==Valor_2(0x14b)+Valor_3?alert(Valor_2(0x150)):alert(Valor_2(0x14f));
```
  
Lo que indica en esa instruccion es que si el valor de la variable "password" es igual al valor de la variable "**Valor_2(0x14b)+Valor_3**" entonces muestra una ventana emergente, y en caso de que no sean iguales muestra otra ventana emergente.

Suponemos en este punto que es aqui donde compara que el valor que nosotros ponemos en el campo de Login sea el correcto. Pero el asunto es ¿Cómo saca ese valor?

Lo que se le ocurrio a DanyData es hacer un print, tambien lo podemos hacer con un alert para que salte el valor que espera justo encima de la linea donde compara y obtendriamos lo que debemos introducir. Seria algo como esto:

```html
alert(Valor_2(0x14b)+Valor_3);
password==Valor_2(0x14b)+Valor_3?alert(Valor_2(0x150)):alert(Valor_2(0x14f));}
```

Guardamos estos cambios y lo ejecutamos de nuevo, damos clic en el login y nos muestra la ventana emergente que hemos querido poner, donde se muestra el valor que espera: "accessgranted1337". Si digitamos esto en el campo login, y volvemos a validar nos muestra otra ventana que pone: "**OK, flag{password}**"

Lo que nos indica que nuestra flag es justamente el password que hemos puesto:
***flag{accessgranted1337}***

---

## **Reto 14**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En el laboratorio de ciencia la profesora de matemáticas ha incluido las ecuaciones lineales como tema para el examen. Pero esta vez vuestra nota se deducirá destripando un programa que ella misma ha compilado. Si lo resuelves obtendrás el 10 de la nota.
>
>¿Cuál es la solución a tantas ecuaciones lineales?
>
>**Datos proporcionados:**
>
>Fichero binario

1. Arrancamos IDA Pro para ver como funciona el binario y empezar a investigar:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto14.png)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto14-1.png)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto14-2.png)

En la función de inicio vemos que el serial tiene 21 caracteres.

Cada una de estas funciones tiene su código:
(En IDA con F5 vemos el codigo en formato mas legible. (OJO solo se ve cuando no esta prótegido el codigo)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto14-3.png)

2.  Recopilamos todas las ecuaciones que vemos dentro de cada una de las comprobaciones:
    
```bash
11189 = (a1[11] * a1[9] - a1[8]);
13471 = (a1[15] * a1[4] - a1[13]);
11161 = (a1[10] * a1[13] + a1[19] - a1[5]);
-12533 = (a1[4] - a1[2] * a1[10] + a1[6]);
1560780= (a1[4] * a1[15] * a1[6]);
-13113 = (a1[10] - a1[11] * a1[7]);
-70061566 = (*a1 - a1[1] * a1[20] * a1[7] * a1[6]);
66767976 = (a1[11] * a1[19] * a1[9] * a1[15]);
-10897 = (a1[3] + a1[17] - *a1 * a1[16]);
10996 = (a1[16] * a1[12] + a1[20] - a1[12])
13338 = (a1[7] * a1[11] + a1[12]);
97 = (a1 - a1[15] + a1[14]);
119 = (a1[12] + a1[4] - a1[3]);
5763 = (a1[19] + a1[19] * a1[3]);
11665 = (a1[18] + a1[2] * a1[5]);
5203 = (a1[20] * a1[1] - a1[17]);
113 = (a1[5] + a1[3] - a1[18] - a1[18]);
5751 = (a1[5] - a1[18] + a1[18] * a1[12]);
11701 = (a1[1] * a1[4] - a1[15]);
625517 = (a1[3] * a1[17] * a1[12] - a1[2]);
283 = (a1[2] + a1[20] + a1[7]);
```

3.  No se aprecia posibilidad alguna de realizar una comparacion entre ecuaciones para usar un sistema, asi que contruimos un pequeño script que ayude a validar posibles datos y a partir de ahí usar aproximaciones.

```bash
#!/bin/bash
valorfinal=13113
for ((v1 = 48; v1 <= 123; v1++)); do
    for ((v2 = 48; v2 <= 123; v2++)); do 
        for ((v3 = 48; v3 <= 123; v3++)); do
            let ecuacion=$((v1-(v2*v3)))
            # echo $total
            if [ $ecuacion = $valorfinal ]; then

                echo "$v1"
                echo "$v2"
                echo "$v3"

            fi
        done
    done
done
```

De este script debemos cambiar el valorfinal y ecuacion cada vez que queramos probar una de las ecuaciones anteriores.

Con esto que ganamos:

El script nos extrae por pantalla los posibles valores que pueden coger las variables. En cada caso nos aparecen más de una posibilidad. Las debemos anotar (Recomiendo EXCEL) para un uso posterior en otras ecuaciones. De esta forma iremos conociendo los valores reales de cada variable (Recordamos que són 20).

Ejemplo:

El script, hace referencia a la ecuación: 13113 = (a1[10] - a1[11] * a1[7]);

Este script nos dará por pantalla valores de 3 en 3 correspondientes a las variables num10, num11 y num7.

Hay que tener suerte de escoger la ecuación que mejor se adapte y menos valores de salida te dé, de esa forma se podrán reutilizar las variables que ya hemos encontrado y después reutilizarlas.

4.  Uso de terceros programas para ir anotando los valores de las variables e ir rellenando las variables que necesitamos….

(NI QUE DECIR TIENE QUE LO MEJOR ES ACABAR EL SCRIPT COMO DIOS MANDA Y QUE LO HAGA TODO EL SCRIPT – Opcion A Mejorar)

Yo lo anoté poco a poco y fui rellenando valores de variables probando con el script primario que hice.

```bash
Ejemplos:

              51      116
66767976 = (a1[11] * a1[19] * a1[9] * a1[15]);

            101            112
113 = (a1[5] + a1[3] - a1[18] - a1[18]);

           109       101       51
11161 = (a1[10] * a1[13] + a1[19] - a1[5]);

          117        115     109    115
12533 = (a1[4] - a1[2] * a1[10] + a1[6]);

          114      116
97 = (a1 - a1[15] + a1[14]);

             112       49       97
10897 = (a1[3] + a1[17] - *a1 * a1[16]);

              97      114      52     114
10996 = (a1[16] * a1[12] + a1[20] - a1[12]);

            106        114
13338 = (a1[7] * a1[11] + a1[12]);

           52       101     49
5203 = (a1[20] * a1[1] - a1[17]);
```

5.  Una vez que tenemos varios de esos valores de valirables vamos rellenando el valor final del serial.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto14-4.png)

Y pasarlos a formato ASCII sabiendo el char() correspondiente.

a1 = 114 r
[1] = 101 e
[2] = 115 s
[3] = 112 p
[4] = 117 u
[5] = 101 e
[6] = 115 s
[7] =
[8] =
[9] =
[10] = 111 o
[11] =
[12] = 114 r
[13] = 101 e
[14] = 99 c
[15] = 116 t
[16] = 97 a
[17] = 49 1
[18] = 50 2
[19] = 51 3
[20] = 52 4

No espero a tenerlos todos, pero pruebo con un poco de guessing:
***flag{respuestacorrecta1234}***


## Solucion 2

Se ha entregado un script con el cual sacar la solucion de forma inmediata.

```python
#!/usr/bin/env python3
from z3 import *
import binascii
import sys

clave = []
s = Solver()
for i in range(21):
    clave.append(Int(str(i)))
    s.add(Or(And(clave[i] >= 48, clave[i] <= 57), And(
        clave[i] >= 65, clave[i] <= 90), And(clave[i] >= 97, clave[i] <= 125)))

s.add(clave[11] * clave[9] - clave[8] == 11189)
s.add(clave[15] * clave[4] - clave[13] == 13471)
s.add(clave[10] * clave[13] + clave[19] - clave[5] == 11161)
s.add(clave[4] - clave[2] * clave[10] + clave[6] == -12533)
s.add(clave[4] * clave[15] * clave[6] == 1560780)
s.add(clave[10] - clave[11] * clave[7] == -13113)
s.add(clave[0] - clave[1] * clave[20] * clave[7] * clave[6] == -70061566)
s.add(clave[11] * clave[19] * clave[9] * clave[15] == 66767976)
s.add(clave[3] + clave[17] - clave[0] * clave[16] == -10897)
s.add(clave[16] * clave[12] + clave[20] - clave[12] == 10996)
s.add(clave[7] * clave[11] + clave[12] == 13338)
s.add(clave[0] - clave[15] + clave[14] == 97)
s.add(clave[12] + clave[4] - clave[3] == 119)
s.add(clave[19] + clave[19] * clave[3] == 5763)
s.add(clave[18] + clave[2] * clave[5] == 11665)
s.add(clave[20] * clave[1] - clave[17] == 5203)
s.add(clave[5] + clave[3] - clave[18] - clave[18] == 113)
s.add(clave[5] - clave[18] + clave[18] * clave[12] == 5751)
s.add(clave[1] * clave[4] - clave[15] == 11701)
s.add(clave[3] * clave[17] * clave[12] - clave[2] == 625517)
s.add(clave[2] + clave[20] + clave[7] == 283)

s.check()
m = s.model()

sys.stdout.write("solucion: ")

total = ([m[n].as_long() for n in clave])

for d in range(21):
    sys.stdout.write(chr(int(str(total[d]))))
sys.stdout.write('\n')
sys.stdout.flush()
```

Obtenemos la flag:
***flag{respuestacorrecta1234}***

---

## **Reto 15**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Una de las salidas que realizáis en el instituto es fuera de la gran ciudad, al campo. En esas salidas pernoctáis en un albergue y si el tiempo acompaña, soléis escuchar al anciano del lugar rememorar algunas historias del pueblo.
>
>El anciano saca una radio y reproduce en una cinta magnética de audio unos sonidos que según dice él, los grabó años atrás. Esto empieza a parecerse a "Stranger Things(tm)"!
>
>¿Podrías desvelar al anciano el mensaje que esconde la cinta?
>
>**Datos proporcionados:**
>
>Fichero wav

Se nos entrega un audio que debemos analizar. Por lo que hacemos una verificacion con _file_ y _exiftool_

Hemos seguido la guia que se especifica en:

[https://ourcodeworld.co/articulos/leer/956/como-convertir-decodificar-un-archivo-de-audio-de-transmisiones-de-television-de-escaneo-lento-sstv-en-imagenes-usando-qsstv-en-ubuntu-1804](https://ourcodeworld.co/articulos/leer/956/como-convertir-decodificar-un-archivo-de-audio-de-transmisiones-de-television-de-escaneo-lento-sstv-en-imagenes-usando-qsstv-en-ubuntu-1804) y [https://www.chonky.net/hamradio/decoding-sstv-from-a-file-on-a-linux-system](https://www.chonky.net/hamradio/decoding-sstv-from-a-file-on-a-linux-system)

Obtenemos la flag:
***flag{4458256}***

---

## **Reto 16**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>En próximos días vais a participar en una de las salidas anuales del instituto. Os llega al correo la información de la salida junto a una imagen adjunta. Como sois curiosos, decidís mirar si hay metadatos en la imagen.
>
>**Datos proporcionados:**
>
>Fichero jpg.

Nos han entregado un fichero jpg, asi que verificamos por ejemplo que sea el tipo de fichero que se supone deberia ser.

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto16]
└─$ file marsperse.jpeg
marsperse.jpeg: JPEG image data, JFIF standard 1.02, aspect ratio, density 100x100, segment length 16, comment: "perseverance", baseline, precision 8, 1200x675, components 3
```
Verificamos si tenemos algo en los metadatos:
```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto16]
└─$ exiftool marsperse.jpeg
ExifTool Version Number : 12.16
File Name : marsperse.jpeg
Directory : .
File Size : 96 KiB
File Modification Date/Time : 2021:02:19 12:31:15+01:00
File Access Date/Time : 2021:05:24 20:36:37+02:00
File Inode Change Date/Time : 2021:05:24 20:35:15+02:00
File Permissions : rwxr--r--
File Type : JPEG
File Type Extension : jpg
MIME Type : image/jpeg
JFIF Version : 1.02
Resolution Unit : None
X Resolution : 100
Y Resolution : 100
Comment : perseverance
Image Width : 1200
Image Height : 675
Encoding Process : Baseline DCT, Huffman coding
Bits Per Sample : 8
Color Components : 3
Y Cb Cr Sub Sampling : YCbCr4:2:0 (2 2)
Image Size : 1200x675
Megapixels : 0.810
```

Vemos una entrada "Comment" que nos llama la atencion, y que pone: perseverance.

Verificamos si podemos sacar algun dato de la imagen, lo hacemos a traves de **_steghide_** y utilizando la palabra que hemos encontrado en los metadatos.

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto16]
└─$ steghide --info marsperse.jpeg 1 ⨯
"marsperse.jpeg":
formato: jpeg
capacidad: 5,9 KB
Intenta informarse sobre los datos adjuntos? (s/n) s
Anotar salvoconducto:
archivo adjunto "flag.txt":
tamao: 186,0 Byte
encriptado: rijndael-128, cbc
compactado: si
```

Procedemos a extraerlo y veremos que informacion nos arroja.
```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto16]
└─$ steghide extract -sf marsperse.jpeg
Anotar salvoconducto:
anot los datos extrados e/"flag.txt".

┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto16]
└─$ cat flag.txt
Nos acaban de enviar los códigos para preparar la transmision. Cuando vayáis al albergue preguntar por el anciano del pueblo, os quiere decir algo.

flag{code_ready_for_transmission}
```

Obtenemos la flag solicitada:
***flag{code_ready_for_transmission}***

---

## **Reto 17**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Se ha recibido un correo electrónico con un documento de texto adjunto con unos caracteres indescifrables.
>
>Pregunta
>
>¿Puedes recuperar el mensaje original?
>
>**Datos proporcionados:**
>
>flag.txt

Nos entregan un fichero flag.txt, que si intentamos verlo, vemos que parece que contiene algunos iconos o imagenes.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto17-1.png)

En principio no nos da mayor informacion, asi que investigamos y encontramos que hay ejemplos (https://reese.dev/codemash2019-ctf-solutions/), y por ejemplo podemos usar un sitio donde podemos ver el codigo unicode de cada imagen. Donde copiamos los "caracteres" que nos entregan. (https://reese.dev/codemash2019-ctf-solutions/)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto17-2.png)

Tomando los valores "CodePoint" y descifrandolo desde hexadecimal, obtenemos la flag.

***flag{una_fuente_puede_ser_un_codificador}***

---

## **Reto 18**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Se ha implantado en el colegio un sistema para entrar a clase mediante lectura de un código QR.
>
>El profesor distribuye varios códigos QR para que los alumnos prueben sus teléfonos
>
>Pregunta
>¿Puedes leer el QR?
>
>**Datos proporcionados:**
>
>flag.txt

Nos entregan una imagen que es un QR Code:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto18-1.png)

Buscamos un sitio web que nos permita subir y leer el QR Code, o con el mismo movil podemos realizarlo. Utilizamos por ejemplo [https://zxing.org/w/decode.jspx](https://zxing.org/w/decode.jspx)

Al subir la imagen nos muestra la informacion que se "esconde" en el QR Code.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto18-2.png)

Obtenemos una secuencia de caracteres, asi que los copiamos y tratamos de verificar que tipo de cifrado se ha efectuado sobre el mismo.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto18-3.png)

Al realizar 11 veces que lo decodifique desde Base64, obtenemos la flag.

***flag{QR_puede_usarse_para_esconder_mensajes}***

---
## **Reto 19**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En clases de informática, el profesor está distribuyendo unos binarios que necesitan de una cadena mágica como parámetro para probar las habilidades de los alumnos.
>
>Pregunta
>
>¿Puedes encontrar la cadena mágica que devuelve la flag?
>
>**Datos proporcionados:**
>
>flag

Nos entregan un binario, que al ejecutarlo sin parámetros, nos pone que debemos escribir "una cadena mágica"

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto19]
└─$ ./flag
Introduce la cadena mágica como argumento
```

Pero si ponemos cualquier cosa, nos pone que esta incorrecto.

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto19]
└─$ ./flag loquesea
Lo siento, loquesea no es correcto
```

Así que debemos revisar el binario para tratar de identificar que espera como argumento. Revisando con IDA PRO (que lo podéis descargar [No promocionamos la piratería, pero para temas académicos, podemos pasarlo por alto] desde [https://web.telegram.org/#/im?p=@idapro7)](https://web.telegram.org/#/im?p=@idapro7))

Debugueando, encontramos que espera una cadena:
**_v7z7vw5rkcrsciwchmjmgmp_**

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto19-1.png)

Vemos que compara cada carácter introducido y le hace una rotación -4 caracteres. Así que probamos con algunos de los cifrados que conocemos con esta característica: Rot13 (cesar) o Rot47, y tratamos de descifrarlo.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto19-2.png)

Aplicando Rot47 y le colocamos -4, encontramos el argumento que espera, para que nos entregue la flag.

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto19]
└─$ ./flag r3v3rs1ng_no_es_dificil
flag{r3v3rs1ng_no_es_d1f1c1l}
```

---
## **Reto 20**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En clases de informática, el profesor está distribuyendo unos binarios que necesitan de una cadena mágica como parámetro para probar las habilidades de los alumnos.
>
>Pregunta
>
>¿Puedes encontrar la cadena mágica que devuelve la flag?
>
>**Datos proporcionados:**
>
>flag

Nos entregan un binario, que si lo ejecutamos solo (de nuevo) nos indica que debemos pasar "la cadena magica"

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto20]
└─$ ./flag-1 1 ⚙
Introduce la cadena mágica como argumento
```

Asi que nos toca hacer reversing, abriendo el IDA Pro, que os he dejado en la entrada anterior, podemos ver que espera una cadena bastante particular:
**_i{2ldio348zAm=Qnlfju3jaJ-avDI1!x_a_**

Si embargo, alli no acaba el asunto, tambien verifica que el nombre de tu ordenador coincida con la cadena que se especifica en el binario: **_C0p3rn1c0_**

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto20-1.png)

Podemos parchear el binario y cambiar esa cadena de hostname por el nuestro (no he logrado hacerlo en IDA, pero si en OllyDBG) o modificar temporalmente el nombre de tu maquina y lanzar el binario con la cadena que espera, para que nos de la flag que buscamos:

```bash
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto20]
└─$ sudo hostname C0p3rn1c0                                                 1 ⚙
                                                                                
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto20]
└─$ hostname                                                                1 ⚙
C0p3rn1c0
                                                                                
┌──(ch4m0㉿kali)-[~/Descargas/incibe/4 semana/reto20]
└─$ ./flag-1 'i{2ldio348zAm=Qnlfju3jaJ-avDI1!x_a'                       1 ⨯ 1 ⚙
Aquí tienes la flag:
flag{usando_variables_del_sistema}
```

obtenemos la flag solicitada:

***flag{usando_variables_del_sistema}***