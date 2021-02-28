# C1b3rwall Challenge: Retos Rookie

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-1.png)

En este post quiero traer los retos que la plataforma C1b3rwall Challenge, de la mano de Hacroks nos presenta.  En esta oportunidad desarrollare los correspondientes al nivel Básico o Rookie.

Si quieres participar tienes información [ [Aquí](https://c1b3rwall.hackrocks.com/) ]

---

## **RETO 1 - Mensaje Interceptado**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Acaba de recibir un mensaje que ha sido interceptado por una organización extranjera. Sin embargo resulta incomprensible. ¿Podrá averiguar su contenido?
> 
> Su investigación comienza con un breve mensaje que ha sido interceptado sin tener más conocimiento sobre el mismo. Parece totalmente incomprensible, pero confiamos en usted para encontrarle un sentido.
>
>**QV9mMXJzdF9zdDNw**

Vemos claramente que el mensaje esta encriptado; por esta razón lo pasaremos por una herramienta que nos identifique que tipo de cifrado tiene y que nos entregue el string en claro.

Para esta operación, podemos utilizar la herramienta online [Cyberchef](https://gchq.github.io/CyberChef).

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-2.png)
Y así, obtenemos la solución al primer reto.

---
## **RETO 2 - Status Report**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Un agente necesita recibir un mensaje. ¿Podrá enviárselo?
> 
> Un agente se encuentra en una misión encubierta. Tenemos un canal de comunicación seguro; sin embargo, este agente tiene una costumbre adquirida por su formación en el MD5 y requiere un formato adicional de mensaje. ¿Podrá enviarle el siguiente mensaje de forma que él lo entienda?.
>
>****reporte status****

El reto nos indica que el agente se comunica a través de mensajes en formato MD5, es por esto, que debemos cifrar el mensaje como nos indican.

De nuevo, para resolver este reto podemos hacer uso de CyberChef.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-3.png)

Obtenemos la solución solicitada.

---
## **RETO 3 - ¿Indescifrable?**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Extraño archivo de texto el que hemos encontrado. ¿Qué será ese texto incompresible?
> 
> Durante la monitorización que tiene asignada como agente, intercepta un texto que se está volviendo viral. Sin embargo, parece que el mismo no tiene sentido alguno. Su misión será averiguar su sentido antes de que sea demasiado tarde.

Dentro de la descripción tenemos un fichero txt ([Aquí](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/indescifrable.txt)), a simple vista es indescifrable, no sabemos que contiene, ni a que pertenece; así que seguimos utilizando la herramienta de CyberChef y veremos que nos arroja.  Cuando no sabemos en qué cifrado esta el texto que nos han entregado, y la herramienta identifica de que se trata, nos saldrá una "varita" que al darle clic descifra lo que estamos introduciendo.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-4.png)

Obtenemos una imagen donde nos entrega la flag que debemos introducir.

---
## **RETO 4 - No estamos solos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Acabamos de interceptar una extraña señal procedente del espacio
> 
> Como agente asiste a una reunión de urgencia a la que asisten todas las agencias de inteligencia de la Unión Europea. En ella se le facilita un archivo de audio, el cual contiene una señal que ha sido interceptada por la estación espacial internacional. ¿Qué misterio oculta?
>
>(Ten en cuenta que el token diferencia entre mayúsculas y minúsculas. Buscamos el mensaje entero en minúsculas)

Dentro de la descripción nos entregan un fichero de audio ([Aquí](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/audio-cat.wav)).

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-5.png)

Verificamos que el fichero si sea lo que nos dicen que es. (un archivo de audio)

```console
kali@kali:~/C1b3rChallenge$ file signal_from_outer_space.wav 
signal_from_outer_space.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 11050 Hz
```

Corresponde con lo que nos indican que debe ser.  Procedemos de esta forma a abrirlo con cualquier reproductor.

Al escucharlo, podemos identificar que es un código morse, así que si tenemos experiencia en código morse, podemos traducirlo; o utilizar una herramienta que nos traduzca los pulsos.

Utilizare para esto una pagina web denominada "[Morse Code Adaptive Audio Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)", subimos el audio allí y la herramienta nos lo pone en texto claro.

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/rookie-6.png)
Nos han dicho en la descripción, que la respuesta debe ser en minúsculas, así que obtenemos: ***miau miau cat invasion***

---

## **RETO 5 - No estamos solos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> Una imagen viral sin sentido ¿o quizás sí?
> 
> Han transcurrido tan sólo unas horas desde que se ha interpretado el mensaje de audio captado por la estación espacial internacional y ahora parece que se ha vuelto viral una extraña imagen. Parece no tener sentido pero debemos sacar toda la información posible de la misma.

Nos entregan un fichero gif:

![Retos C1b3rwall Challenge](https://ch4m17ux.github.io/img/posts/c1berwall-challenge-rookie/cat.gif)
Como siempre, lo primero es verificar que la imagen es realmente lo que dice que es:

```console
kali@kali:~/C1b3rChallenge$ file what_the_gif.gif 
what_the_gif.gif: GIF image data, version 89a, 480 x 480
```
Observamos que efectivamente es un fichero gif.  Procedemos a verificar los strings que pueda traer.

```console
kali@kali:~/C1b3rChallenge$ strings -n 20 what_the_gif.gif 
5358%!86;95698>:<D@<<A*$A0-A68A=?B*,B>CD4.D:6EBDEITFDHFFMFN]N2/N:6NGHNJNO=9PPYQC>QNSTXcU]lWVZX<:XC>XQUXcuYG9YLKZHG[L@]WY^\b`EB`LC`dqaQDaQQc]ceKGeQHfWPfZXfcfgVDhlwhp
n``nmtpNKpXHpXPq@MqZVsaHtgct
ur}vaPvcVvjnvqww`_wpqwy
n0th1ng h3r3, try harder
c4ts_is_com1ng_3nd3r____vipyne
```
Observamos que hay una cadena de texto que resalta, no es algo que este comúnmente en ficheros de todo estilo: ***c4ts_is_com1ng_3nd3r***

Obtenemos nuestra flag solicitada.

# Fin
Cualquier errata o duda podéis contactar en el grupo de ayuda de esta plataforma. ([Aquí](https://t.me/C1b3rWallAcademy))
