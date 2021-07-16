
# Academia Hacker Incibe - #writeUp - 7 semana

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---

## **Reto 31**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>La profesora de literatura ha olvidado su contraseña y la necesita para poder subir las notas a la plataforma oficial. Tú has aprobado, pero hasta que no estén en la aplicación no será efectivo y es necesario tenerlas subidas antes de 1 semana.
>
>El personal de sistemas ha proporcionado un script para recuperarla, pero la profesora no recuerda la respuesta a la pregunta de recuperación.
>
>Pregunta:
>¿Podrías ayudarnos a recuperarla?
>
>**Datos proporcionados:**
>
>Script de python.

Nos dan un fichero python, que parece estar compilado de alguna forma.

A continuación, ejecutamos el script en la línea de comandos:

```bash
┌──(root@kali)-[~/]
└─# python3 reto31.py
Welcome to the password recovery tool.
What is your pet's name?
Dog
Comparing strings...
Wrong answer!:
TRY HARDER!
```
Como podemos observar nos solicita el nombre de la mascota para recuperar la contraseña. Si nos fijamos bien en el contenido del fichero parece código precompilado, por lo que vamos a intentar decompilarlo. Para ello utilizamos la herramienta [https://github.com/zrax/pycdc,](https://github.com/zrax/pycdc,) obteniendo el siguiente resultado:

```bash
┌──(root@kali)-[~/]
└─# ./pycdc reto31.py > reto31_decompiled.py
```
![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto31-1.png)

En la línea 34 tenemos la definición de la clase *`“sCRCDlpYibqMekCnUWAszaUKNQLKRZWYTqoGuKtdieZYbYpqawbvzctGoHiZKFNE”`*, que tiene dos parámetros: “`name`” y “`age`”, y además, tenemos la creación de un objeto de esta clase en la línea 53. De aquí podemos deducir que el nombre de la mascota es ‘*`Y29tb3R1`*’. 

Decodificamos el texto en base64 y obtenemos el nombre:
```bash
┌──(root@kali)-[~/]
└─# python3 -c "import base64;print
(base64.b64decode('Y29tb3R1').decode('ascii'))"
comotu
```
Por último, ejecutamos el script e introducimos el nombre de la mascota:

```bash
┌──(root@kali)-[~/]
└─# python3 reto31.py
Welcome to the password recovery tool.
What is your pet's name?
comotu
Comparing strings...
Congratulations! Right answer:
    comotu says flag{pyth0n_decompile_OK}
```

***flag{pyth0n_decompile_OK}***

---
## **Reto 32**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Como ejercicio final del módulo de forense, el profesor de informática ha propuesto la siguiente actividad: Descifrar el contenido del mensaje oculto en el fichero Mensaje.zip. Para ello tenemos una captura de tráfico y el propio fichero.
>
>Pregunta:
>¿Aprobarás este módulo?
>
>**Datos proporcionados:**
>
>Dos ficheros: Fichero pcap y fichero zip.

Descargamos los ficheros. Intentamos descomprimir el fichero Mensaje.zip pero nos solicita contraseña:
```bash
┌──(root@kali)-[~/]
└─# unzip Mensaje.zip
Archive: Mensaje.zip
[Mensaje.zip] Mensaje.pdf password:
password incorrect--reenter:
password incorrect--reenter:
skipping: Mensaje.pdf incorrect password
```
Analizando el pcap, vemos que predomina tráfico HTTP entre dos IPs concretas: *192.168.209.128* y *192.168.209.141*, en la que el primero es el servidor y el segundo es el cliente:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-1.png)

Si nos fijamoos en el paquete número **16** se hace una petición `POST` al recurso “/html/index.php” con parámetros `GET` que contiene lo que parece una sentencia SQL, aparecen palabras del tipo `SELECT` y `UNION`:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-2.png)

Si buscamos dentro del tráfico palabras típicas de consultas a bases de datos como SELECT, encontramos que existen muchos paquetes que contienen esa cadena, analizamos los de mayor tamaño para ver la respuesta:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-3.png)

