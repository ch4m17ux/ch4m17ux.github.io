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

Con todo estopodemos generar el script para descifrar la flag:

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
***picoCTF{R0UND_N_R0UND_B0D5F596}***

----------
# Fin