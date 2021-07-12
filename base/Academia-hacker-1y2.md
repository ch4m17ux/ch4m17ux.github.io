# Academia Hacker Incibe- #writeUp

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 
# TL:DR

---

## **Reto 1**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Desde la creación del instituto, algunos alumnos se han encargado de la gestión del periodido local, "El noticiero", donde se intercambian mensajes y escriben artículos didácticos.
>
>En uno de los artículos alguien anónim@ ha lanzado un reto. Asegura haber escondido un mensaje en el libro más universal de la literatura castellana. En su mensaje advierte que para empezar, nos proporciona algunas coordenadas para que las mentes mas brillantes del instituto puedan resolverlo.
>
>¿Cuál es el mensaje secreto que ha enviado el alumno anónimo y ha escondido este alumn@?
>
>Nota: En la solución, reemplaza espacios con "_".
>
>Datos proporcionados.
>
>10:8:2
23:11:1
30:8:2
30:26:7
35:1:7
151:19:10
151:11:8
152:11:5

En el reto nos indican que un personaje ha "*escondido un mensaje en el libro más universal de la literatura castellana*", por lo que deducimos que se trata de "*El Quijote - Miguel de Cervantes Saavedra*"; y dentro del zip que nos entregan con el reto, tenemos una copia del mismo.

Debido a estas conjeturas, procedemos a abrir el PDF del libro y encontramos que es una version del mismo; revisando los datos que nos han proporcionado, podriamos decir que nos estan indicando que debemos buscar algunas palabras para formar la flag, como no tenemos 152 capitulos, nos decantamos que nos estan indicando que debemos buscar: ***Pagina:Linea:Palabra***.

Siguiendo esta premisa, encontramos:
queres, saber, noticia, sobre, conocer, misterio, quien, hizo

Y dando el formato de la flag:
**flag{querer_saber_noticia_sobre_conocer_misterio_quien_hizo}**

---

## **Reto 2**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Después de muchos años recopilando documentación, fotos y artículos, se ha decidido realizar una limpieza y llevar la documentación antigua a una nueva sala que le ha cedido el instituto.
>
>En esta sala se pueden archivar de una forma sencilla por fecha todos los documentos del periodico.
>
>Durante este proceso moviendo documentos, una hoja extraña se cae entre los documentos que lleváis.
>
>Contiene un texto ilegible junto a la referencia del emperador Julio César. ¿Podrás sacar en claro que quería decir la nota?
>
>**Datos proporcionados:**
>
>Yn fvthvragr vasbeznpvba rf pbasvqrapvny. Gr nlhqnen n cebfrthve ra yn vairfgvtnpvba. Ab gr pbasvrf, ab gbqnf ynf vasbeznpvbarf qr ynf dhr qvfcbarzbf fba gna snpvyrf pbzb rfgn ebgnpvba qr pnenpgrerf. Sveznqb: ha nzvtb.
>
>synt{rfgnzbf_rzcrmnaqb_n_pbabpre_nytb_qr_uvfgbevn} 

Nos estan proporcionando un mensaje que esta codificado, nos hacen alusion a Julio Cesar, asi que lo primero que pensamos es en cifrado Cesar (Rot13).  Por lo que procedemos a decodificarlo con cualquier web que nos permite hacerlo y obtenemos.

O por consola tambien podriamos realizarlo:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto2.png)

Facilmente podemos encontrar la flag solicitada:
**flag{estamos_empezando_a_conocer_algo_de_historia}**

---

## **Reto 3**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Al darle la vuelta a la hoja, veis que también tiene otro texto escrito en esa parte, aunque tampoco lo entendéis. Se adjunta también un fichero con extensión pyc. ¿Nos servirá de ayuda?
>
>¿Podrás proporcionarnos la otra información que está en la otra cara de la hoja?
>
>**Datos proporcionados:**
>
>Ax8VCB4HEAAGDDMEBRERPhENAh8DLQQcEQERMAgaBjERAhwEGgADHA==
>
>**Datos extra:**
>*Os proporcionamos alguna indicación para empezar a resolver el reto: uncompyle6 es una herramienta que descompila el byte-code de Python. Devuelve el fichero original, que necesitarás para resolver la prueba*.