Decodificamos el payload de la petición POST y obtenemos:

```bash
email=admin@admin.com'/**/UNION/**/ALL/**/SELECT/**/CONCAT(0x716b717a7
1,0x716b727770446663716e7571674d5642766a6645586d636145457072535778494a
4d63595a567854,0x717a7a6271),NULL,NULL/**/FROM/**/(SELECT/**/0/**/AS/*
*/dSyq/**/UNION/**/SELECT/**/1/**/UNION/**/SELECT/**/2/**/UNION/**/SEL
ECT/**/3/**/UNION/**/SELECT/**/4/**/UNION/**/SELECT/**/5/**/UNION/**/S
ELECT/**/6/**/UNION/**/SELECT/**/7/**/UNION/**/SELECT/**/8/**/UNION/**
/SELECT/**/9/**/UNION/**/SELECT/**/10/**/UNION/**/SELECT/**/11/**/UNIO
N/**/SELECT/**/12/**/UNION/**/SELECT/**/13/**/UNION/**/SELECT/**/14)/*
*/AS/**/iosi#&pass=wedfc
```
Vemos que en el cuerpo de la petición aparece un parámetro email cuyo valor contiene un intento de inyección SQL, por lo que podemos determinar que existe tráfico correspondiente a un ataque SQLi. Por la complejidad de la sentencia se puede deducir que ha sido realizada con una herramienta automática como puede ser sqlmap.

En este punto vamos a analizar las respuestas del servidor para ver si hay datos exfiltrados y qué contienen. Ordenamos los paquetes y nos vamos a analizar los últimos, ya que en un ataque con herramientas automáticas los datos son exfiltrados una vez comprobada la vulnerabilidad. En el último paquete vemos la siguiente información:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-4.png)

Parece un volcado de los datos de la tabla loginapp.usuarios. En el que, analizando la petición descubrimos que tiene tres columnas: ALG, user y password:

```bash
email=admin@admin.com'/**/UNION/**/ALL/**/SELECT/**/CONCAT(0x717671767
1,IFNULL(CAST(ALG/**/AS/**/NCHAR),0x20),0x667661736868,IFNULL(CAST(`us
er`/**/AS/**/NCHAR),0x20),0x667661736868,IFNULL(CAST(password/**/AS/**
/NCHAR),0x20),0x7178717a71),NULL,NULL/**/FROM/**/loginapp.usuarios#&pa
ss=wedfc
```
Como puede observarse la petición añade una serie de caracteres en hexadecimal delante y detrás de cada resultado, por lo que vamos a analizar dichas cadenas para poder obtener los resultados exactos:

```bash
┌──(root@kali)-[~/]
└─# python3
Python 3.9.1+ (default, Feb 5 2021, 13:46:56) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> bytes.fromhex('7176717671').decode('utf-8')
'qvqvq'
>>> bytes.fromhex('667661736868').decode('utf-8')
'fvashh'
>>> bytes.fromhex('7178717a71').decode('utf-8')
'qxqzq'
```
Quitando esas cadenas de la respuesta del servidor tenemos los siguientes datos:

```bash
MD5;ciencias@escuela.local;NmYzYWM5MjMzMmZiMGNiZjI2ODU1ZmYxNzFmYmI0NjI
=
MD5;history@escuela.local;MzM0OWIxZTE5MjMxMDU2MDEyYWFkZDQxZGNkNTVjNjI=
MD5;informatica@escuela.local;OGI1YmFiNDE3MDdhNzJlYzdiYzhiMjZkMmYyOGZm
MDQ=
MD5;literatura@escuela.local;OTgzZTgzMzYwYjQxZjE5NTM1ZTAzYWY1MjEwOTMwZ
TY=
MD5;matematicas@escuela.local;YWYxMmUyODk1NWY0N2VhZWIzZTQzYzhkZDJkMDI4
ZmI=
```
Una vez comprobada la dinámica, vamos a buscar mas tablas dentro del tráfico que nos puedan dar más información.

