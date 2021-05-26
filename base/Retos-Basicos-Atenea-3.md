# Resolviendo los retos básicos de Atenea (CCN-CERT) 

En un [primer post](https://ch4m17ux.github.io/2021/01/06/retos-basicos-atenea.html) estuve presentando la resolución de los retos básicos de Atenea, posteriormente realice una [segunda entrega](https://ch4m17ux.github.io/2021/01/07/retos-basicos-atenea-2.html); finalizare en esta entrega.

## Reto 13 – Variable

### **Enunciado:**

Nos dan unos ejemplos de tipos de variables y nos piden buscar o identificar el que tiene un tipo de datos erróneo:

>byte num = 44;
short med = 1223;
long lmax = 839492019487;
float mreal = 112.31f;
double rbig = 761132.4321;
boolean bbin = true;
int max = "1000";
char lett = 'A';

La solución al reto es el nombre de la variable (*por ejemplo: vbar*), en el formato de la plataforma.

### **Solución:**

Realizando una verificación y si tenemos alguna experiencia en programación, nos podemos dar cuenta que a la variable ***max***, que es de tipo entero (*int*) le han asignado una cadena de texto.  Asi que la respuesta es: ***`max`***

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-1.png)
## Reto 14 – Variable 2

### **Enunciado:**

Nos dan una linea de código en **`BASIC`**, y nos piden que encontremos el equivalente en **`BASH`**.  
  
>**`PRINT "Atenea"`**

### **Solución:**

Si tenemos experiencia en **`BASH`**, podemos darnos cuenta que este reto es muy sencillo, ya que para mostrar en pantalla una cadena de texto utilizamos:

>**echo "Atenea"**

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-2.png)
## Reto 15 – C

### **Enunciado:**

En este reto nos dan un binario escrito en **`C`**, nos piden compilarlo y ejecutarlo.

### **Solución:**

Utilizamos ***`gcc`*** para poder compilar el fichero dado y posteriormente lo ejecutaremos.  Voy a ejecutar el comando y le indico que quiero que cree un fichero con nombre **`pass`**

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-3.png)
## Reto 16 – Python

### **Enunciado:**

Nos dan un script escrito en **`Python`** y nos piden que obtengamos el valor de la variable **`result`**, esta variable nos dará el password que necesitamos.

### **Solución:**

Si tenemos (o no, lo podemos averiguar) experiencia en `Python`, sabemos que para obtener el valor de una variable y mostrarla en pantalla utilizamos la función **`print`**, así que bastara con añadir al final del fichero la linea:

>`print result`

Podemos abrir el script con cualquier editor de texto, o simplemente por consola podemos usar el comando `echo` para nuestra finalidad.  Finalmente ejecutamos el script:

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-4.png)
## Reto 17 – Java

### **Enunciado:**

En este caso nos han dado un script en `Java`, nos piden descompilarlo y buscar el valor de una variable que resalta sobre las demás.

### **Solución:**

Basta con utilizar un descompilador online como http://www.javadecompilers.com

Cargamos el binario Java que nos han dado y esperamos los resultados.  Dentro de lo que podemos ver, observamos que a simple vista hay una variable que resalta.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-5.png)
Fácilmente encontramos que la contraseña para resolver el reto es:

 >final  String  ThisIsTheVariableYouAreLookingFor  =  "30853506b923083a";

Lo convertimos en el formato de la flag solicitada.

![Retos Básicos Atenea](https://ch4m17ux.github.io/img/posts/reto-basico-atenea-2/basico-atenea-3-6.png)

---
*Con esta entrega damos finalización a los retos básicos de Atenea. Espero os haya gustado y os sirva.  Cualquier comentario, no dudéis en enviarlo a mi contacto.*