Seguimos las instrucciones y nos instalamos uncompyle6, usando la versión para python 2.7: [https://palomarinfosec.github.io/Presentations/InstallingUncompyle6.pdf](https://palomarinfosec.github.io/Presentations/InstallingUncompyle6.pdf)

El paso mas importante es:

```
# sudo pip install uncompyle6-3.7.4-py2-none-any.whl
# uncompyle6 --version
```
Esta herramienta nos decompila el el fichero python que esta en el zip (contraseña del zip: _reto03_afe0cb6c1bdfbc79e900a427244961cb24ee8141_)

En mi caso lo he volcado a otro fichero, de otro modo lo pone en la salida de la consola:
  
![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto3.jpg)
  Verificamos el codigo que nos ha decompilado y vemos como realiza la codificacion del mensaje, vemos que tenemos dos opciones: cifrado y descifrado.

```
import binascii, itertools, base64, sys
	def xor_crypt_string(data, key='estoesunaclaveparacifrar', encode=False, decode=False):
		from itertools import izip, cycle
		import base64
		if decode:
			data = base64.decodestring(data)
		xored = ('').join(chr(ord(x) ^ ord(y)) for x, y in izip(data, cycle(key)))
		if encode:
			return base64.encodestring(xored).strip()
		return xored
	secret_data = sys.argv[1]
	print 'Cifrado'
	print xor_crypt_string(secret_data, encode=True)
	print 'Descifrado'
	print xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True)
```

Lo modificamos para que nos arroje la salida que queremos (que seria decodificar el mensaje) y podemos tener el siguiente codigo:

```
import binascii, itertools, base64, sys
	def xor_crypt_string(data, key='estoesunaclaveparacifrar', encode=False, decode=False):
		from itertools import izip, cycle
		import base64
		if decode:
			data = base64.decodestring(data)
		xored = ('').join(chr(ord(x) ^ ord(y)) for x, y in izip(data, cycle(key)))
		if encode:
			return base64.encodestring(xored).strip()
		return xored	
	secret_data = 'Ax8VCB4HEAAGDDMEBRERPhENAh8DLQQcEQERMAgaBjERAhwEGgADHA=='
	claro = xor_crypt_string(secret_data,decode=True)
	print (claro)
```
Al ejecutarlo, nos arroja la flag que estamos buscando:
**flag{tengo_esta_clave_entre_mis_papeles}**

---

## **Reto 4**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Con la información que habéis obtenido, intentáis utilizar las credenciales para poder acceder al ordenador del periodico y al entrar os descargáis un archivo.
>El fichero original ha cifrado alguna información secreta que debes obtener para que la investigación no se atasque. Esto es lo que sabemos que ha devuelto la salida del fichero que has obtenido al entrar en la web del periódico.
>
 >**Datos proporcionados:**
>
>Hemos recibido este mensaje junto a unas instrucciones para su manejo. Parece un completo enigma.
>
>59556843656d517a545764684d3035355a4735425a317074526e526a626d646e57544a
>61633249794e476461534842785a55644e5a316b7a566a42615630316e596c684f4d57
>51795a32646156315a6f5a4668765a325674536e4e684d6e4e6e576d3543626d4e59515
>7645a57454a74576a4a6e5a32517962486c684d30316e596c6857613246755a32645a57
>48426f597a4e725a316c59516d356957456c6e59556477626c6c745557646c574842785
>95663775a324e496144466b6257396e5a56646f64574a745a326469563342785930646a
>5a32466e5054303d
>
>Modelo: M3
>Reflector: ????
>ROT1.: 1
>ROT2.: 2
>ROT3.: 3
>POS1.: A
>POS2.: B
>POS3.: C
>ANILLO1: A
>ANILLO2: B
>ANILLO3: C
>PLUGBOARD: bq cr di ej kw mt os px uz gh

Vemos que debemos utilizar una web que nos permita decodificar la maquina enigma.  Al tratar de hacerlo directamente, nos arroja un mensaje muy extraño, asi que analizamos y encontramos que si decodificamos el texto en `HEX` y 2 veces `BASE64` (*hecho desde linux para evitar historias raras de los conversores online*) sale esto:

*hpsws ksrvp famrx cflon dzjxc cutec msuwh eeauz zblkk fpgqp apfgh wirks mudjx azasy apgmr hjgbd yzjim pxuvj yhnnh mjjpg j*

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto4.png)

Obtenemos el mensaje:  