Si nos fijamos en los paquetes anteriores, concretamente en el número 3484, tenemos otra tabla llamada “documentos”, dónde analizando la respuesta como en la tabla anterior tenemos los siguientes datos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-5.png)

De estos datos podemos deducir que el fichero “Mensaje.zip” pertenece al profesor de literatura. Teniendo los datos de contraseñas del profesor de literatura vamos a intentar abrir el fichero “Mensaje.zip” con la contraseña de dicho profesor. Para ello, antes debemos descifrarla.

Por los datos de la tabla, la columna “ALG” debe indicar el algoritmo de cifrado ya que indica el algoritmo MD5 y por el formato parece ser base64. Decodificando en base64 nos da como resultado la siguiente cadena:

```bash
──(root@kali)-[~/]
└─# echo -n OTgzZTgzMzYwYjQxZjE5NTM1ZTAzYWY1MjEwOTMwZTY= | base64 -d
983e83360b41f19535e03af5210930e6
```
A continuación vamos a la web [https://md5online.es/](https://md5online.es/) e intentamos descifrar el md5:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-6.png)

Y nos da como resultad “*`xdH9UWhNF4XGkerK`*”. El siguiente paso es intentar extraer el documento con esta contraseña:

```bash
┌──(root@kali)-[~/]
└─# unzip Mensaje.zip 
Archive: Mensaje.zip
[Mensaje.zip] Mensaje.pdf password: 
 inflating: Mensaje.pdf
```
Abrimos el fichero Mensaje.pdf y obtenemos la flag:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto32-7.png)

---
## **Reto 33**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Hoy es el día de visita al museo. Estáis todos esperando a entrar.
>
>Te das cuenta de que la entrada al museo tiene un mensaje en el reverso "Descifra el mensaje.". Lo firma Mr.EnglishBreakFast.
>
>Pregunta:
>¿Qué mensaje ha transmitido Mr.EnglishBreakFast?
>
>**Datos proporcionados:**
>
>fichero txt.

El nombre de la tarea y también el hecho de que tengamos diferentes tipos de letra, hacen pensar en el cifrado del bacon. El primer paso obvio es decodificar el cifrado de bacon para el caso de diferentes tipos de letra. Si lo decodificamos en notación A (normal)/B (negrita) según la que se suele utilizar obtenemos lo siguiente:

```bash
AABBA
ABABB
ABAAA
BAABA
AABBB
AAAAB
AAAAA
AAABA
ABBBA
ABBAB
glishbacon
```
Esto parece una parte del texto plano. Pero, el texto también utiliza mayúsculas y minúsculas, que también es una forma conocida de codificar datos como cifrado bacon. Descodificando a partir de esta idea (minúsculas - A, mayúsculas - B), obtenemos lo siguiente:
```bash
AAABA
ABAAA
ABBAB
AAABA
ABBBA
BAABA
ABAAA
BAAAB
AABAA
ABBAB
cincosiren
```
Otra forma de codificar los datos en este tipo de cifrado se basa en la posición de la letra en el alfabeto. Si está en posiciones impares - A, si está en posiciones pares - B. La decodificación produce lo siguiente:
```bash
ABBAB
AABAA
ABABB
BAABB
AABAA
AAABB
AABAA
ABABB
AAAAA
BAABA
neltedelas
```
Para obtener la última parte, podemos utilizar de nuevo el cifrado basado en la posición de los caracteres. Si se trata de las primeras 13 letras - A, de lo contrario - B:
```bash
BBAAA
BAABB
AABAA
AABAA
BAABA
ABBBB
AABAA
BAAAB
ABBBA
AABAA
yteesperoe
```
Con estos cuatro pasos obtenemos la flag.
**yteesperoeneltedelascincosirenglishbacon**

>Tenemos otra posible solucion y es traves de un script de Python que automatice esta decodificacion. Que podeis encontrar en: https://github.com/ch4m17ux/Scripts/blob/main/decode_bacon.py

