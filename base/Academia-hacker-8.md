# Academia Hacker Incibe - #writeUp - 8 semana

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/academia-hacker-incibe.jpg)

Durante el mes de Mayo y Junio de 2021, estaremos participando en Academia Hacker.  Una iniciativa de [Incibe](https://www.incibe.es/) para formar y encontrar las capacidades en Ciberseguridad.

El registro esta cerrado, debido a que se ha tenido una convocatoria de 400 equipos con un minimo de 4 participantes y un maximo de 8.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---
## **Reto 36**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>En uno de los laboratorios de computación encuentras una máquina apagada con un post-it en el lateral: "/root/Desktop/reto36/reversesecret - Resolver mediante ingeniería inversa".
>
>Parece que te animas a encender el ordenador, un viejo pentium que todavía arranca. Guardas el fichero a tu máquina para trabajar cómodamente y empiezas el desafío.
>
>Al reverso del post-it se puede leer: "Enviar flag a mi número personal, se recompensará"
>Pregunta:
>¿Qué condiciones necesitará este binario para que imprima la flag?
>
>**Datos proporcionados:**
>
>Fichero binario.

Previamente en IDA PRO se ve que la rutina inicial pide 3 argumentos y que hay hasta 4 checks diferentes.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto36-1.png)

Arrancamos maquina virtual de Incibe e instalamos un debugger edb:

Instalamos el debugger 
```bash
┌──(root@kali)-[~/]
└─# sudo apt install edb-debugger
```
Arrancamos el debugger
```bash
┌──(root@kali)-[~/]
└─# edb
```
Abrimos el archivo que queremos debuggar introduciendo 3 parametros al azar.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto36-2.png)

Empezamos a debuggar con F8 y F7 Para llegar donde queremos….

La idea es llegar a los checks para poder quitarlos y ver si son necesarios o simplemente se pueden bypasear…

Con F8 llegamos hasta las rutinas de ejecución y sus correspondientes “JE”. Pasamos y cuando lleguemos a los JE, botón derecho del ratón encima -> Edit ->

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto36-3.png)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto36-4.png)

Esta accion la hacemos en los 3 primeros checks y seguimos con F8 …

Hasta que el programa acaba con return “0” -> SIN FALLOS….

Vemos el log que aparece en la ventana del propio programa… Por detrás….

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto36-5.png)

**_flag{g00d_j0b_reversers}_**

---
## **Reto 37**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Os llega un mensaje a vuestro Telegram, de una persona que no conocéis. El mensaje solamente pone "Escuchadlo", y un mp3.
>
>Pregunta:
>¿Qué esconde el archivo de sonido? ¿Solamente es una canción?
>
>**Datos proporcionados:**
>
>Archivo de audio con codificación MP3

El archivo de audio es la 5ª Sinfonía de Beethoven. Además, tiene 3 zonas superpuestas de un código morse.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto37-1.png)

El archivo final está normalizado y tiene este aspecto, evitando que se pueda detectar esto de una forma sencilla.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto37-2.png)

Al parecer es una pista normal en estéreo, pero en las posiciones de unión se escucha un ligero pitido.

La unión hace que la pista en morse se centre más en el lado izquierdo (donde era sordo Beethoven) y su sinfonía en la parte derecha. Si se sitúa que solo se quiere escuchar la pista izquierda, el código morse es más claro.

Al realizar la mezcla de sonidos, la carga del código morse ha sido un 100% a la izquierda, y la carga de la sinfonía un 90% hacia la derecha. Esto provoca que ambas se pueden escuchar tanto a un lado como al otro, pero el volumen con el que se escucha no es el mismo.

Teniendo en cuenta que un pitido largo es un guion y uno corto un punto (nomenclatura estándar para escritura morse), lo que nos encontramos dentro del audio es la siguiente codificación durante 3 secuencias separadas a lo largo de la canción:

..... -.-- -- .--. .... --- -. -.--

Que descodificado significa: **5YMPHONY**

Las secuencias se pueden encontrar en las siguientes posiciones del audio:

-   1m 6s
-   2m 39s
-   6m 44s
    
