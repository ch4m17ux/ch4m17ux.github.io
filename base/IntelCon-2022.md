# CTF IntelCon 2022 - #writeUp

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/logo-intelcon.png)

He estado participando en un CTF organizado por Gingseg con el apoyo de ZeroLynx, basado en retos de tipo OSINT.

No soy experto en OSINT, asi que es una experiencia enriquecedora y agradezco a la organizacion por la realizacion y el trabajo realizado.

Se han presentado en total 9 retos, en 3 lineas, que llamaremos, de investigacion.

---
>### Disclaimer: 
>Estas entradas no pretenden indicar que sea la unica forma de solucionar, todo se realiza de forma academica, cualquier errata se agradece que sear reportada para poder subsanar.
>Espero que os guste y aprendamos juntos. #HackThePlanet
 

# TL:DR

---
## **Insider I**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-I.jpg)

>**Datos proporcionados:**
>
>Fichero 7zip.

En este reto se nos entrega un fichero 7zip, que al abrirlo contiene un Readme y un fichero txt, que contiene una cadena de texto al parecer en Base64, pero al tratar de decodificarlo, no muestra nada legible.  Por otra parte, se nos indica en el Readme que los ficheros han sido cifrados en AES-256.  Tambien nos detallamos en el comentario "Contamos CONTI GO ;)", asi que todo indica que tiene alguna relacion con el grupo CONTI.

Buscamos en Google cosas relacionadas con CONTI y dentro del millar de resultados vemos que hay una cuenta en español de @conti_es.

Analizamos este usuario y no tiene mucha información, tambien contiene muy pocos post, asi como muy pocos seguidores, sin embargo, revisando a que personas sigue en twitter, la mayoria son personas relacionadas con la ciberseguridad en España, a excepcion de uno que resalta por tener su descripcion en Ingles.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-I-1.jpg)
He revisado su perfil entendiendo que debia buscar alguna clave, pero finalmente, luego de algunos fallos, he descubierto que la flag era el nombre de usuario. 

Por lo que encontramos que la flag es:
**`FLAG: INT{m1Geelka}`**

---
## **Insider II**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-II.jpg)

Para este reto, revisando los post del usuario en twitter que encontramos en el reto anterior (*`@m1Geelka`*) vemos que hay pocos post, sin embargo, encontramos cadenas de texto y una URLS.

He probado las URLs que estan alli, pero o bien no accede, en el caso de ONION, en el otro es un banner, como es un CTF de OSINT no he tirado por stego de la imagen para no rizar el rizo, probando las cadenas como flag da error, así que he tomado las cadenas y las URL’s y he ido reemplazando en las URL's encontradas, para ver si por casualidad alguna mostraba alguna informacion interesante.  Al final una de ellas es la correcta:

Reemplazando en la URL de anonfiles con una de las cadenas:
7eK111z2yd ->> https://anonfiles.com/7eK111z2yd

Obtenemos un HTML que al visualizarlo nos muestra un texto: PB: m4v8z6AK

Por lo que encontramos que la flag es:
**`FLAG: INT{m4v8z6AK}`**

---
## **Insider III**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III.jpg)

En este reto luego de probar con las cadenas que aparecen en Twitter, y ver que no daba con la llave de descifrado, he visto que en el ID anterior indicaba algo de PB. Pues luego de dar muchas vueltas se me ocurrió que PB podría ser Pastebin, además que es un sitio donde regularmente se publican datos de exfiltraciones, y se ha iluminado el camino.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III-1.jpg)

En este pastebin no encuentro nada, así que decido buscar en su usuario para ver si tiene más publicaciones.

En todas se trata de exfiltraciones que quiza ha encontrado, pero me ha llamado la atención una que hace referencia a un bucket de S3 en Amazon.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III-2.jpg)

> `conti-the-filecrypter-repo.s3.eu-west-3`

Agregando lo que le falta para que la URL de Amazon sea correcta, tenemos:
*https://conti-the-filecrypter-repo.s3.eu-west-3.amazonaws.com/*

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III-3.jpg)

Vemos que en el xml se muestra una carpeta que contiene un fichero `key.bk`, asi que con la URL anterior y completando de nuevo con estos datos, podemos descargarlo.
*https://conti-the-filecrypter-repo.s3.eu-west-3.amazonaws.com/Configs/key.bk*

Y al revisar el contenido, tenemos:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III-4.jpg)

Así que hacemos uso del contenido del fichero y esta key.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/insider-III-5.jpg)

Por lo que encontramos que la flag es:
**`FLAG: INT{_c0n71_15_d4n63r0u5_}`**

---
## **Destino I**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-1.jpg)

Este reto hay que hacer uso de Google images, Yandex u otro similar, subiendo la imagen y viendo las mas parecidas he encontrado que en algunas pone que se parece a una fotos del aeropuerto de Naxos.

No ha sido fácil, ya que no hay coincidencia directa (por lo menos a mi no me ha salido), por lo que ha sido probar, con el aeropuerto de Naxos, que era el que salia en las coincidencias.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-I-1.jpg)

Encontramos que la flag es:
**`FLAG: INT{NAXOS}`**

---
## **Destino II**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-II.jpg)

Este reto es muy difícil, no hay de donde tirar, así que he dado muchas vueltas que no detallare aquí que me enrollo, asi que no quiero que parezca que ha sido magia, pero atando cabos he buscado los vuelos que salen desde allí de forma directa y me sale uno que es hacia Atenas.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-II-1.jpg)

Pero sigo dando vueltas, como unir esto con alguien que le haya recomendado cosas? Se me ha ocurrido que buscar en la red social por excelencia de ocupaciones puede ser una buena opcion, pero no me salía nada con tripulantes de cabina que estén en Grecia o similares, luego he unido esto con las siglas del aeropuerto de naxos, pero nada, así que he puesto la ruta JNX-ATH junto con tripulante de cabina y no había nada que fuese algo para este CTF, al final he decidido probar con el puesto de trabajo en griego para ver si sonaba alguna campana, y aunque lo dude, sono.

He visto un perfil mas falso que la leche y tenía que ser ese.  De nuevo digo que no es sencillo este reto, lo dicho, he tardado muchas horas en solo este reto.

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-II-2.jpg)
He probado con su nombre completo y no valia, asi que he puesto solo su primer nombre.

Encontramos que la flag es:
**`FLAG: INT{IOSIF}`**

---
## **Destino III**

Nos entregan la descripción del reto:

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-III.jpg)

Este reto también es complicado, pero viendo las fotos del linkedin del tripulante vemos que hay unas vistas, dice que te recomienda un hotel con esas vistas, porque su casa esta ocupada. Revisando la foto en Google images sale que es una imagen de una plaza, y revisando qué plaza es, encontramos que es Plaza Monastikari. 

Así que he buscado los hoteles que dan en esa plaza y encontré dos, en ambos hice una búsqueda en booking y tripadvisor para ver si encontraba algo relacionado al CTF y solo en el siguiente de la imagen, encontré como primera recomendacion. (también cabe aclarar que viendo los demás retos era ese y ya tenia datos para los demás que me hacia falta)

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-III-1.jpg)

![CTF IntelCon 2022](https://ch4m17ux.github.io/img/posts/intelcon-2022/Destino-III-2.jpg)

He probado con su nombre completo y no valia, asi que he puesto solo su primer nombre.

Encontramos que la flag es:
**`FLAG: INT{p0SMzGL1oAMhWin}`**

---
Espero que os haya gustado
----------
# Fin
Cualquier errata o duda es bienvenida.