---
## **Reto 34**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Dentro del club de competiciones al que perteneces se intercambian retos con otros países. Desde la empresa ByteCode Alliance os han propuesto resolver el flujo de un programa escrito en C y compilado para web como con emcc.
>
>Demuestra a tu profesor que puedes resolver el reto y enviarlo para obtener la beca de desarrollo web.
>
>Pregunta:
>¿Qué mensaje se ha ocultado en la función getFlag?
>
>**Datos proporcionados:**
>
>Fichero WASM.

El participante se encuentra con un fichero compilado en C con emcc :
```bash
└─# file WASM.wasm
WASM.wasm: WebAssembly (wasm) binary module version 0x1 (MVP)
```
Se trata de un módulo preparado para ser incluido en un fichero js que cargue vía web. El fichero js o el html no está incluido. WebAssembly admite dos formatos, binario (el proprocionado) y texto. El participante deberá convertir el código al formato WAT ya que es el formato de texto que acepta WebAssembly.

Podemos convertirlo en [https://webassembly.github.io/wabt/demo/wasm2wat/](https://webassembly.github.io/wabt/demo/wasm2wat/)

```bash
(module
 (type $t0 (func (result i32)))
 (type $t1 (func (param i32)))
 (type $t2 (func (param i32) (result i32)))
 (type $t3 (func))
 (type $t4 (func (param i32 i32) (result i32)))
 (type $t5 (func (param i32 i32 i32) (result i32)))
 (type $t6 (func (param i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 
i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32) (result i32)))
 (type $t7 (func (param i32 i64 i32) (result i64)))
 (func $__wasm_call_ctors (export "__wasm_call_ctors") (type $t3)
 (call $emscripten_stack_init))
 (func $_Z7getFlagiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (export "_Z7getFlagiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") (type $t6) (param $p0 
i32) (param $p1 i32) (param $p2 i32) (param $p3 i32) (param $p4 i32) (param $p5 i32) (param $p6 i32) 
(param $p7 i32) (param $p8 i32) (param $p9 i32) (param $p10 i32) (param $p11 i32) (param $p12 i32) 
(param $p13 i32) (param $p14 i32) (param $p15 i32) (param $p16 i32) (param $p17 i32) (param $p18 i32) 
(param $p19 i32) (param $p20 i32) (param $p21 i32) (param $p22 i32) (param $p23 i32) (param $p24 i32) 
(param $p25 i32) (param $p26 i32) (param $p27 i32) (param $p28 i32) (param $p29 i32) (param $p30 i32) 
(param $p31 i32) (param $p32 i32) (param $p33 i32) (param $p34 i32) (param $p35 i32) (param $p36 i32) 
(param $p37 i32) (param $p38 i32) (param $p39 i32) (result i32)
 (local $l40 i32) (local $l41 i32) (local $l42 i32) (local $l43 i32) (local $l44 i32) (local $l45 i32) (local $l46 
i32) (local $l47 i32) (local $l48 i32) (local $l49 i32) (local $l50 i32) (local $l51 i32) (local $l52 i32) (local $l53 
i32) (local $l54 i32) (local $l55 i32) (local $l56 i32) (local $l57 i32) (local $l58 i32) (local $l59 i32) (local $l60 
i32) (local $l61 i32) (local $l62 i32) (local $l63 i32) (local $l64 i32) (local $l65 i32) (local $l66 i32) (local $l67 
i32) (local $l68 i32) (local $l69 i32) (local $l70 i32) (local $l71 i32) (local $l72 i32) (local $l73 i32) (local $l74 
i32) (local $l75 i32) (local $l76 i32) (local $l77 i32) (local $l78 i32) (local $l79 i32) (local $l80 i32) (local $l81 
i32) (local $l82 i32) (local $l83 i32) (local $l84 i32) (local $l85 i32) (local $l86 i32) (local $l87 i32) (local $l88 
i32) (local $l89 i32) (local $l90 i32) (local $l91 i32) (local $l92 i32) (local $l93 i32) (local $l94 i32) (local $l95 
i32) (local $l96 i32) (local $l97 i32) (local $l98 i32) (local $l99 i32) (local $l100 i32) (local $l101 i32) (local 
$l102 i32) (local $l103 i32) (local $l104 i32) (local $l105 i32) (local $l106 i32) (local $l107 i32) (local $l108 
i32) (local $l109 i32) (local $l110 i32) (local $l111 i32) (local $l112 i32) (local $l113 i32) (local $l114 i32) 
(local $l115 i32) (local $l116 i32) (local $l117 i32) (local $l118 i32) (local $l119 i32) (local $l120 i32) (local 
$l121 i32) (local $l122 i32) (local $l123 i32) (local $l124 i32) (local $l125 i32) (local $l126 i32) (local $l127 
i32) (local $l128 i32) (local $l129 i32) (local $l130 i32) (local $l131 i32) (local $l132 i32) (local $l133 i32) 
(local $l134 i32) (local $l135 i32) (local $l136 i32) (local $l137 i32) (local $l138 i32) (local $l139 i32) (local 
$l140 i32) (local $l141 i32) (local $l142 i32) (local $l143 i32) (local $l144 i32) (local $l145 i32) (local $l146 
i32) (local $l147 i32) (local $l148 i32) (local $l149 i32) (local $l150 i32) (local $l151 i32) (local $l152 i32) 
(local $l153 i32) (local $l154 i32) (local $l155 i32) (local $l156 i32) (local $l157 i32) (local $l158 i32) (local 
$l159 i32) (local $l160 i32) (local $l161 i32) (local $l162 i32) (local $l163 i32) (local $l164 i32) (local $l165 
i32) (local $l166 i32) (local $l167 i32) (local $l168 i32) (local $l169 i32) (local $l170 i32) (local $l171 i32) 
(local $l172 i32) (local $l173 i32) (local $l174 i32) (local $l175 i32) (local $l176 i32) (local $l177 i32) (local 
$l178 i32) (local $l179 i32) (local $l180 i32) (local $l181 i32) (local $l182 i32) (local $l183 i32) (local $l184 
i32) (local $l185 i32) (local $l186 i32) (local $l187 i32) (local $l188 i32) (local $l189 i32) (local $l190 i32) 
(local $l191 i32) (local $l192 i32) (local $l193 i32) (local $l194 i32) (local $l195 i32) (local $l196 i32) (local 
$l197 i32) (local $l198 i32) (local $l199 i32) (local $l200 i32) (local $l201 i32) (local $l202 i32) (local $l203
i32) (local $l204 i32) (local $l205 i32) (local $l206 i32) (local $l207 i32) (local $l208 i32) (local $l209 i32) 
(local $l210 i32) (local $l211 i32) (local $l212 i32) (local $l213 i32) (local $l214 i32) (local $l215 i32) (local 
$l216 i32) (local $l217 i32) (local $l218 i32) (local $l219 i32) (local $l220 i32) (local $l221 i32) (local $l222 
i32) (local $l223 i32) (local $l224 i32) (local $l225 i32) (local $l226 i32) (local $l227 i32) (local $l228 i32) 
(local $l229 i32) (local $l230 i32) (local $l231 i32) (local $l232 i32) (local $l233 i32) (local $l234 i32) (local 
$l235 i32) (local $l236 i32) (local $l237 i32) (local $l238 i32) (local $l239 i32) (local $l240 i32) (local $l241 
i32) (local $l242 i32) (local $l243 i32) (local $l244 i32) (local $l245 i32) (local $l246 i32) (local $l247 i32) 
(local $l248 i32) (local $l249 i32) (local $l250 i32) (local $l251 i32) (local $l252 i32) (local $l253 i32) (local 
$l254 i32) (local $l255 i32) (local $l256 i32) (local $l257 i32) (local $l258 i32) (local $l259 i32) (local $l260 
i32) (local $l261 i32) (local $l262 i32) (local $l263 i32) (local $l264 i32) (local $l265 i32) (local $l266 i32) 
(local $l267 i32) (local $l268 i32) (local $l269 i32) (local $l270 i32) (local $l271 i32) (local $l272 i32) (local 
$l273 i32) (local $l274 i32) (local $l275 i32) (local $l276 i32) (local $l277 i32) (local $l278 i32) (local $l279 
i32) (local $l280 i32) (local $l281 i32) (local $l282 i32) (local $l283 i32) (local $l284 i32) (local $l285 i32) 
(local $l286 i32) (local $l287 i32) (local $l288 i32) (local $l289 i32) (local $l290 i32) (local $l291 i32) (local 
$l292 i32) (local $l293 i32) (local $l294 i32) (local $l295 i32) (local $l296 i32) (local $l297 i32) (local $l298 
i32) (local $l299 i32) (local $l300 i32) (local $l301 i32) (local $l302 i32) (local $l303 i32) (local $l304 i32) 
(local $l305 i32) (local $l306 i32) (local $l307 i32) (local $l308 i32) (local $l309 i32) (local $l310 i32) (local 
$l311 i32) (local $l312 i32) (local $l313 i32) (local $l314 i32) (local $l315 i32) (local $l316 i32) (local $l317 
i32) (local $l318 i32) (local $l319 i32) (local $l320 i32) (local $l321 i32) (local $l322 i32) (local $l323 i32) 
(local $l324 i32) (local $l325 i32) (local $l326 i32) (local $l327 i32)
 (local.set $l40
 (global.get $g0))
 (local.set $l41
 (i32.const 176))
 (local.set $l42
 (i32.sub
 (local.get $l40)
 (local.get $l41)))
 (global.set $g0
 (local.get $l42))
 (local.set $l43
 (i32.const 102))
 (i32.store offset=168
 (local.get $l42)
 (local.get $p0))
 (i32.store offset=164
 (local.get $l42)
 (local.get $p1))
 (i32.store offset=160
 (local.get $l42)
 (local.get $p2))
 (i32.store offset=156
 (local.get $l42)
 (local.get $p3))
 (i32.store offset=152
 (local.get $l42)
 (local.get $p4))
 (i32.store offset=148
 (local.get $l42)
 (local.get $p5))
 (i32.store offset=144
 (local.get $l42)
 (local.get $p6))
 (i32.store offset=140
 (local.get $l42)
 (local.get $p7))
 (i32.store offset=136
 (local.get $l42)
 (local.get $p8))
 (i32.store offset=132
(local.get $l42)
 (local.get $p9))
 (i32.store offset=128
 (local.get $l42)
 (local.get $p10))
 (i32.store offset=124
 (local.get $l42)
 (local.get $p11))
 (i32.store offset=120
 (local.get $l42)
 (local.get $p12))
 (i32.store offset=116
 (local.get $l42)
 (local.get $p13))
 (i32.store offset=112
 (local.get $l42)
 (local.get $p14))
 (i32.store offset=108
 (local.get $l42)
 (local.get $p15))
 (i32.store offset=104
 (local.get $l42)
 (local.get $p16))
 (i32.store offset=100
 (local.get $l42)
 (local.get $p17))
 (i32.store offset=96
 (local.get $l42)
 (local.get $p18))
 (i32.store offset=92
 (local.get $l42)
 (local.get $p19))
 (i32.store offset=88
 (local.get $l42)
 (local.get $p20))
 (i32.store offset=84
 (local.get $l42)
 (local.get $p21))
 (i32.store offset=80
 (local.get $l42)
 (local.get $p22))
 (i32.store offset=76
 (local.get $l42)
 … CORTADO 
 (br_if $B7
 (i32.le_u
 (i32.load offset=20
 (local.get $p0))
 (i32.load offset=28
 (local.get $p0))))
 (local.set $l2
 (i32.or
 (call $f17
 (local.get $p0))
 (local.get $l2))))
 (block $B8
 (br_if $B8
 (i32.eqz
(local.get $l1)))
 (call $f11
 (local.get $p0)))
 (br_if $L5
 (local.tee $p0
 (i32.load offset=56
 (local.get $p0))))))
 (call $f15))
 (local.get $l2))
 (func $f17 (type $t2) (param $p0 i32) (result i32)
 (local $l1 i32) (local $l2 i32)
 (block $B0
 (br_if $B0
 (i32.le_u
 (i32.load offset=20
 (local.get $p0))
 (i32.load offset=28
 (local.get $p0))))
 (drop
 (call_indirect $__indirect_function_table (type $t5)
 (local.get $p0)
 (i32.const 0)
 (i32.const 0)
 (i32.load offset=36
 (local.get $p0))))
 (br_if $B0
 (i32.load offset=20
 (local.get $p0)))
 (return
 (i32.const -1)))
 (block $B1
 (br_if $B1
 (i32.ge_u
 (local.tee $l1
 (i32.load offset=4
 (local.get $p0)))
 (local.tee $l2
 (i32.load offset=8
 (local.get $p0)))))
 (drop
 (call_indirect $__indirect_function_table (type $t7)
 (local.get $p0)
 (i64.extend_i32_s
 (i32.sub
 (local.get $l1)
 (local.get $l2)))
 (i32.const 1)
 (i32.load offset=40
 (local.get $p0)))))
 (i32.store offset=28
 (local.get $p0)
 (i32.const 0))
 (i64.store offset=16
 (local.get $p0)
 (i64.const 0))
 (i64.store offset=4 align=4
 (local.get $p0)
 (i64.const 0))
 (i32.const 0))
 (func $__errno_location (export "__errno_location") (type $t0) (result i32)
(i32.const 1040))
 (table $__indirect_function_table (export "__indirect_function_table") 1 1 funcref)
 (memory $memory (export "memory") 256 256)
 (global $g0 (mut i32) (i32.const 5243936))
 (global $g1 (mut i32) (i32.const 0))
 (global $g2 (mut i32) (i32.const 0)))
```
Hay una flag falsa (que claramente se lee esta no es la flag) definida en el código. Al final el bloque nos interesa analizar es el siguiente, previo filtrado de constantes.

```bash
(i32.const 102))
(i32.const 108))
(i32.const 97))
(i32.const 103))
(i32.const 123))
(i32.const 78))
(i32.const 79))
(i32.const 84))
(i32.const 72))
(i32.const 69))
(i32.const 70))
(i32.const 76))
(i32.const 65))
(i32.const 71))
(i32.const 82))
(i32.const 88))
(i32.const 125))
```
Ahora solo queda convertir de la tabla ASCII a texto para obtener la flag.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto34-1.png)

