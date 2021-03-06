# TryHackMe: Curso intensivo de pentesting (primera parte)

![Curso Pentesting - TryHackMe](https://ch4m17ux.github.io/img/posts/curso-intensivo-pentesting/pentesting-1.png)

En esta oportunidad quiero traer un post de mi amigo @DamonCDB, quien es uno de los mas disciplinados que he conocido en este tema de hacking etico y pentesting.  Podeis visitar su Blog llamado "[Mis Hobbies](https://mostrandomishobbies.blogspot.com)".  

Este articulo es de su autoría y quiero tambien compartirlo con vosotros para que conozcais su trabajo.  Podeis visitar el post original [AQUI](https://mostrandomishobbies.blogspot.com/2021/01/tryhackme-ci-pentesting-primera-parte.html)

---

En esta ocasión vamos a ver una sala que nos muestra algunos comandos a la hora de empezar con el pentesting.  La sala se llama: [CC - Pen testing](https://tryhackme.com/room/ccpentesting)

Más adelante veremos cada una de estas herramientas con más detenimiento, pero por ahora esto es un acercamiento a dichas herramientas para ir familiarizándonos con ellas.

Esta sala estará dividida, ya que consta de 7 secciones distintas, y bastante extensas. Además, en esta ocasión os he publicado las respuestas de cada una de las preguntas, aunque la mayoría son sencillas de encontrar con tan solo usar la página del manual de cada herramienta o, en su defecto, la ayuda (*ya sabéis, para usar el manual solo tenéis que escribir `"man comando"` y para la mayoría de herramientas la ayuda aparece con comando `"--help"`).

Para cualquier duda, no tengáis problema en ponerme un comentario, y os atenderé tan pronto me sea posible.  

## **CURSO INTENSIVO DE PENTESTING**

La idea tras esta sala es proveer de una introducción a varias herramientas y conceptos que os encontraréis de forma habitual en los test de penetración.

Esta sala asume que tenéis un conocimiento básico de Linux y redes.  Además, no está destinada a ser un *“final absoluto”* en el tema de las pruebas de penetración.

Las tareas en esta sala pueden completarse en cualquier orden; de todos modos, si eres nuevo en el mundo del pentesting, es recomendable completar las dos primeras antes de hacer nada más.

### **SECCIÓN 1 – UTILIDADES DE RED**

#### **NMAP**

`Nmap` es una de las herramientas más importantes en el arsenal de cualquier pentester. Ésta nos permite ver qué puertos están abiertos, además de información sobre qué servicios están corriendo en cada uno de esos puertos. Por lo tanto, esta tarea se enfocará a enseñaros varios modificadores de `nmap`. Las primeras preguntas pueden contestarse con tan solo utilizar la página de manual de `nmap`. Las últimas requerirán que despliegues la máquina virtual que te facilitamos.

-   ¿Qué significa nmap? Respuesta: *`Network Mapper`*
-   ¿Cómo especificas qué puerto(s) hay que escanear? Respuesta: *`-p`*
-   ¿Cómo realizar un “escaneo ping” (comprobar si el host está activo)? Respuesta: *`-sn`*
-   ¿Cuál es el modificador para un escaneo UDP? Respuesta: *`-sU`*
-   ¿Cómo corres los scripts por defecto? Respuesta: *`-sC`*
-   ¿Cómo activas el “modo agresivo” (habilita la detección de SO, detección de versión, escaneo de scripts y traceroute)? Respuesta: *`-A`*
-   ¿Qué modificador habilita la detección de SO? Respuesta: *`-O`*
-   ¿Cómo consigues las versiones de los servicios que están corriendo en la máquina objetivo? Respuesta: *`-sV`*

Es hora de desplegar la máquina adjunta:

-   ¿Cuántos puertos hay abiertos en la máquina? Respuesta: *`1`*
-   ¿Qué servicio está corriendo en la máquina? Respuesta: *`Apache`*
-   ¿Cuál es la versión del servicio? Respuesta: *`2.4.18`*
-   ¿Cuál es la salida del script http-title (incluido en los scripts por defecto): Respuesta: *`Apache2 Ubuntu Default Page: It Works`*

#### **NETCAT**

Netcat, también conocido como `nc`, es una herramienta extremadamente versátil. Permite a los usuarios conectar a puestos específicos y enviar y recibir datos. También permite a las máquinas recibir datos y conexiones en puertos específicos, lo cual hace de nc una herramienta muy popular para conseguir una `Reverse Shell`.

Después de conectar a un puerto con `nc` podréis enviar datos, esto también tiene la consecuencia para el usuario de poder mandar datos mediante una tubería o pipe con `nc`. Por ejemplo, se puede hacer `"echo hello | nc <ip> 1234`" para enviar la cadena `hello` al servicio corriendo en el puerto `1234`.

Nota: Hay múltiples versiones de `nc`, por lo que si no puedes encontrar una respuesta en tu página de manual específica, prueba con las páginas de manual de otras versiones.

-   ¿Cómo se pone a la escucha para conexiones? Respuesta: *`-l`*
-   ¿Cómo se activa el modo verbose (te permite ver quién se ha conectado a ti)? Respuesta: *`-v`*
-   ¿Cómo especificamos el puerto en el que escuchar? Respuesta: *`-p`*
-   ¿Cómo especificamos qué programa ejecutar después de conectar al host (uno de los más infames)? Respuesta: *`-e`*
-   ¿Cómo conectamos a puertos udp? Respuesta: *`-u`*

### **SECCIÓN 2 – ENUMERACIÓN WEB**

#### **GOBUSTER**

Uno de los principales problemas en el pentesting de páginas web es no saber dónde está cada cosa. Un reconocimiento básico puede decirnos dónde se encuentran algunos ficheros y directorios; de todos modos, algunas de las cosas más importantes estarán ocultas a los ojos de los usuarios. Ahí es donde entra `Gobuster`, la idea tras este programa es que intenta encontrar directorios válidos de un diccionario de posibles directorios. `Gobuster` puede utilizarse también para subdominios válidos utilizando el mismo método.

Las primeras preguntas de esta tarea se pueden contestar utilizando la página de manual de `Gobuster`, mientras que las últimas requerirán el despliegue de la máquina virtual.

Si en el SO que estás utilizando no se encuentra la página de manual de `Gobuster`, utiliza `"gobuster –help"`.

-   ¿Cómo especificamos el modo de fuerza bruta para ficheros y directorios? Respuesta: *`dir`*
-   ¿Cómo especificamos el modo de fuerza bruta para dns? Respuesta: *`dns`*
-   ¿Qué modificador indica las extensiones a buscar? Por ejemplo, si la extensión configurada es php, y la palabra es “admin”, entonces gobuster buscará admin.php en el servidor web. Respuesta: *`-x`*
-   ¿Qué modificador indica el diccionario a utilizar? Respuesta: *`-w`*
-   ¿Cómo indicamos el Username para una autenticación básica (si el directorio requiere un usuario/contraseña)? Respuesta: *`-U`*
-   ¿Cómo especificamos la contraseña para una autenticación básica? Respuesta: *`-P`*
-   ¿Cómo indicamos los códigos de estado que gobuster interpretará como válidos? Por ejemplo, 200, 400, 404, 204 Respuesta: *`-s`*
-   ¿Cómo saltamos la certificación de ssl? Respuesta: *`-k`*
-   ¿Cómo especificamos un User-Agent? Respuesta: *`-a`*
-   ¿Cómo especificamos una cabecera HTTP? Respuesta: *`-H`*
-   ¿Qué modificador establece la URL en fuerza bruta? Respuesta: *`-u`*

Despliega la máquina adjunta:

-   ¿Cuál es el nombre del directorio oculto? Respuesta: *`secret`*
-   ¿Cuál es el nombre del archivo oculto con extensión xxa? Respuesta: *`password`*

#### **NIKTO**

`Nikto` es una herramienta de escaneo web muy popular que permite a los usuarios encontrar vulnerabilidades comunes en la web. Normalmente se utiliza para verificar CVE’s comunes como shellshock, además de para conseguir información general acerca de un servidor web que le indicamos.

-   ¿Cómo especificamos el host a utilizar? Respuesta: *`-h`*
-   ¿Qué modificador desactiva ssl? Respuesta: *`-nossl`*
-   ¿Cómo forzamos ssl? Respuesta: *`-ssl`*
-   ¿Cómo especificamos la autenticación (usuario + contraseña)? Respuesta: *`-id`*
-   ¿Cómo seleccionamos qué plugin utilizar? Respuesta: *`-plugins`*
-   ¿Qué plugin comprueba si podemos enumerar a los usuarios de apache? Respuesta: *`apacheusers`*
-   ¿Cómo actualizamos la lista de plugins? Respuesta: *`-update`*
-   ¿Cómo listamos los plugins que podemos utilizar? Respuesta: *`--list-plugins`*

### **SECCIÓN 3 – METASPLOIT**

`Metasploit` es uno de los frameworks de pentesting más populares que existe. Contiene una extensa base de datos de casi todos los CVE, los cuáles puedes utilizar fácilmente contra una máquina. El objetivo de esta sección es adentraros un poco en algunas de las características de metasploit, y al final encontraréis una máquina que necesitaréis explotar.

#### **PREPARANDO**

Una vez instalado `metasploit` por medio de su instalador o de los repositorios de vuestra distribución, tendréis varios comandos disponibles. Esta sección se enfocará principalmente en el comando `msfconsole`.

La ejecución de este comando nos presentará un prompt de *`“msf5”`* el cual nos permitirá entrar los comandos. Todas las tareas se pueden contestar con el comando `“help”`

-   ¿Qué comando nos permite buscar módulos? Respuesta: *`search`*
-   ¿Cómo seleccionamos un módulo? Respuesta: *`use`*
-   ¿Cómo mostramos información acerca de un módulo específico? Respuesta: *`info`*
-   ¿Cómo listamos las opciones que podemos configurar? Respuesta: *`options`*
-   ¿Qué comando nos permite ver las opciones avanzadas de un módulo en concreto? Respuesta: *`advanced`*
-   ¿Cómo mostramos las opciones de una categoría específica? Respuesta: *`show`*

#### **SELECCIONANDO UN MÓDULO**

Una vez encontrado el módulo necesario para la máquina que queráis explotar, necesitaréis seleccionarlo y configurar las opciones pertinentes. Esta tarea os llevará a través de esta selección y configuración de opciones para uno de los módulos más conocidos de metasploit: *`“eternalblue”`*. Todos los comandos básicos que pueden ejecutarse antes de seleccionar un módulo pueden utilizarse también una vez que el módulo ha sido seleccionado.

-   ¿Cómo seleccionamos el módulo eternalblue? Respuesta: *`use exploit/windows/smb/ms17_010_eternalblue`*
-   ¿Qué opción nos permite seleccionar el o los hosts objetivos? Respuesta: *`RHOSTS`*
-   ¿Cómo indicamos el puerto objetivo? Respuesta: *`RPORT`*
-   ¿Qué comando nos permite configurar las opciones? Respuesta: *`set`*
-   ¿Cómo configuramos el SMBPass a “username”? Respuesta: *`set SMBPass username`*
-   ¿Cómo configuramos el SMBUser a “password”? Respuesta: *`set SMBUser password`*
-   ¿Qué opción configura la arquitectura a ser explotada? Respuesta: *`arch`*
-   ¿Qué opción configura el payload que se enviará a la máquina objetivo? Respuesta: *`payload`*
-   Una vez finalizada la configuración de las opciones requeridas, ¿cómo corremos el exploit? Respuesta: *`exploit`*
-   ¿Qué modificador configuramos si queremos que el exploit se ejecute en segundo plano? Respuesta: *`-j`*
-   ¿Cómo listamos las distintas sesiones actuales? Respuesta: *`sessions`*
-   ¿Qué modificador nos permite entrar en el modo interactivo en una sesión (nos lleva a un meterpreter o a una regular shell)? Respuesta: *`-i`*

#### **METERPRETER**

Una vez ejecutado el exploit, lo ideal es que os dirija a una de estas dos cosas: una shell de comandos o una shell de meterpreter. `Meterpreter` es el *“centro de control”* de `metasploit` donde podéis hacer varias cosas para interactuar con la máquina. Podéis encontrar una lista de los comandos más comunes de meterpreter [aquí](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/).

> *Nota: Las regular shells pueden actualizarse a shells de meterpreter usando el módulo `post/multi/manage/shell_to_meterpreter`.*

-   ¿Qué comando nos permite descargar archivos desde la máquina? Respuesta: *`download`*
-   ¿Qué comando nos permite subir archivos a la máquina? Respuesta: *`upload`*
-   ¿Cómo listamos los procesos en ejecución? Respuesta: *`ps`*
-   ¿Cómo cambiamos los procesos en el host de la víctima (idealmente ello nos permitirá cambiar de usuario y conseguir los permisos asociados a ese usuario)? Respuesta: *`migrate`*
-   ¿Qué comando listará los ficheros en el directorio actual en la máquina remota? Respuesta: *`ls`*
-   ¿Cómo ejecutamos un comando en la máquina objetivo? Respuesta: *`execute`*
-   ¿Qué comando inicia una shell interactiva en la máquina objetivo? Respuesta: *`shell`*
-   ¿Cómo encontramos archivos en la máquina objetivo (función similar a la del comando de Linux “find”)? Respuesta: *`search`*
-   ¿Cómo obtenemos la salida de un archivo en la máquina remota? Respuesta: *`cat`*
-   ¿Cómo ponemos una shell de meterpreter en “modo segundo plano” (esto permite ejecutar otros módulos de msf mientras mantiene la shell de meterpreter como una sesión)? Respuesta: *`background`*

#### **GUÍA FINAL**

Es momento de utilizar todo lo aprendido en las tareas anteriores de metasploit y probarlas en una máquina de ejemplo. Esta máquina es vulnerable al módulo de metasploit `exploit/multi/http/nostromo_code_exec` en el puerto `80`, y esta tarea os llevará a lo largo del proceso de explotación y obtención de una shell en la máquina.

-   Selecciona el módulo que necesita ser explotado. Respuesta: *`use exploit/multi/http/nostromo_code_exec`*
-   ¿Qué variable necesitamos configurar para seleccionar el host remoto? Respuesta: *`rhosts`*
-   ¿Cómo configuramos el puerto 80? Respuesta: *`set rport 80`*
-   ¿Cómo configuramos la dirección de escucha (nuesta máquina)? Respuesta: *`lhost`*

Es hora de desplegar la máquina:

-   ¿Cuál es el nombre del directorio secreto dentro del directorio /var/nostromo/htdocs? Respuesta: *`s3cretd1r`*
-   ¿Cuál es el contenido del archivo que hay dentro del directorio? Respuesta: *`Woohoo!`*


# Fin