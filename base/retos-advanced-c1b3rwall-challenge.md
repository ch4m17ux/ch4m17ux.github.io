# C1b3rwall Challenge: Retos Advanced

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-1.png)

En este post quiero traer los retos que la plataforma C1b3rwall Advanced, de la mano de Hacroks nos presenta.  Como he tratado en la entrada anterior, en esta oportunidad desarrollare los correspondientes al nivel Avanzado o Advanced.

Si quieres participar tienes información [ [Aquí](https://c1b3rwall.hackrocks.com/) ]

---

## **RETO 1 - No tan rápido**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Durante una investigación a una importante banda internacional de ladrones de vehículos de lujo, hemos interceptado un correo electrónico que contenía un archivo con extensión .pcap.
>
>El agente que interceptó el mensaje no conoce esta extensión, así que ha solicitado nuestra ayuda para comprobar si existe alguna pista que lleve a la detención de la cúpula de la banda. Además, ha compartido con nosotros el contenido del mensaje:
>
>_Wiesz, co robić. Wszystkie informacje znajdują się w linku._
>
>Para resolver este reto, deberás proporcionar cualquier información que lleve a nuestros agentes hacia la siguiente pista. Si por ejemplo encuentras un enlace externo, el token será la URL **completa**.

Nos entregan un fichero con extensión `.pcap` como indica la descripción. [Lo puedes descargar [AQUI\]
](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/net.pcap)

Una de las cosas que hago siempre, es verificar que lo que nos entregan si es lo que dicen que es; en este caso un fichero probablemente de captura de red.

```console
kali@kali:~/C1b3rChallenge$ file net.pcap 
net.pcap: Zip archive data, at least v1.0 to extract
```

Como observamos, el fichero no es precisamente una captura de trafico de red, sino que es un fichero `ZIP`.  Así que procedemos a descomprimirlo.

```console
kali@kali:~/C1b3rChallenge$ unzip net.pcap
Archive:  net.pcap
  inflating: trace/tlhahisoleseding  
  ```

Obtenemos una carpeta con un binario que podríamos ejecutar. Al hacerlo vemos que hay una cadena de texto que se repite.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-1.png)
Por lo que lo anterior podemos sacar la cadena de texto:

```console
uggcf://jjj.qebcobk.pbz/f/qtdipont5zsxygp/p1o3epunyyratr.mvc?qy=1|Wejdź na
naszą uzgodnioną witrynę
```

Que si la ponemos en CyberChef y jugamos haber que tipo de cifrado tiene, encontramos:

```console
https://www.dropbox.com/s/dgqvcbag5mfkltc/c1b3rchallenge.zip?dl=1|Jrwqź an
anfmą hmtbqavbaą jvgelaę
```

Y según la descripción tenemos:

>Si por ejemplo encuentras un enlace externo, el token será la URL **completa**.

Deducimos que la flag es:
**https://www.dropbox.com/s/dgqvcbag5mfkltc/c1b3rchallenge.zip?dl=1**

---

## **RETO 2 - La carta a los Ladrones Magos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> En nuestra investigación a la banda de ladrones de vehículos hemos encontrado un fichero PDF. A primera vista parece documentación oficial aprobada por el Gobierno de España, pero no tiene ningún sentido que una banda como esta quisiera guardar tan celosamente este documento.
>
>Tenemos la esperanza de encontrar información acerca de sus próximos objetivos. Quizá una lista de vehículos que robar o, al menos, el nombre real del archivo que la contiene.
>
>La solución a este reto será el nombre de dicho archivo.

Nos entregan un fichero, que podéis descargar de [AQUI](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/dotyczysamochodow.pdf).

Si lo abrimos vemos que efectivamente es un PDF, así que vamos a analizarlo,y podríamos empezar por ver sus "`strings`":

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-2.png)

Nos llama la atención esa cadena de texto que vemos al final, que al parecer esta cifrado en `Base64`, así que lo llevaremos a CyberChef y vemos que nos arroja.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-3.png)

Esta cifrado en `base64` y nos arroja un listado de vehículos, al final vemos lo que presumimos que sera el nombre del fichero que nos solicitan: ***LI5T4_V3HICUL05***

