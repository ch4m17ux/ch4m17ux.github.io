# Resolviendo los retos básicos de Atenea (CCN-CERT)

Hemos descubierto la plataforma del *`CCN-CERT`*, llamada [`ATENEA`](https://atenea.ccn-cert.cni.es/challenges).  CCN-CERT significa o son las siglas de *Capacidad de Respuesta a incidentes de Seguridad de la Información del Centro Criptológico Nacional*, adscrito al CNI.

Voy a eliminar los flags, para que os toméis el trabajo de leer la forma de solucionarlo, y por orden de la organización.

## Reto 1 – Hash

### **Enunciado:**

Nos dan una cadena de texto y nos piden que calculemos su hash **`md5`**, tenemos que tener en cuenta que la solución debe ir en el formato: **`flag{md5}`**

>##### Todas las soluciones deben ir en este formato, independiente del resultado obtenido, esto es que siempre daremos la solución con su hash md5.

La contraseña para superar este reto es **LearnTheHashFunction**  

### **Solución:**

La resolución de este primer reto es muy sencilla, bastará con usar el módulo md5 de la librería hashlib de python, para esto creare un script, voy a escribirlo para que me de el formato de la flag que debo introducir como solución:
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-1.png)

Lo ejecutamos y obtenemos la respuesta del primer reto:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-2.png)

---
>He decidido, luego de este reto, crear un script que me permita introducir la cadena de texto que deseo codificar en md5, así me permitirá sacar la flag en el formato que solicita la plataforma.

>![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-3.png)
---

## Reto 2 – Hash 2

#### **Enunciado:**

En este reto nos dan una cadena de texto y nos piden que calculemos su hash **`sha256`** y posteriormente su hash **`md5`** para que como hemos indicado anteriormente podamos introducir la respuesta en el formato que la plataforma exige (*`flag{md5}`*).

La contraseña para superar este reto es ****ThisIsAMoreSecureHashFunction****  

#### **Solución:**

Como en el primer reto, esta solución es bastante sencilla.  Vamos de nuevo con un script en python, que nos permitirá obtener la respuesta; podríamos utilizar algún codificador online y nos dará el mismo resultado.

> He dejado que mi script me muestre como seria la codificación en `SHA256` y la flag en `MD5` que debo introducir.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-4.png)Con este script obtenemos la flag que buscamos:
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-4-1.png)


## Reto 3 – Hash 3

#### **Enunciado:**

En este reto nos dan una cadena codificada en md5 y nos solicitan buscar cual seria su texto correspondiente.

La contraseña para superar este reto es: **54f662a095fa3d5fbbdaac72d176701b**

#### **Solución:**

Hay múltiples forma de solucionar esto reto:

 1. Podríamos utilizar un decodificador online.
 2. Podríamos utilizar hashcat o JohnTheRipper.

Por temas prácticos utilizare un decodificador online:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-5.png)

Posteriormente, nos piden que convirtamos la cadena de texto en mayúsculas, y calculemos su hash md5.  Así que podemos hacerlo manualmente o utilizar un script en python. En este caso utilizare un script que haga justamente esta operación en un solo paso:
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-6.png)Obtenemos la flag que nos piden:
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-7.png)

## Reto 4 – ASCII

#### **Enunciado:**

Nos dan una explicación de los códigos ascii,: Los códigos del 33 al 126 se conocen como caracteres imprimibles, y representan letras, dígitos, signos de puntuación y varios símbolos.  
  
Nos piden encontrar los los caracteres correspondientes a la codificación ASCII que nos entregan:  
  
**080 097 115 115 119 111 114 100 032 112 097 114 097 032 115 117 112 101 114 097 114 032 101 108 032 114 101 116 111 058 032 084 104 101 065 083 067 073 073 084 097 098 108 101 033**

#### **Solución:**

Para solucionar esto, podemos utilizar algún decodificador online o realizarlo con python.  Una de las paginas mas utilizadas para codificar y decodificar es [iCyberchef](http://icyberchef.com/), pero para seguir con el uso de python, lo resolveré asi.

Vamos a ir convirtiendo cada código ascii en letras (char), recorriendo la cadena que nos han dado separando por espacios, para lo cual aprovecharemos la función split.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-8.png)
Lo cual nos da la contraseña o texto que nos piden.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-9.png)
Como he dicho al comienzo, he creado un script para convertir las contraseñas de los retos al formato que solicita el sitio como respuesta, en hash *MD5*.

![Retos Basicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-10.png)

## Reto 5 – Base64

#### **Enunciado:**

En este reto nos dan un fichero txt con una cadena de texto, la cual debemos descodificar y poner la respuesta en el formato que nos solicitan (*`flag{md5-hash}`*)

El contenido del fichero es:

    UmVjdWVyZGEgcXVlIGN1YW5kbyBjb2RpZmljYXMgYWxnbyBlbiBiYXNlNjQgTk8gbG8gZXN0w6Fz
    IGNpZnJhbmRvLCBzaW5vIHF1ZSBzaW1wbGVtZW50ZSBsbyBlc3TDoXMgY29kaWZpY2FuZG8uDQoN
    CkxhIGNvbnRyYXNlw7FhIHBhcmEgc3VwZXJhciBlc3RlIHJldG8gZXM6IHJlY3VlcmRhcXVlYmFz
    ZTY0Tk9lc2NpZnJhcg0KCg==


#### **Solución:**
Podemos utilizar cualquier web que nos descodifique, usar bash o utilizar python.  Mostrare la forma con bash y el resultado en una web.

**Bash:**
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-11.png)

**Web:**
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-12.png)

Calculamos el hash de la respuesta, para dar la respuesta de la flag:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-13.png)

## Reto 6 – Hex

#### **Enunciado:**

En esta ocasión nos dan una cadena que debemos convertir de Hex a Char:

**50617373776f72643a2044346d7054686548337821**

#### **Solución:**
Podemos utilizar una web que nos descodifique la cadena, o realizar un script en python.  Os mostrare ambas opciones.

**Web:**
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-14.png)

**Python**
![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-15.png)

Obtenemos la flag que nos piden:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea/basico-atenea-16.png)

--- 
Esta seria la primera parte de estas soluciones, en el siguiente [`post`](https://ch4m17ux.github.io/2021/01/06/retos-basicos-atenea.html) seguiremos con la segunda parte de estos retos.