*PONGA ATENC IONSI FRACA SAMOS ENEST AMISI ONNOS VEREM OSABO CADOS APERD ERLOT ODOAN OTEES TABAN DERAE NIGMA MTRES UKWBV I*

Si lo organizamos, que sea mas legible:
  
*PONGA ATENCION SI FRACASAMOS EN ESTA MISION NOS VEREMOS ABOCADOS A PERDERLO TODO ANOTE ESTA BANDERA ENIGMAMTRES UKWBV I*

Deducimos que la flag seria:
**flag{ENIGMAMTRESUKWBVI}**

---

## **Reto 5**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Habláis con el director del instituto y os permite acceder al contenido del disco. Al entrar encontráis un "pcap". ¿Qué es un "pcap"? os preguntáis. No lo sabemos, pero habrá que investigar.
>
>Los datos os suenan codificados en hexadecimal, pero ... ¿Cómo recomponer estas piezas de cada petición? Además, hay mucho ruido de navegación en el fichero.
>
>**Datos proporcionados:**
>
>Fichero "pcap" descargable

Nos descargamos el pcap que nos entregan, y lo analizamos con wireshark.

Vemos mucho trafico UDP, TCP, TLS y demas, como nos han indicado en la descripcion del reto.  Asi que analizamos un poco mas y encontramos que hay algunas peticiones DNS, que tienen un formato inicial HEX, asi que lo filtramos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto5.jpg)

Y podemos obtener (tomando solo los valores hexadecimales) el siguiente mensaje:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto5-1.png)

Conseguimos la flag:
**flag{dns_spy_exfiltration}**

---

## **Reto 6**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Parece que alguien desde una cuenta anónima está intentado ayudar en la investigación y os ha enviado otro fichero pcap. Lo ha capturado desde alguna clase de informática que se dio en el instituto.
>
>Hay varias tramas que se corresponden a una subida FTP. Nos piden encontrar el contenido de lo que se ha descargado para proseguir en la investigación. Se trata de un fichero que se han descargado.
>
>**Datos proporcionados:**
>
>Fichero pcap descargable.

Abrimos el pcap entregado que tenemos en Wireshark y observamos las tramas. Encontramos que se ha hecho una descarga de dos ficheros, por un lado tenemos un zip denominado: flag.zip y por otro lado un txt denominado: passwords.txt

Vamos filtrando el trafico por tramas y vemos que en el stream 2, tenemos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-1.png)

Podemos ver que hay una traza que tiene un tamaño mas grande que los demas, asi que tratamos de sacar ese fichero que ha sido descargado (en este caso del ftp). seleccionamos dicha trama y nos selecciona la parte que nos interesa, que en este caso es el fichero requerido.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-2.png)
Dandole clic derecho podemos exportar los bytes del fichero como un paquete.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-3.png)

Le ponemos un nombre y tenemos el fichero de la flag comprimido: flag.zip

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-4.png)

Al intentar descomprimirlo, nos solicita una contraseña.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-6.png)

Por esta razon, debemos buscar el listado de passwords, que habiamos visto que se habia descargado tambien. Por lo que seguimos filtrando las tramas y encontramos la traza que nos interesa.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto6-6.png)

Y realizamos la misma operacion que hemos realizado con la anterior traza, para obtener un fichero de claves: passwords.txt

Utilizamos este fichero para trata de crackear a traves de jonhTheRipper la contraseña.

