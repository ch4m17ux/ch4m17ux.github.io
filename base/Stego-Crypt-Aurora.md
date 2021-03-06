--- layout: post title: "CTF Stego/Crypt" 
subtitle: "\#ProyectoAurora"
date: 2020-12-15 23:45:13 +0100 
background: '/img/posts/06.jpg' 
---


# CTF Stego/Crypt
---

Durante los días del 10 al 12 de Diciembre de 2020, estuvimos participando como equipo (**L4r0\_134W Team**) en el CTF organizado por [Proyecto Aurora](https://www.proyecto-aurora.org/).

En este CTF encontramos un reto correspondiente al grupo de Stego/Crypt, donde nos entregaban dos archivos:

> -   Un fichero PDF con una imagen de los continentes.
> -   Un fichero ZIP que esta bloqueado a traves de una contraseña.

![Ficheros PDF y ZIP](https://ch4m17ux.github.io/img/posts/Donde_Estoy.jpg)

Inicialmente tratamos de romper la contraseña del ZIP a traves de `Zip2John`, pero encontramos que no hay forma de crackearla, por lo que la clave debe estar en el PDF, por esta razón, trataremos a traves de tecnicas de estenografía obtener la informacion embebida en el fichero PDF y conseguir la contraseña para descomprimir el fichero ZIP.

Lo primero que debemos hacer es verificar los `"Magic Numbers"` del fichero PDF, puede que realmente no sea un fichero real y se enmascare con otro, por lo que a traves de un editor Hex verificamos la informacion, y encontramos que coincide con lo correspondiente a un PDF real:

  25 50 44 46 2D      %PDF
  ---------------- -- ------
                      
Posteriormente procedemos a verificar si dentro de los strings del fichero vemos algun mensaje o codigo oculto:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code1-ctf-stego.png)

Encontramos que tenemos una sencuencia alfanumerica que podria ser algun texto cifrado:

> ***H4sIAO+3wl8A/wVAyQkAIAxbxRWCfoX67xKiXw8SwfXL7dl/nDW1lYlhXh62BQDOV0cXAAAA***

Procedemos con alguna herramienta a tratar de descifrarlo, para este caso hemos usado [**iCyberchef**](https://gchq.github.io/CyberChef/). 

Cuando copiamos la cadena de texto podemos ver que se activa una "varita" que nos sugiere que tiene un cifrado `Base64`.

![iCyberchef - Decode string](https://ch4m17ux.github.io/img/posts/stego-0-1.jpg)

Posteriormente esta misma "varita" nos indica que presuntamente el resultado esta cifrado en `Gunzip`.

![iCyberchef - Decode string](https://ch4m17ux.github.io/img/posts/stego-0-2.jpg)

Con lo cual podemos resumir que la herramienta online nos indica que es una cadena con doble cifrado: `Base64` y `Gunzip`. Resultando la contraseña que necesitamos para descomprimir el fichero ZIP que nos han entregado.

> password= Am3r1c@L4t1n@

![iCyberchef - Decode string](https://ch4m17ux.github.io/img/posts/stego-1.jpg)

Procedemos a descomprimir el ZIP y nos da como resultado dos nuevos ficheros:

> -   Un fichero JPG con una imagen de America.
> -   Un fichero ZIP que esta bloqueado a traves de una contraseña.

![Ficheros JPG y ZIP](https://ch4m17ux.github.io/img/posts/Que_Pais.jpg)

Tomamos la imagen y trataremos de descifrar el mensaje oculto, que nos dara la contraseña con la qué descomprimir el fichero ZIP.

Analizamos el fichero JPG y vemos que los magic numbers corresponden:

  FF D8 FF E1      %JPG
  ------------- -- ------
                   

Verificamos con `binwalk` sin hay alguna imagen que podria estar embebida, y encontramos que hay alguna imagen mas que podria estar alli:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code2-ctf-stego.png)

Utilizamos entonces `exiftool` para ver si vemos algo mas:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code3-ctf-stego.png)

Podemos ver que nos da la posibilidad de obtener una imagen Thumbnail

> Thumbnail Image : (Binary data 3755286 bytes, use -b option to extract)

Procedemos a sacar la imagen:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code4-ctf-stego.png)

![Estadio Manaos Brasil](https://ch4m17ux.github.io/img/posts/Estadio-Stego-Aurora.jpg)

Verificamos los strings de la imagen que hemos sacado, para ver si podemos identificar alguna cadena de texto o algun codigo encriptado:

    strings -n 10 my_thumbnail.jpg

Encontramos una secuencia interesante:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code5-ctf-stego.png)

> A=4 I=1 S=5 B=8

Identificamos que el estadio de la miniatura esta en Brasil, asi que procedemos a reemplazar las letras con la secuencia que nos han dado, lo cual resulta:

> Brasil - 8r451l

Con esta clave descomprimimos el zip que nos sacamos de los pasos anteriores y, vemos que contiene una imagen y una fichero TXT.

![enter image description here](https://ch4m17ux.github.io/img/posts/Que_Ciudad.jpg)

La imagen es del Cristo Redentor de Rio de Janeiro (Brasil) y el fichero TXT nos da algunas instrucciones:

![codigo linux ctf](https://ch4m17ux.github.io/img/posts/code6-ctf-stego.png)

Asi que, lo que debemos hacer es realizar un `XOR`, por descarte entre las palabras “Cristo Redentor” y “Rio de Janeiro” probamos a hacer un XOR a la clave que nos han dado, pero utilizamos la de la ciudad (que es el nombre de los ficheros)

Realizando esta operación nos da la flag que andábamos buscando.

![Decode String](https://ch4m17ux.github.io/img/posts/rio-de-janeiro.jpg)

> ***flag{35T0Y\_3N\_R10\_D3\_J4N31R0}***


Y de esta forma finalizamos el reto que se nos ha presentado.

FIN 
---
