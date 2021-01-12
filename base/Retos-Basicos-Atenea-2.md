# Resolviendo los retos básicos de Atenea (CCN-CERT) 

En un [post anterior](https://ch4m17ux.github.io/2021/01/06/retos-basicos-atenea.html) estuve presentando la resolucion de los retos basicos de Atenea, en esta segunda entrega continuare con algunas retos mas, y quiza nos alcance para realizar una tercera entrega.

Como en el post anterior, voy a eliminar los flags, para que os toméis el trabajo de leer la forma de solucionarlo, y por orden de la organización.

## Reto 7 – XOR

### **Enunciado:**

Voy a copiar el enunciado que se tiene en la plataforma para poder comprender mejor lo que se nos pide:

>Una cadena de texto puede ser cifrada aplicando el operador de bit XOR sobre cada uno de los caracteres utilizando una clave. Para descifrar la salida, sólo hay que volver a aplicar el operador XOR con la misma clave.

Debemos utilizar la clave **encryptXOR** 

Para descifrar el siguiente mensaje:  
  
**UGFzc3dvcmQ6IHhvFzYMACEfBiAgIA==**

### **Solución:**

En este caso vemos que la contraseña a descifrar esta en *`Base64`*; asi que, debemos decodificarlo en este hash y posteriormente convertirlo a Hexadecimal.  La clave tambien la convertimos a hexadecimal y podemos utilizar una web que nos permita calcular bit a bit la respuesta. Para este reto utilizare la web [XOR Calculator](http://xor.pw).

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-1.png)

Convertimos la respuesta de *`Hex`* a *`ASCII`*, y obtenemos:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-2.png)

También podríamos resolver este reto con un script de python:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-3.png)

Que nos da la misma respuesta que conseguimos con la web.  Finalmente, convertimos la respuesta en el formato de la flag:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-4.png)
## Reto 8 – Entropy

### **Enunciado:**
Nos dan una serie de imágenes y nos piden que calculemos la entropía de cada uno de ellos, y la solución es el nombre del fichero con mayor entropía, incluyendo la extensión (*por ejemplo: imagen25.jpg*).

### **Solución:**

Dentro de la explicación y las referencias que nos dan en el reto, podemos ver que hay un sitio donde encontramos un script en Python que nos calcula la entropía[ \[Aquí\]](https://kennethghartman.com/calculate-file-entropy/), así que lo tomaremos como base y haremos algunas modificaciones para que recorra el directorio, compare la entropía de cada fichero y nos muestre solo el que tenga la mayor.  También que ese nombre lo convierta en el formato de la flag de la plataforma.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-5.png)

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-6.png)
## Reto 9 – Magic Number

### **Enunciado:**
En esta ocasión nos dan un fichero sin extensión; debemos buscar cual es su "*`número mágico`*" o "*`file signature`*", expresado en mayúsculas.

### **Solución:**

Para dar solución podemos hacer uso de la consola de linux y utilizar **`xxd`**, que nos da los números mágicos del fichero, también podemos hacer uso de **`file`**, para saber de que fichero se trata.

Teniendo la primera fila de los *números mágicos* que tiene el fichero podemos calcular la flag solicitada.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-7.png)
## Reto 10 – Strings

### **Enunciado:**
Para este reto se nos ha dado un fichero que según se indica es un *`binario`*, y nos piden que revisemos dentro de los ***`strings`*** del mismo a que URL se esta intentando conectar.

### **Solución:**

Para poder dar solución a este reto, basta con buscar con el comando ***`strings`*** (para que nos muestre las posibles "*palabras legibles*") y filtrar por la cadena que buscamos; en este caso algo similar a ***www***.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-8.png)
## Reto 11 – Metadatos

### **Enunciado:**
Nos dan un fichero ***PDF***, del cual debemos buscar quien es el autor.

### **Solución:**
Este reto es muy sencillo, debemos utilizar ***`exiftool`*** para poder ver sus metadatos y buscar la información que nos solicitan.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-9.png)
## Reto 12 – Metadatos 2

### **Enunciado:**
Nos dan un fichero ***JPG***, del cual debemos averiguar el modelo de la cámara con la que se tomó la fotografía (la solución es sólo el modelo, sin incluir la marca, y todo en mayúsculas)

### **Solución:**
La solución al igual que en el reto anterior, es utilizar exiftool para buscar la información que nos están pidiendo.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-10.png)

---
Con esto finalizamos con la segunda entrega. En el siguiente post finalizaremos con los retos básicos de Atenea.

Si desea ver la primera sección de retos, puedes ir a este ***`[enlace](https://ch4m17ux.github.io/2021/01/06/retos-basicos-atenea.html)`***