**_flag{WASM_REVERSING_IS_HARD_BUT_FASTEST}_**

---
## **Reto 35**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>A un compañero tuyo le gustan mucho las figuritas con alambres. Hace bicicletas con tan solo unos clips de oficina.
>
>Esta vez te ha propuesto un desafío para conocer un código PIN de alguno de los muchos laboratorios existentes en el edificio. Como delegado de curso tiene acceso al laboratorio y posiblemente este código sea el de una de las puertas de acceso.
>
>Si consigues descifrarlo vas a poder acceder a esos importantes recursos que te permitirán empezar a descubrir parte de la historia de la institución.
>
>Pregunta:
>¿Cuál es el código PIN mirando las figuras? Ayúdate del esquema adjunto.
>
>**Datos proporcionados:**
>
>Fichero esquema de decodificación.

Se nos presenta un fichero de imagen con unos símbolos.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto35-1.png)

De igual forma tenemos un mensaje que descifrar. Es el número PIN de una estancia del edificio.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto35-2.png)

Las filas de arriba abajo pertenecen a unidades, decenas, centenas y miles. Tan solo debemos partir esta figura en estas cuatro “geometrías” en orden inverso. Primero miles, centenas, decenas y unidades.

No se ha mencionado, pero es deducible que el orden de izquierda a derecha incrementa la numeración representativa de cada fila. Esto es, la última fila y en orden tendrá el valor de 1000, 2000, 3000, … y así con las centenas, 100, 2000, 300, …

De tal forma que si superponemos las figuras obtendremos el código PIN 5703.

No hay figura que corresponda con la tercera posicion.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto35-3.png)
