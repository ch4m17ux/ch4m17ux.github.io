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
ch4m0@ch4m0:~/Descargas/C1b3rChallenge$ unzip net.pcap
Archive:  net.pcap
  inflating: trace/tlhahisoleseding  
  ```

Obtenemos una carpeta con un binario que podríamos ejecutar. Al hacerlo vemos que hay una cadena de texto que se repite.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-1.png)
Por lo que lo anterior podemos sacar la cadena de texto:

```console
uggcf://jjj.qebcobk.pbz/f/qtdipont5zsxygp/p1o3epunyyratr.mvc?qy=1|Wejdź na naszą uzgodnioną witrynę
```

Que si la ponemos en CyberChef y jugamos haber que tipo de cifrado tiene, encontramos:

```console
https://www.dropbox.com/s/dgqvcbag5mfkltc/c1b3rchallenge.zip?dl=1|Jrwqź an anfmą hmtbqavbaą jvgelaę
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

Nos entregan un fichero como indica la descripción. [Lo puedes descargar [AQUI\]
](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/dotyczysamochodow.pdf)

Al parecer es un fichero `PDF`, asi que vamos a ver si se esconde algo dentro o podemos sacar algo que pueda estar oculto.

Lo primero que podemos hacer es buscar dentro de los strings del fichero, puede que haya alguna cadena de texto interesante.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-advanced/advanced-2.png)
Observamos que hay una cadena de texto al final que parece ser un `Base64`, asi que vamos a verificar que nos arroja.