---
## **RETO 3 - ¿Cuánto cuesta este coche?**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Tras meses de conversaciones interceptadas, hemos conseguido detener a un cliente de la banda de ladrones de coches de lujo. Tenemos pruebas más que suficientes para mantenerlo detenido y hemos conseguido que nos diga el lugar y la hora en las que tendrá lugar la próxima compra.
>
>Gracias a que los ladrones nunca han visto a nuestro detenido, hemos decidido aprovechar para enviar un agente en su lugar a llevar a cabo la compra para así poder detenerlos. El problema es que el comprador se niega a cooperar más, y nos falta un dato de vital importancia para que nuestro agente no levante sospechas: el precio del coche que se va a comprar.
>
>Analizando el disco duro del detenido, hemos encontrado una imagen sospechosa y creemos que el precio puede estar ahí.

Nos entregan un fichero, que podéis descargar de [AQUI](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/ldrns.jpg).

Procedemos a revisar que el fichero entregado si sea una imagen:

```console
kali@kali:~/C1b3rChallenge$ file ldrns.jpg 
ldrns.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1,
segment length 16, baseline, precision 8, 225x225, components 3
```

En principio es un fichero de imagen, asi que vamos a ver si dentro de los `strings` encontramos algo:

```console
kali@kali:~/C1berChallenge$ strings -n 8 ldrns.jpg 
!1!%)+...
383-7(-.+
++++++++++++++++++++++++++++++++++++++++++++++++++
vnL6#b`s)
 %`I [p~
{199395pula}
```

Podemos encontrar que hay una cadena de texto que llama la atención, no es algo que se encuentre en los `strings` de un fichero: así que podemos pensar que la flag solicitada es:  ***199395pula***

---
## **RETO 4 - Te quiero a ti**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Un agente infiltrado en la banda de ladrones de coches de lujo ha oído hablar de un nuevo golpe, pero no ha conseguido identificar ni la marca ni el modelo del vehículo objetivo. Por suerte, lo que sí ha conseguido ha sido acceso al móvil de uno de los ladrones, de donde ha podido descargar un archivo comprimido en el que cree que se encuentra la información que buscamos.
>
>En su informe, el agente detalla que no ha sido capaz de descomprimir este archivo, motivo por el que ha solicitado nuestra ayuda.
>
>La solución a este reto es el número de serie del vehículo que pretenden robar los criminales. (*Ten en cuenta que no podemos poner un número de serie real, por lo que cuando encuentres el token quizá no tenga el mismo formato*)

Nos entregan un fichero, que podéis descargar de [AQUI](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/jestesmy_legionem.tar.xz).

Todo parece indicar que es un fichero `tar.gz` aunque con la extensión mal escrita, así que como hemos hecho antes, verificamos si efectivamente tenemos un fichero de compresión.

```console
kali@kali:~/C1berChallenge$ file jestesmy_legionem.tar.xz 
jestesmy_legionem.tar.xz: JPEG image data
```

Para sorpresa, podemos ver que no es un fichero de compresión, es un fichero de imagen.  Así que, podríamos abrirlo con un visor de imágenes o cambiar la extensión y posteriormente abrirlo.  Como lo realicemos, podemos ver que la imagen se visualiza así:

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-4.png)

La imagen esta corrupta, podríamos tratar de restaurarla, a mi me ha funcionado abrir una imagen `JPG` que no este corrupta y verificar la cabecera para que con un editor `HEX` poder cambiar esos valores y tratar de visualizarla. (*Como os he dicho, hay múltiples formas de solucionar este reto*)

Abrimos una pagina que nos permita ver y editar los valores Hexadecimal: [hexed.it/](http://hexed.it/)

Cargamos la imagen y editamos los valores como se muestra:

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-5.png)

Cómo sabemos cuales deberíamos poner? como he indicado antes, si abrimos otra imagen `JPG` que tengamos podemos ver que son similares a las que hemos puesto.

Al hacerlo ya podemos ver la imagen:

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/jestesmy_legionem-Recover-.jpg)

En la parte inferior izquierda, hay una cadena de texto que nos llama la atención.  Probamos para verificar si es la flag que nos piden y obtenemos que es valida: ***PLNDC10010***