```code
──(kali㉿kali)-[~/Descargas/incibe/reto06]
└─$ zip2john flag.zip > secret.hash
ver 1.0 efh 5455 efh 7875 flag.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=52, decmplen=40, crc=BF705D76

┌──(kali㉿kali)-[~/Descargas/incibe/reto06]
└─$ cat secret.hash
flag.zip/flag.txt:$pkzip2$1*2*2*0*34*28*bf705d76*0*42*0*34*bf70*81e2*5a85ba04cd58d275ddd202b91c0907b475dd8630
a025cc6e7e83d84ef15497534610b5cb941a0cfa8322467e565e33e0faaf21de*$/pkzip2$:flag.txt:flag.zip::flag.zip

┌──(kali㉿kali)-[~/Descargas/incibe/reto06]
└─$ sudo john hash_6 -w=passwords.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
karina (flag.zip/flag.txt)
1g 0:00:00:00 DONE (2021-05-10 15:37) 12.50g/s 2912p/s 2912c/s 2912C/s danielle..january
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
  
Obtenemos la contraseña para descomprimir el fichero comprimido flag.zip, y dentro tenemos un txt con la flag solicitada.

Conseguimos la flag:
**flag{ftp_stream_pcap_with_credentials!}**

---

## **Reto 7**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En el escritorio del usuario de uno de los ordenadores localizáis una aplicación. Os aseguráis de que no sea maliciosa y ejecutáis el fichero exe. Parece contener dos entradas de texto.
>
>Hay dos flags en esta prueba, recupera la flag1 del fichero exe.
>
>**Datos proporcionados:**
>
>Fichero ejecutable.

Debugueando con IDA PRO (lo que ha realizado BitOverRun), podemos ver que se esperan dos entradas (Este reto es la primera parte y continua en el reto8).

En este reto se nos pide la Flag1. En el codigo vemos que tenemos un string:

```code
AAICBBIOCQASCAUOAg4PAgQFCAUO
```
  
![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto7-1.png)

Que analizando mejor el codigo encontramos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto7-2.png)


Se nos indica que esta codificado con XOR y un Base64. Aun mas, vemos que el XoR lo realiza con la key 41

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto7-3.png)

Nos queda unicamente decodificarlo con los datos que hemos obtenido.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto7-4.png)


Obtenemos la flag:
**flag{ACCESOHASIDOCONCEDIDO}**

---

## **Reto 8**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> En el escritorio del usuario de uno de los ordenadores localizáis una aplicación. Os aseguráis de que no sea maliciosa y ejecutáis el fichero exe. Parece contener dos entradas de texto.
>
>Hay dos flags en esta prueba, recupera la flag2 del fichero exe.
>
>**Datos proporcionados:**
>
>Fichero ejecutable.

Este reto es la secuela del anterior Reto. Siguiendo con el analisis del mismo, encontramos que hay una segunda flag, mas corta, pero que vemos claramente.

```code
PBZCYRGNQB
```
  
![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto8-1.png)

Revisando las funciones, encontramos que ha sido codificada en Rot13

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto8-2.png)

Por lo que solo nos queda, realizar el proceso inverso.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto8-3.png)

Obtenemos la flag:
**flag{COMPLETADO}**

---

## **Reto 9**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> Revisando la información en Documents, encontráis un mensaje muy extraño. ¿Podrías ayudar a resolverlo?
>
>Se repiten con frecuencia algunos pares de caracteres. Parece hexadecimal.
>
>**Datos proporcionados:**
>
>2d 2e 2e 20 2e 2e 20 2e 2e 2e 20 2d 2e 2d 2e 20 2d 2d 2d 20 2e 2e 2e 2d 20 2e 20 2e 2d 2e 20 2e 2e 2d 2d 2e 2d
>
>20 2e 2e 2e 2e 20 2e 20 2d 2e 2e 2d 20 2e 2e 2d 2d 2e 2d 20 2d 2d 20 2d 2d 2d 20 2e 2d 2e 20 2e 2e 2e 20 2e 20
>
>2e 2e 2d 2d 2e 2d 20 2d 2e 2d 2e 20 2d 2d 2d 20 2d 2e 2e 20 2e

Tenemos una serie de caracteres que estan en algun tipo de codificacion, asi que utilizamos CyberChef y, tratamos de determinar que tipo de cifrado tiene y si podemos decodificarlo.

Determinado que esta en Hexadecimal, y finalmente en codigo Morse.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto9.png)

Obtenemos nuestra flag:
**flag{DISCOVER_HEX_MORSE_CODE}**

---

## **Reto 10**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
> La profesora de música ha recibido un mensaje en su correo con un fichero donde aparecen algunas passwords cifradas.
>
>Te pide descifrarlas. La solución son todas las contraseñas concatenadas con '_'.
>
>Pregunta:
>¿Eres capaz de encontrar todas las contraseñas?
>
>flag{password1_password2_password3_password4}
>
>**Datos proporcionados:**
>
>fichero txt.

Se nos ha entregado un fichero con algunos Hashes.
 
```code
┌──(ch4m0㉿kali)-[~/Descargas/incibe/reto10]
└─$ cat shadow.txt
$6$yMJT8Nf23i7Z1WkF$ChxmECeWSs3W8Or1Ogf4eapPz5FNcBM4SBvZG.21fI0wpNUmR1yCmK71r7sYFMXCL3deD5BWDD/6A4WU66cjv0
$6$xonBhxE19HmG8.DR$LdediY0FTHMUPyeQAiEFVgUR6rKVrOGcCECCn.EQupIwH2EyZqib3gc5kJfuwp/ppLJY41Ap5KEUf7RCk3T4O0
$6$ooyV5Z5dEaDfyPom$VnKneoTa7s7DJRFFarye2sjZiwWbrr1jQ28lzw36OGaAChy1K14GY6BEFTABLGjZ8Xs4iSmbaZdfDXYFi9ED71
$6$a5m5M9J/FEJGzyrd$shv36BNOS58W8VQBbjLKESl/3QjJxomkBb84j9Mw2g04JW3TIVGstOmJQFT5wdpl1soe9XjI3YjDNNH6uXv7s1
```
  
Segun nos indicas, debemos crackear las constraseñas que tenemos en este fichero. lo primero que debemos hacer es identificar que tipo de cifrado tienen.

```code
┌──(ch4m0㉿kali)-[~/Descargas/incibe/reto10]
└─$ hashid shadow.txt
--File 'shadow.txt'--
Analyzing '$6$yMJT8Nf23i7Z1WkF$ChxmECeWSs3W8Or1Ogf4eapPz5FNcBM4SBvZG.21fI0wpNUmR1yCmK71r7sYFMXCL3deD5BWDD/6A4WU66cjv0'
[+] SHA-512 Crypt
Analyzing '$6$xonBhxE19HmG8.DR$LdediY0FTHMUPyeQAiEFVgUR6rKVrOGcCECCn.EQupIwH2EyZqib3gc5kJfuwp/ppLJY41Ap5KEUf7RCk3T4O0'
[+] SHA-512 Crypt
Analyzing '$6$ooyV5Z5dEaDfyPom$VnKneoTa7s7DJRFFarye2sjZiwWbrr1jQ28lzw36OGaAChy1K14GY6BEFTABLGjZ8Xs4iSmbaZdfDXYFi9ED71'
[+] SHA-512 Crypt
Analyzing '$6$a5m5M9J/FEJGzyrd$shv36BNOS58W8VQBbjLKESl/3QjJxomkBb84j9Mw2g04JW3TIVGstOmJQFT5wdpl1soe9XjI3YjDNNH6uXv7s1'
[+] SHA-512 Crypt
--End of file 'shadow.txt'--
```
  
Tenemos que estan en SHA-512, asi que procedemos a crackearlo con hashcat.

```code
┌──(ch4m0㉿kali)-[~/Descargas/incibe/reto10]
└─$ hashcat -a 0 -m 1800 shadow.txt /usr/share/wordlists/rockyou.txt -o cracked.txt
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz, 2813/2877 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

