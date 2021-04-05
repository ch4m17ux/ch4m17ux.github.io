# #FromZeroToLynx - CTF writeUp - Silver

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/banner.png)

En los este (y los siguientes) post quiero traer los retos que se estan desarrollando en el CTF desarollado por [ZeroLynx](https://www.zerolynx.com/es/home), donde se nos presentan retos enmarcados en el evento de ESL España CS:Go.

En esta entrada abordaré los retos del nivel basico o Silver.

Si quieres participar tienes información [ [Aquí](https://www.fromzerotolynx.gg/) ]

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 
---

## **Farm**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> La noche se te fue de las manos y te has quedado encerrado… ¡en una granja de pollos!
>
>¿Encontrarás la flag de salida?
>

Nos entregan un fichero con extensión `.bsp` (Lo puedes descargar [AQUI](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/granja.bsp))

Lo primero que hago siempre, es verificar que el fichero entregado sea lo que presuntamente nos dicen que es, asi que lo verificamos a traves del comando `file`:

```console
kali@kali:~/ZeroToLynx$ file granja.bsp
granja.bsp: data
```

Vemos que es un fichero con informacion de datos, asi que procedemos a verificar si encontramos algo entre sus `strings`. (*Aqui yo he ido aumentado el numero de caracteres que quiero que busque, debido a que me salia mucha información*)

```console
kali@kali:~/ZeroToLynx$ strings -n 45 granja.bsp
"axis" "512 -226.05 -27.8, 502.89 -223.53 -27.8"
"message" "ESL{MuyBienMatasteAlPolloCorrecto}"
materials/maps/granja/cubemapdefault.hdr.vtfVTF
materials/maps/granja/cubemapdefault.hdr.vtfPK
```
Hemos encontrado la flag que nos han solicitado: **ESL{MuyBienMatasteAlPolloCorrecto}**

*Otra opcion podria ser haber copiado el mapa en Counter Strike: Global Offensive y cargarlo para matar a los pollos, y de entrada jugar un rato.*

---

## **Pretorianos**

Nos entregan la descripción del reto:

> ***OBJETIVO***:
> ¿Txh kdb pdv ohjhqgdulr txh od jxdugld suhwruldqd gh Mxolr Fhvdu?
>
>Y nos entregan una imagen:
>
>![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/pretorianos.png)

Tenemos que identificar que dice el mensaje que para estar codificado de alguna forma, asi que lo pasare por CyberChef y trataremos de obtener el mensaje.

![CTF #FromZeroToLynx](https://ch4m17ux.github.io/img/posts/ctf-zerotolynx/pretorianos_2.png)

Vemos que se descifra con Rot23 o lo que es lo mismo con cifrado Cesar.