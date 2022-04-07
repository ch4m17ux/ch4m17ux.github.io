
# picoCTF 2022 - Crypto


Durante los dias 17 al 29 de Marzo de 2022, estuvimos participando como el team **H4ck3rT34m** en los retos de **picoCTF**.

En esta ocasion quiero desarrollar algunos retos que pudimos resolver en la categoria de ***Crypto***.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sea reportada para poder subsanarla.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---
## **basic-mod1**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. 
>Download the message [here](https://artifacts.picoctf.net/c/399/message.txt). 
>Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 
>Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`).
>

Nos entregan un fichero que contiene un mensaje, al abrirlo vemos que son una serie de numeros:
```bash
387 248 131 272 373 221 161 110 91 359 390 50 225 184 223 137 225 327 42 179 220 365
```
Siguiendo las instrucciones del reto, nos pone que:

 1. Debemos tomar cada numero entregado y calcular **mod37**
 2. Mapear cada modulo obtenido en un diccionario que se compone:
	 a. Las posiciones *0-25* letras en *mayusculas*.
	 b. Las posiciones *26-35* son *decimales*.
	 c. La posicion *36* es el simbolo "*_*"

De esta forma tenemos nuestro diccionario:
***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"***

Podemos crear un script que nos permita realizar el calculo del modulo a cada numero, y que nos vaya adicionando su resultado en un array convertido en su correspondiente de acuerdo al diccionario.

Con todo esto podemos generar el script para descifrar la flag:

```bash
#!/usr/bin/env python3
#creamos un array con los numeros que nos dan en el mensaje
a = [387,248,131,272,373,221,161,110,91,359,390,50,225,184,223,137,225,327,42,179,220,365]

# Construimos el diccionario, de acuerdo a las instrucciones
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

#Calculamos el modulo de cada numero y su correspondiente valor en el
#diccionario, lo guardamos en un array para imprimir el resultado al 
#final.
b = [alph[i%37] for i in a]
print("picoCTF{"+''.join(b)+"}")
```
Ejecutando el script obtenemos la flag:

```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ python3 calculate-mod.py          
picoCTF{R0UND_N_R0UND_B0D5F596}
```
Encontramos la flag:
***picoCTF{R0UND_N_R0UND_B0D5F596}***

---
## **basic-mod2**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>A new modular challenge! 
>Download the message [here](https://artifacts.picoctf.net/c/505/message.txt). 
>Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 
>Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`.
>
Al igual que en el reto anterior, nos entregan un fichero que contiene un mensaje, al abrirlo vemos que son una serie de numeros:
```bash
145 126 356 272 98 378 395 352 392 215 446 168 180 359 51 190 404 209 185 115 363 431 103
```
Como hemos visto en el reto anterior, debemos seguir las instrucciones que nos dan, para poder resolver el reto:

 1. Debemos tomar cada numero entregado y calcular el inverso modular **mod41**
 2. Mapear cada inverso modular obtenido en un diccionario que se compone:
	 a. Las posiciones *1-26* son las letras del alfabeto en *mayusculas*.
	 b. Las posiciones *27-36* son *decimales*.
	 c. La posicion *37* es el simbolo "*_*"

Tomamos el diccionario que obtuvimos en el reto anterior y lo reutilizamos (son los mismos parametros):
***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"***

Python3 tiene una funcion que nos puede ayudar con este calculo del inverso modular, asi que lo utilizaremos en el script que vamos a contruir como solucion.  Como se explico en el reto anterior, el script realizara los calculos y los va a adicionando a un array de acuerdo al valor correspondiente del diccionario.

Nuestro script para encontrar la flag es:

```bash
#!/usr/bin/env python3
#creamos un array con los numeros que nos dan en el mensaje
a = [145,126,356,272,98,378,395,352,392,215,446,168,180,359,51,190,404,209,185,115,363,431,103]
#Creamos un array vacio, que nos servira para guardar los resultados de la flag.
d = []
m = 41

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for c in a:
	#Calculamos el modulo inverso
    b = pow(c, -1, m)
    #Guardamos los resultado en otro array
    d += alph[b-1]
    
#Imprimimos la flag.
print("picoCTF{"+''.join(d)+"}")
```
Ejecutando el script obtenemos la flag:

```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ python3 calculate-inverse-module.py          
picoCTF{1NV3R53LY_H4RD_374BE7BB}
```
Encontramos la flag:
***picoCTF{1NV3R53LY_H4RD_374BE7BB}***

---
## **credstuff**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? 
>Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar). 
>The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.
>
Este reto es relativamente muy facil, nos entregan un fichero que esta comprimido en `tar`,  al descomprimirlo tenemos dos ficheros txt:

 - usernames.txt
 - passwords.txt

