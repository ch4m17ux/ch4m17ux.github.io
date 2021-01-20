# OverPass3 - Hosting (Writeup - TryHackMe) 

![Reto Overpass3 - TryHackMe](https://ch4m17ux.github.io/img/posts/overpass3/tryhackme-overpass3.jpg)

> *En esta maquina se nos indica que debemos lanzar la maquina y esperar a que inicie, tardara cerca de 5 minutos, de otro modo no podremos acceder a la misma.  Se ha establecido que la maquina tenga un nivel intermedio de expertiz, y esta bien denominada, ya que hay que trabajar un poco para poder escalar privilegios, las vulnerabilidades para poder hacerlo solo podran ser explotadas casi al final del desarrollo de la misma*.

## Recoleccion de informacion

Como generalmente creo que se deberia comenzar, es realizando un un escaneo de puertos; asi podremos saber que puertos abiertos tiene la maquina y poder tener un panorama general de los pasos a realizar.

### NMAP

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-1.png)

Podemos ver que tenemos 3 puertos abiertos:
> - 21
 >- 22
 >- 80
 
Asi que vamos a seguir recolectando información. Ya que tenemos un sitio web, verificamos si podemos ver algo dentro del sitio, dentro del codigo fuente y demas.  Lo mas interesante de reseñar es que tenemos algunos nombres que nos podrian ayudar a tratar de probar accesos a traves de SSH o algun administrador del sitio que pueda tener, asi que tomamos nota:

>* Paradox
>* Elf
>* MuirlandOracle
>* NinjaJc01

Vamos a ejecutar un escaneo de directorios sobre el sitio web, verificamos si encuentra alguna zona de administracion o similar.

### Gobuster

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-2.png)

Observamos que nos ha encontrado un directorio interesante (`/backups`), ya que no es comun que se tenga en un sitio web.  Al verificar este directorio encontramos que tiene un fichero `ZIP`, que nos lo descargaremos y verificaremos que contiene.

PONER IMAGEN DEL SITIO WEB

Una ves que lo hemos descargado encontramos que hay dos ficheros: 

> * Un fichero excel encriptado con `GPG`
> * Una llave que suponemos que seria la que nos permita descencriptar el fichero.


![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-3.png)

Lo que debemos hacer primero es importar esta llave que hemos obtenido (y que seguro nos vendra muy bien)

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-4.png)
Posteriormente desencriptamos el fichero excel encriptado.

![OverPass3 - WriteUp](https://ch4m17ux.github.io/img/posts/overpass3/overpass3-5.png)
Obtenemos un fichero excel que podemos visualizar, bien sea con algun editor que tengas en tu maquina (*como `LibreOffice`*) o utilizar un visor online.  De un modo u otro, podremos ver que hay una tabla con algunos datos interesantes: Nombre de Cliente, **Nombre de Usuario**, **Contraseña**, Numero de tarjeta de credito y CVC (*No os emocioneis, los numeros de tarjeta no son validos*).  Verificaremos si con estos datos podemos acceder via `SSH`.

| Customer Name | Username |Password |Credit card number | CVC|
|--|--|--|--|--|
| Par. A. Doxx | paradox | ShibesAreGreat123 | 4111 1111 4555 1142 | 432 |
| 0day Montgomery | 0day | OllieIsTheBestDog | 5555 3412 4444 1115 | 642 |
| Muir Land | muirlandoracle |A11D0gsAreAw3s0me | 5103 2219 1119 9245 | 737 |