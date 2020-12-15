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

![Ficheros PDF y ZIP](https://ch4m17ux.github.io/img/posts/Donde_Estoy.jpg)

Inicialmente tratamos de romper la contraseña del ZIP a traves de `Zip2John`, pero encontramos que no hay forma de crackearla, por lo que la clave debe estar en el PDF, por esta razón, trataremos a traves de tecnicas de estenografía obtener la informacion embebida en el fichero PDF y conseguir la contraseña para descomprimir el fichero ZIP.

Lo primero que debemos hacer es verificar los `"Magic Numbers"` del fichero PDF, puede que realmente no sea un fichero real y se enmascare con otro, por lo que a traves de un editor Hex verificamos la informacion, y encontramos que coincide con lo correspondiente a un PDF real:

| 25 50 44 46 2D |  |  %PDF |
|--|--|--|
|  |  |  |

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

![Ficheros JPG y ZIP](https://ch4m17ux.github.io/img/posts/Que_Pais.jpg)
Tomamos la imagen y trataremos de descifrar el mensaje oculto, que nos dara la contraseña con la qué descomprimir el fichero ZIP.

Analizamos el fichero JPG y vemos que los magic numbers corresponden:

| FF D8 FF E1 |  |  %JPG |
|--|--|--|
|  |  |  |

Verificamos con `binwalk` sin hay alguna imagen que podria estar embebida, y encontramos que hay alguna imagen mas que podria estar alli:

```sh
    root@kali:~/Descargas/CTF-ProyectoAurora/Stego-Crypt/Donde_Estoy$ sudo binwalk Que_Pais.jpg 
    
    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             JPEG image data, EXIF standard
    12            0xC             TIFF image data, big-endian, offset of first image directory: 8
    184           0xB8            JPEG image data, EXIF standard
    196           0xC4            TIFF image data, big-endian, offset of first image directory: 8
```

Utilizamos entonces `exiftool` para ver si vemos algo mas:

```sh
    root@kali:~/Descargas/CTF-ProyectoAurora/Stego-Crypt/Donde_Estoy$ sudo exiftool Que_Pais.jpg 
    ExifTool Version Number         : 12.10
    File Name                       : Que_Pais.jpg
    Directory                       : .
    File Size                       : 3.7 MB
    File Modification Date/Time     : 2020:11:29 03:05:10+01:00
    File Access Date/Time           : 2020:12:15 20:28:31+01:00
    File Inode Change Date/Time     : 2020:12:12 18:08:19+01:00
    File Permissions                : rw-r--r--
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    Warning                         : [minor] File contains multi-segment EXIF
    Exif Byte Order                 : Big-endian (Motorola, MM)
    X Resolution                    : 72
    Y Resolution                    : 72
    Resolution Unit                 : inches
    Y Cb Cr Positioning             : Centered
    Compression                     : JPEG (old-style)
    Thumbnail Offset                : 184
    Thumbnail Length                : 3755286
    DCT Encode Version              : 100
    APP14 Flags 0                   : [14], Encoded with Blend=1 downsampling
    APP14 Flags 1                   : (none)
    Color Transform                 : YCbCr
    Image Width                     : 938
    Image Height                    : 898
    Encoding Process                : Baseline DCT, Huffman coding
    Bits Per Sample                 : 8
    Color Components                : 3
    Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
    Image Size                      : 938x898
    Megapixels                      : 0.842
    Thumbnail Image                 : (Binary data 3755286 bytes, use -b option to extract)
```

Podemos ver que nos da la posibilidad de obtener una imagen Thumbnail

>Thumbnail Image                 : (Binary data 3755286 bytes, use -b option to extract)

Procedemos a sacar la imagen:

```sh
    root@kali: exitftool -b --ThumbnailImage Que-Pais.jpg > my_thumbnail.jpg
```

![Estadio Manaos Brasil](https://ch4m17ux.github.io/img/posts/Estadio-Stego-Aurora.jpg)

Verificamos los strings de la imagen que hemos sacado, para ver si podemos identificar alguna cadena de texto o algun codigo encriptado:

	strings -n 10 my_thumbnail.jpg

Encontramos una secuencia interesante:

```sh
    ch4m0@kali:~/Descargas/CTF-ProyectoAurora/Stego-Crypt/Donde_Estoy$ strings -n 10 my_thumbnail.jpg
        A=4 I=1 S=5 B=8
        %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
        &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
        O1a%CuTl+s
```

>A=4 I=1 S=5 B=8

Identificamos que el estadio de la miniatura esta en Brasil, asi que procedemos a reemplazar las letras con la secuencia que nos han dado, lo cual resulta: 
>Brasil - 8r451l

Con esta clave descomprimimos el zip que nos sacamos de los pasos anteriores y, vemos que contiene una imagen y una fichero TXT.

![enter image description here](https://ch4m17ux.github.io/img/posts/Que_Ciudad.jpg)

La imagen es del Cristo Redentor de Rio de Janeiro (Brasil) y el fichero TXT nos da algunas instrucciones: 

        ..,.,,,....                                                      
                     #&  .&(                 ,(#&@@&#,                                        
                       %%  ,@/                         ,#&@#.                                 
                        ,@.  #&                              ,%@#.                            
      @&&&&&&&&&&&&&&&&&&&&&&&&&.                                .%@/                         
                           &,  .&.                                   (@/                      
                           .@   /&                                      &&                    
                            %%   &/                                       %&                  
                            ,@   (%      ULTIMO PASO!!!                    &%                
                            .@   /%      DECIFRA LA FLAG                   *&&@@@@@@@@@@@@. 
                            .@   (#                                         &%                
                            (%   &*                                       %&                  
                            @.  (%                                      &&                    
                           &#  ,&                                    #&*                      
      @&&&&&&&&&&&&&&&&&&&&&&&&&.                                 %@/                         
                         &(  (&                              .#@%.                            
                       *@.  @#                          ,%@&/                                 
                      &(  %&.                ..,/%&&&#*                                       
                               .,*********.                                                   
    
    FLAG= ProyectoAurora{71,!)//: I&=3+..*J1!7I1 <:*#0#3N)(R)>((n#/-'& &.1  * 9@ODc4#3.RDV_5^<6A!-;^T:.R1/]<\C;_}
	
	
Asi que, lo que debemos hacer es realizar un `XOR`, por descarte entre las palabras "Cristo Redentor" y "Rio de Janeiro" probamos a hacer un XOR a la clave que nos han dado, pero utilizamos la de la ciudad (que es el nombre de los ficheros)

Realizando esta operación nos da la flag que andábamos buscando.

![enter image description here](https://ch4m17ux.github.io/img/posts/rio-de-janeiro.jpg)
>***flag{35T0Y_3N_R10_D3_J4N31R0}***

## FIN