Segun las instrucciones al comparar estos dos ficheros tenemos que la primera linea del fichero de `usernames` su usuario, corresponde a la primera linea del fichero `passwords` y esta seria su contraseña.

Asi que debemos buscar en qué línea tenemos al usuario `cultiris`, y con ellos buscar entre los password dicha linea, alli estara su contraseña.

Abrimos una consola y podemos realizarlo de forma sencilla.  Lo primero seria descomprimir el fichero dado:

```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ tar xvf leak.tar          
leak/
leak/passwords.txt
leak/usernames.txt
```
Buscamos en qué linea esta el usuario solicitado:
```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ grep -n cultiris usernames.txt
378:cultiris
```
Con este numero de linea, vamos al fichero passwords y buscamos que tenemos alli:
```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ sed -n 378p passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}
```
Por ultimo, encontramos que la contraseña esta con algun tipo de cifrado basico, por lo que conociendo que tiene toda la pinta de ser la flag, debe comenzar por `"picoCTF{"`, entre la `p` de la flag y la `c` de la contraseña encontrada, tenemos 13 posiciones, asi que es un `ROT13`.

Haciendo uso de python o de un sitio web lo podemos descrifrar facilmente:
```bash
┌──(root㉿kali)-[~/picoCTF]
└─$ python3
Python 3.8.10
>>> import codecs
>>> secret = 'cvpbPGS{P7e1S_54I35_71Z3}'
>>> msg = codecs.decode(secret, 'rot13')
>>> print(msg)
picoCTF{C7r1F_54V35_71M3}
```
Encontramos la flag:
***picoCTF{C7r1F_54V35_71M3}***