---
## **RETO 5 - El jefe final**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Tras meses de jugar al ratón y al gato, por fin hemos logrado desmantelar a gran parte de la banda de ladrones de vehículos de lujo más internacional a la que nos hemos enfrentado. Hemos frustrado muchos de sus intentos de venta he incluso hemos podido anticiparnos para evitar múltiples robos gracias a la lista de vehículos que encontramos gracias a ti.
>
>Esto nos ha colocado en una posición única para acabar con ellos, pero los líderes han adoptado un perfil bajo y no logramos encontrarlos. No podemos permitir que se reagrupen.
>
>En una de las últimas operaciones llevadas a cabo contra la banda conseguimos evitar que destruyeran todos sus discos duros. En uno de ellos encontramos un ejecutable extraño y un fichero jpeg que parece una imagen en blanco. Sabemos que están relacionados de alguna manera porque se encontraban almacenados juntos dentro de una carpeta oculta, pero obviamente no hemos ejecutado el fichero.
>
>Estamos casi seguros de que el plan de huida de la banda se encuentra gracias a estos dos archivos, así que necesitamos que nos digas las coordenadas exactas del escondite de sus líderes.
>
>(*El formato del token serán dichas coordenadas separadas por una coma y sin espacios. Por ejemplo: 40.4167,-3.70325*)

Nos entregan dos ficheros, que podéis descargar de [AQUI](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/jestesmy_legionem.tar.jpg) y [AQUI](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/ZentimoSettings.bin).

Como en el reto anterior, nos entregan un fichero que parece ser un `tar.gz` o un `JPG` (parece que no se han decidido) y nos entregan lo que parecería un binario de Linux.

Vemos si los ficheros son los que aparentan ser:

```console
kali@kali:~/C1berChallenge$ file jestesmy_legionem.tar.jpg 
jestesmy_legionem.tar.jpg: JPEG image data
ch4m0@ch4m0:~/C1berChallenge$ file ZentimoSettings.bin 
ZentimoSettings.bin: Zip archive data, at least v5.1 to extract
```

Vemos que uno de los ficheros es un `JPG` y el otro es un archivo `ZIP`.

Cuando tratamos de descomprimir el fichero `ZIP`, nos solicita una contraseña: según la descripción del reto, parece que podríamos sacar del fichero `JPG`, de alguna manera, la contraseña solicitada.  Así que vamos a intentarlo.

Verificamos si dentro de los `strings` del fichero `JPG` podemos ver algo interesante.

```console
kali@kali:~/C1berChallenge$ strings -n 10 jestesmy_legionem.tar.jpg 
psswdxterm.
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
Y[<Ti WVnwt
fwFFTs,L+A/
MgST\w?B?a
/:6Y-:#/zl
```

Vemos con total claridad una cadena de texto interesante: ***passwdxterm***

Probamos con esta contraseña al descomprimir el otro fichero y no nos la acepta, así que hacemos un poco de "Try Harder" e intentamos solo con la cadena: **xterm**

Con esta si que nos permite descomprimir, observamos que es un fichero `DOCX`, así que verificamos si efectivamente es lo que aparenta ser.

```console
kali@kali:~/C1berChallenge$ file wordlist.docx 
wordlist.docx: RIFF (little-endian) data, WAVE audio, Microsoft PCM,
16 bit, mono 44100 Hz
```

Para nuestra sorpresa, es un fichero de audio `WAV`.  Tendremos que analizarlo para tratar de saber que puede esconder.

Si lo abrimos con `Sonic Visualiser`, podremos escucharlo y ver si observamos algo que no debe estar allí.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-6.png)

No veo nada extraño, aunque parece que el audio es código morse, antes de ir por ese camino, quiero ver si el espectrograma esconde algo, así que selecciono el menú "`Layer`" y posteriormente "`Add Spectogram`"

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-7.png)

Han escondido algunas letras en el espectrograma, seguiré por este camino, vemos que las letras significan números escritos en francés, lo primero que haré es sacar estos nombres y traducirlo.

Texto:
*cinq quatre . cinq neuf trois zero cinq deux virgule un huit . huit un zero trois neuf six*

Traducido:
*cinco cuatro . cinco nueve tres cero cinco dos coma uno ocho . ocho uno cero tres nueve seis (54.593052,18.810396)*

Probamos con el texto integro en Francés o Español y no lo valida: por lo que lo introducimos en números y tenemos nuestra flag: ***54.593052,18.810396***

---
# Fin

Cualquier errata o duda podéis contactar en el grupo de ayuda de esta plataforma. ([Aquí](https://t.me/C1b3rWallAcademy))