Además, el audio tiene al final del archivo un zip comprimido con contraseña.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto37-3.png)
Una vez extraído este archivo zip, se puede usar la contraseña obtenida del código morse para descomprimir el archivo y obtener el flag, ya de dentro del zip hay un archivo “flag.txt”.

***flag{ES_14_5ª_S1nfonIA}***

---
## **Reto 38**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Distintos profesores de diversas materias se han puesto de acuerdo para confeccionar un rompecabezas para sus alumnos usando los conocimientos adquiridos para subir la nota global
>
>Pregunta
>¿Puedes resolver el rompecabezas y encontrar el mensaje oculto?
>
>Nota: una vez resuelto el mensaje debe entregarse como flag{mensaje}, quedando el mensaje libre de espacios
>
>**Datos proporcionados:**
>
>1. flag.txt
>2. 1.png
>3. 2.jpg
>4. file

Nos dan la siguiente información en el fichero flag.txt:

```bash
Modell 
1.png + 2.jpg
Walzenlage     Posición del rodillo
V II III
Stellung       posición
file extension
Ringstellung   Posición del anillo
13 17 04
---- Steckerverbindungen ----
gu cr di ej kw mt ps ox qz bh Conexiones de enchufe
######################################################################
niwyy lufqj yeegx hpbas wnkky gtwwd rxmhs cczuh trtsu lssje idaxh axzj
```

Junto con esta información tenemos dos imágenes:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto38-1.png)

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto38-2.png)

La primera imagen nos indica que es una maquina “ENIGMA 1” y la segunda haciendo un poco de OSINT encontramos que es una foto de NORUEGA

Además nos dan un fichero sin extensión (file) que aparece como datos. No tiene nada que nos permita saber que fichero es (Magic Bytes) pero haciendo un strings apunta a aplicación android.

Descargo un APK que es un ZIP con muchos ficheros dentro y voy probando todos los que aparecen hasta que aparece un texto legible.

Uniendo toda esta informacion, utilizamos una web que nos permite decodificar mensajes de maquinas Enigma.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto38-3.png)

Encontramos la flag que nos solicitan:
**_flag{enhorabuenaahoraestaslistoparalosmensajesentiemposdificiles}_**

---
## **Reto 39**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Un inspector de la administración se ha olvidado un pen drive en la mesa de la sala multiusos. Hemos encontrado en su interior un script en PowerShell ofuscado.
>
>Pregunta:
>¿Podrías analizarlo y descubrir que esconde?
>
>**Datos proporcionados:**
>
>Script en PowerShell descargable

Primero Tenemos Que Desofuscar El Codigo:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-1.png)

Cambiamos la cantidad de guiones por el valor. Si tenemos --- lo cambiamos por 3, si tenemos ---------- se cambia por A. Parece ser una secuencia Hexadecimal.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-2.png)

Tras esto añadimos un echo al final con la parte mas grande del código para que nos diga que tenemos ahí.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-3.png)

Si ejecutamos este código nos da lo siguiente:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-4.png)

Si Quitamos “Char" Nos Quedan Un Monton De Valores:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-5.png)

Si Pasamos Todos Estos Valores a `Hex` Y Luego a `Ascii` Tenemos:

```bash
Write-Host -BackgroundColor white -ForegroundColor blue "Executing the process..."
$n = $MyInvocation.MyCommand.Name
if ($n.substring(0,1) -eq 'k'){
        #$xorkey = "try brute force!"
        Write-Host "Flag: V15SU05yAlEDUAZpYQJEB0dlWQFfWGplBVFQB0ZFVwZfSQ=="
        Write-Host -BackgroundColor green -ForegroundColor white "CONGRATZ!"
        exit
}
Write-Host -BackgroundColor red -ForegroundColor white "TRY HARDER!"
```
Obtenemos un string en Base64, y nos estan indicando que debemos realizar un XoR brute force, si lo intentamos tal como nos indican, vemos que no llegamos a buen puerto. Sin embargo, conocemos que:

El xor es auto inverso
Asi que a ^ b = c
y tambien a ^ c = b

Por lo que conocemos dos partes de la ecuacion: El codigo cifrado y lo que deberia ser parte del texto claro. Si lo pasamos por cyberchef obtenemos:

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-6.png)

