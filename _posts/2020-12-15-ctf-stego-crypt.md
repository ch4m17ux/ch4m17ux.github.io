---
layout: post
title: "CTF Stego/Crypt"
subtitle: "#ProyectoAurora"
date: 2020-12-15 23:45:13 +0100
background: '/img/posts/06.jpg'
---

# CTF Stego/Crypt

Durante los días del 10 al 12 de Diciembre de 2020, estuvimos participando como equipo (**L4r0_134W Team**) en el CTF organizado por [Proyecto Aurora](https://www.proyecto-aurora.org/).

En este CTF encontramos un reto correspondiente al grupo de Stego/Crypt, donde nos entregaban dos archivos:

>- Un fichero PDF con una imagen de los continentes.
>- Un fichero ZIP que esta bloqueado a traves de una contraseña.

Inicialmente tratamos de romper la contraseña del ZIP a traves de `Zip2John`, pero encontramos que no hay forma de crackearla, por lo que la clave debe estar en el PDF, por esta razón, trataremos a traves de tecnicas de estenografía obtener la informacion embebida en el fichero PDF y conseguir la contraseña para descomprimir el fichero ZIP.

Lo primero que debemos hacer es verificar los `"Magic Numbers"` del fichero PDF, puede que realmente no sea un fichero real y se enmascare con otro, por lo que a traves de un editor Hex verificamos la informacion, y encontramos que coincide con lo correspondiente a un PDF real:

| 25 50 44 46 2D | %PDF |
|--|--|
|  |  |

Posteriormente procedemos a verificar si dentro de los strings del fichero vemos algun mensaje o codigo oculto:

```sh
root@kali:$ strings -n 10 Donde_Estoy.pdf 
<</Filter/FlateDecode/Length 44>>
<</Subtype/Image/BitsPerComponent 8/Width 1024/Interpolate true/ColorSpace/DeviceRGB/Height 576/Filter[/DCTDecode]/Type/XObject
/Length 71706>>
'9=82<.342
!22222222222222222222222222222222222222222222222222
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
I_^2sHp[qbGLR
<</First 35/Filter/FlateDecode/N 6/Type/ObjStm/Length 243>>
<</Filter/FlateDecode/Root 2 0 R/Info 12 0 R/Size 25/W[1 3 1]/Type/XRef/Length 53>>
"H4sIAO+3wl8A/wVAyQkAIAxbxRWCfoX67xKiXw8SwfXL7dI/nDW1lYlhXh62BQDOV0cXAAAA"
```
Encontramos que tenemos una sencuencia alfanumerica que podria ser algun texto cifrado:
>***H4sIAO+3wl8A/wVAyQkAIAxbxRWCfoX67xKiXw8SwfXL7dI/nDW1lYlhXh62BQDOV0cXAAAA***

Procedemos con alguna herramienta a tratar de descifrarlo, para este caso hemos usado [**iCyberchef**](http://icyberchef.com/).  Y nos indica que es una cadena con doble cifrado: `Base64`  y `Gunzip`.  Resultando la contraseña que necesitamos para descomprimir el fichero ZIP que nos han entregado.

> password= Am3r1c@L4t1n@

![iCyberchef - Decode string](https://ch4m17ux.github.io/img/posts/stego-1.jpg)

Procedemos a descomprimir el ZIP y nos da como resultado dos nuevos ficheros: 
>- Un fichero JPG con una imagen de America.
>- Un fichero ZIP que esta bloqueado a traves de una contraseña.

Tomamos la imagen y trataremos de descifrar el mensaje oculto, que nos dara la contraseña con la qué descomprimir el fichero ZIP.

Analizando el fichero JPG 

