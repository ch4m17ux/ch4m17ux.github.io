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
## Reto 8 – XOR

### **Enunciado:**
Nos dan una serie de imágenes y nos piden que calculemos la entropía de cada uno de ellos, y la solución es el nombre del fichero con mayor entropía, incluyendo la extensión (*por ejemplo: imagen25.jpg*).

### **Solución:**

Dentro de la explicación y las referencias que nos dan en el reto, podemos ver que hay un sitio donde encontramos un script en Python que nos calcula la entropía[ \[Aquí\]](https://kennethghartman.com/calculate-file-entropy/), así que lo tomaremos como base y haremos algunas modificaciones para que recorra el directorio, compare la entropía de cada fichero y nos muestre solo el que tenga la mayor.  Tambien que ese nombre lo convierta en el formato de la flag de la plataforma.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-5.png)

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-6.png)
## Reto 9 – Magic Number

### **Enunciado:**
En esta ocasión nos dan un fichero sin extensión; debemos buscar cual es su "*`numero mágico`*" o "*`file signature`*", expresado en mayúsculas.

### **Solución:**

Para dar solución podemos hacer uso de la consola de linux y utilizar **`xxd`**, que nos da los números mágicos del fichero, también podemos hacer uso de **`file`**, para saber de que fichero se trata.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-2-7.png)