---
## **morse-code**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>Morse code is well known. Can you decrypt this? 
>Download the file [here](https://artifacts.picoctf.net/c/235/morse_chal.wav). 
>Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.
>
Encontramos que nos entregan un fichero de audio, que al reproducirlo tenemos una secuencia de sonidos, como indica el titulo del reto es un audio morse.

Podemos utilizar una web que nos decodifique el audio, por ejemplo: https://morsecode.world/international/decoder/audio-decoder-adaptive.html

Subimos alli el fichero entregado y reproducimos, a medida que va reproduciendo nos va indicando que letras y numeros corresponden en el mensaje:

![morse-code](https://ch4m17ux.github.io/img/posts/picoctf/morse-code.png)

El mensaje obtenido es:
`wh47 h47h 90d w20u9h7`

Ajustando la flag como nos la solicitan, obtenemos:
***picoCTF{wh47_h47h_90d_w20u9h7}***

---
## **rail-fence**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? 
>Download the message [here](https://artifacts.picoctf.net/c/278/message.txt). 
>Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
>
En la descripcion del reto podemos ver una URL de Wikipedia, donde se explica el cifrado. Es muy sencillo de realizar de forma manual, pero por cuestiones de tiempo en el CTF podemos utilizar un decodificar online. 

Asi que teniendo el mensaje entregado:

    Ta _7N6D34hlg:W3D_H3C31N__198ef sHR053F38N43D80 i33___NF

Utilizamos el decodificar online [Cryptii](https://cryptii.com/pipes/rail-fence-cipher)

Obtenemos el mensaje decodificado:

![rail-fence](https://ch4m17ux.github.io/img/posts/picoctf/rail-fence.png)

Asi que la flag buscada es:
***picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_318F0948}***

---
## **substitution0**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? 
>Download the message [here](https://artifacts.picoctf.net/c/385/message.txt).
>
Nos entregan un fichero que corresponde a un mensaje cifrado, por la descripcion del reto, es un cifrado de sustitucion. 

Revisando el mensaje entregado tenemos:
```
PJFRENTZHOMQKLAIUVSWCYDXGB 

Zevecial Qetvplr pvase, dhwz p tvpye plr swpweqg phv, plr jvactzw ke wze jeewqe
nvak p tqpss fpse hl dzhfz hw dps elfqaser. Hw dps p jepcwhncq sfpvpjpecs, plr, pw
wzpw whke, clmladl wa lpwcvpqhsws—an facvse p tvepw ivhbe hl p sfhelwhnhf iahlw
an yhed. Wzeve deve wda vaclr jqpfm siaws lepv ale exwvekhwg an wze jpfm, plr p
qalt ale lepv wze awzev. Wze sfpqes deve exfeerhltqg zpvr plr tqassg, dhwz pqq wze
piiepvplfe an jcvlhszer taqr. Wze dehtzw an wze hlsefw dps yevg vekpvmpjqe, plr,
wpmhlt pqq wzhlts hlwa falshrevpwhal, H facqr zpvrqg jqpke Ocihwev nav zhs aihlhal
vesiefwhlt hw.

Wze nqpt hs: ihfaFWN{5CJ5717C710L_3Y0QC710L_N96P338E}
```
En la pista que nos entregan, nos refieren a tratar de romper el cifrado con un analisi de frecuencia de las letras, podemos encontrar varias herramientas que nos ayudan para esto, Utilizamos el decodificar online [Cryptii](https://cryptii.com/pipes/alphabetical-substitution)

Obtenemos el mensaje decodificado:

![substitution0](https://ch4m17ux.github.io/img/posts/picoctf/substitution0.png)

Asi que la flag buscada es:
***picoCTF{5UB5717U710N_3V0LU710N_F96A338E}***

---
## **substitution1**

Nos entregan la descripción del reto:

> ***DESCRIPCION***:
> 
>A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. 
>Download the message [here](https://artifacts.picoctf.net/c/420/message.txt).
>
Como en el reto anterior, nos entregan un fichero que corresponde a un mensaje cifrado, por la descripcion del reto, muy similar al anterior. 

Revisando el mensaje entregado tenemos:
```
PJFRENTZHOMQKLAIUVSWCYDXGB 

DAFq (qgjwa fjw dkxahwz agz frke) kwz k aoxz jf djbxhazw qzdhwtao djbxzatatjn. 
Djnazqaknaq kwz xwzqznazs mtag k qza jf dgkrrznezq mgtdg azqa agztw dwzkatltao, 
azdgntdkr (kns ejjertne) qutrrq, kns xwjyrzb-qjrltne kytrtao. Dgkrrznezq hqhkrro 
djlzw k nhbyzw jf dkazejwtzq, kns mgzn qjrlzs, zkdg otzrsq k qawtne (dkrrzs k 
frke) mgtdg tq qhybtaazs aj kn jnrtnz qdjwtne qzwltdz. DAFq kwz k ewzka mko aj 
rzkwn k mtsz kwwko jf djbxhazw qzdhwtao qutrrq tn k qkfz, rzekr znltwjnbzna, kns 
kwz gjqazs kns xrkozs yo bkno qzdhwtao ewjhxq kwjhns agz mjwrs fjw fhn kns 
xwkdatdz. Fjw agtq xwjyrzb, agz frke tq: 
xtdjDAF{FW3VH3NDO_4774DU5_4W3_D001_3645YZD6}
```
Como en el reto anterior, tenemos multiples herramientas online que rompen el cifrado, asi que por ejemplo tenemos:

 - https://www.guballa.de/substitution-solver
 - https://quipqiup.com/

Utilizando el primero obtenemos el mensaje decodificado:

![substitution1](https://ch4m17ux.github.io/img/posts/picoctf/substitution1.png)

Asi que la flag buscada es:
***picoCTF{FR3QU3NCY_4774CK5_4R3_C001_3645BEC6}***


----------
# Fin