INFO: All hashes found in potfile! Use --show to display them.

Started: Mon May 10 16:41:21 2021
Stopped: Mon May 10 16:41:22 2021
```

Nos arroja las contraseñas crackeadas.

```code
┌──(ch4m0㉿kali)-[~/Descargas/incibe/reto10]
└─$ cat cracked.txt
$6$xonBhxE19HmG8.DR$LdediY0FTHMUPyeQAiEFVgUR6rKVrOGcCECCn.EQupIwH2EyZqib3gc5kJfuwp/ppLJY41Ap5KEUf7RCk3T4O0:dragon
$6$yMJT8Nf23i7Z1WkF$ChxmECeWSs3W8Or1Ogf4eapPz5FNcBM4SBvZG.21fI0wpNUmR1yCmK71r7sYFMXCL3deD5BWDD/6A4WU66cjv0:whatever
$6$ooyV5Z5dEaDfyPom$VnKneoTa7s7DJRFFarye2sjZiwWbrr1jQ28lzw36OGaAChy1K14GY6BEFTABLGjZ8Xs4iSmbaZdfDXYFi9ED71:princesa
$6$a5m5M9J/FEJGzyrd$shv36BNOS58W8VQBbjLKESl/3QjJxomkBb84j9Mw2g04JW3TIVGstOmJQFT5wdpl1soe9XjI3YjDNNH6uXv7s1:administrator
```
  
Asi que la flag seria:
**flag{dragon_whatever_princesa_administrator}**