Asi que la clave comienza por "12345", podemos ponerla como key e ir completando hasta que nos de la flag.

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto39-7.png)

**_flag{D3c0d3_P0w3rSh3ll_S4cc3ssf4l}_**

---
## **Reto 40**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>El profesor de matemáticas es alguien muy cercano, se ha interesado  por vuestro club de CTFs y os ha enviado un mensaje cifrado donde  asegura que con los datos proporcionados se podrá descifrar.
>
>Como premio al primero que lo consiga ... ¡Le aumentará 1 punto la nota final!
>
>Pregunta:
>¿Cual es el mensaje cifrado?
>
>**Datos proporcionados:**
>
>Fichero python

El participante recibirá un fichero `reto40.py` con el código con el que se ha cifrado la flag. Este código es el siguiente:

```bash
#!/usr/bin/env python3
from Crypto.Util.number import *
import gmpy2, binascii
from myrsa import myreal_p, myreal_q
from oximoron import flag
n = myreal_p * myreal_q
e = 0x10001
ciphertext = binascii.hexlify(long_to_bytes(pow(bytes_to_long(flag), e, n)))
file = open('secret.enc', 'w')
file.write("cipher: {}\nn: {}\ne: ".format(ciphertext, str(n), str(e)))
```

Este código produce un secret.enc con la información de flag cifrada, el valor para `N` y el exponente `E`. No da mas datos para p y q, valores que deben ser deducidos ya que la factorización de `N` es `p*q`. 

El contenido de secret es el siguiente:

```bash
secret: 
b'55d4e09b61c53557c2a265141206ba394a92648e290c0377ca58aec1b6811254125590ea3393563c485b
ad44cd5c80b85c219927a8bea340a4aa39dd7310afca'
N: 
8732851030901103315546024107527412423460054120791582645327296072030149520595598830189
737190136429774375847088648891282895380791041462467946364644597106651
E: 65537
```

Para esto accedemos a factordb y factorizamos el valor de N

![Academia Hacker](https://ch4m17ux.github.io/img/posts/academia-hacker/reto40-1.png)
```bash
p = 8943499445052244503125097349497546991018505772383891525
7965779692637908486619
q = 9764467571731469302829928738214358161149910425174602655
2841672042065803811329
```

Seguidamente, viendo el archivo Python “reto40.py” podemos ver que la flag está cifrada con un binascii.hexlify y long_to_bytes.

Viendo en la base de conocimientos de Python > binascii vemos que hexlify devuelve la representación hexadecimal de los datos binarios. Cada byte de datos se convierte en la correspondiente representación hexadecimal de 2 dígitos. El objeto bytes devuelto es, por tanto, el doble de largo que la longitud de los datos. (binascii — Convert between binary and ASCII — Python 3.9.5 documentation)

También vemos que hay una manera de invertir este cifrado con binascii.unhexlify (binascii — Convert between binary and ASCII — Python 3.9.5 documentation)

Haremos lo mismo con la transformación “long_to_bytes”, que la pasaremos a “bytes_to_long”.

Con todo esto ya podemos generar el script para descifrar el valor:

```bash
#!/usr/bin/env python3

from Crypto.Util.number import *
import binascii

n = 8732851030901103315546024107527412423460054120791582645327296072030149520595598830189737190136429774375847088648891282895380791041462467946364644597106651
e = 65537
c = bytes_to_long(binascii.unhexlify("55d4e09b61c53557c2a265141206ba394a92648e290c0377ca58aec1b6811254125590ea3393563c485bad44cd5c80b85c219927a8bea340a4aa39dd7310afca"))

p = 89434994450522445031250973494975469910185057723838915257965779692637908486619
q = 97644675717314693028299287382143581611499104251746026552841672042065803811329

phi = ( p - 1 ) * ( q - 1 )
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
```
Ejecutando el script obtenemos la flag:

```bash
┌──(root㉿kali)-[~/Descargas/incibe/8 semana/reto38]
└─$ python3 banderita.py          
b'flag{coppersmith_weak_rsa_roca_attack}'
```
***flag{coppersmith_weak_rsa_roca_attack}***

----------
# Fin

Cualquier errata o duda es bienvenida.
