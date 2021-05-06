# Academia Hacker Incibe- #writeUp

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 
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

```bash
ch4m0@DESKTOP-DORD02K:~/ch4m17ux.github.io$ echo 'Yn fvthvragr vasbeznpvba rf pbasvqrapvny. Gr nlhqnen n cebfrthve ra yn vairfgvtnpvba. Ab gr pbasvrf, ab gbqnf ynf vasbeznpvbarf qr ynf dhr qvfcbarzbf fba gna snpvyrf pbzb rfgn ebgnpvba qr pnenpgrerf. Sveznqb: ha nzvtb.

synt{rfgnzbf_rzcrmnaqb_n_pbabpre_nytb_qr_uvfgbevn}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'

La siguiente informacion es confidencial. Te ayudara a proseguir en la investigacion. No te confies, no todas las informaciones de las que disponemos son tan faciles como esta rotacion de caracteres. Firmado: un amigo.

flag{estamos_empezando_a_conocer_algo_de_historia}
```
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
>59556843656d517a545764684d3035355a4735425a317074526e526a626d646e57544a61633249794e476461534842785a55644e5a316b7a566a42615630316e596c684f4d5751795a32646156315a6f5a4668765a325674536e4e684d6e4e6e576d3543626d4e595157645a57454a74576a4a6e5a32517962486c684d30316e596c6857613246755a32645a5748426f597a4e725a316c59516d356957456c6e59556477626c6c745557646c57484278595663775a324e496144466b6257396e5a56646f64574a745a326469563342785930646a5a32466e5054303d
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