# Actividad Play with Docker

## Getting Started Walk-through for IT Pros and System Administrators

### Stage 1: The Basics

#### **First Alpine Linux Containers**

> [!TIP] Se dispone de una terminal incluida en el navegador para realizar los ejercicios del laboratorio  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_1.PNG)
 

**1.0 Running your first container**

Comenzar creando el contenedor de ejemplo `hello-world`  

```shell
$ docker container run hello-world
```
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_2.PNG)
El motor de Docker no pudo encontrar la imagen localmente, por lo que se dirige al registro centralizado de docker, Docker Hub y descarga la imagen desde ahí.
<img src="../Imagenes/Actividad Play with Docker/ActividadPlaywithDocker_3.png" alt="alt text">

**1.1 Docker images**  

```shell
$ docker image pull alpine
``` 
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_4.png)  
El comando `pull` descarga la imagen de alpine desde Docker Hub y la guarda localmente. 
Luego, listar las imágenes disponibles  
```shell
$ docker image ls
```  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_5.png)  

**1.2 Docker container run**  

Crear un contenedor desde la imagen de alpine  
```shell
$ docker container run alpine ls -l
```
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_6.png)  
El contenedor ejecuta el comando `ls -l` y lista los archivos en el directorio, acto seguido se apaga, este es el ciclo de vida por defecto de un contenedor.  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_7.png)  

Ejecutar el comando `echo` en un contenedor.    
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_8.png)  
El mensaje `"hello from alpine"` ha sido impreso y se cierra el contenedor.  

Ejecutar el comando `/bin/sh` en un contenedor  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_9.png)
No se muestra nada en nuestro terminal, solo se ejecutó y cerró instantáneamente el shell pues no se le pasó ningún comando adicional.  

Ejecutar el comando `/bin/sh` en un contenedor con la bandera `-it` de Docker  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_10.png)  
Dentro del contenedor se está ejecutando la shell de Alpine Linux, podemos ingresar varios comandos como `ls -l` y `uname -a`, luego salimos del contenedor con `exit`.  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_11.png)

Listar los contenedores ejecutándose ahora.  
```shell
$ docker container ls
```
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_12.png)
No hay ningún contenedor ejecútandose en este momento, por lo que la lista está vacía.

Listar todos los contenedores. 
```shell
$ docker container ls -a
``` 
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_13.png)
Existen 5 instancias de alpine que han sido corridas desde el comienzo del laboratorio. Con esto se confima que cada vez que usamos `docker run` se crea un nuevo contenedor con la imagen de alpine usando el comando que ingresamos en cada instancia.
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_14.png)

**1.3 Container Isolation**

Correr `/bin/ash` dentro de un contenedor.  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_15.png)
Al correr echo `"hello world"` en un nuevo archivo `hello.txt` y luego usar `ls` vemos que se encuentra listado el nuevo archivo.  

Correr `ls` dentro de un contenedor.  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_16.png)
El archivo `hello.txt` que creamos no se encuentra. Esto demuestra el aislamiento entre contenedores, pues el primer contenedor no puede interactuar con el segundo.

Mostrar todos los contenedores  
```shell
$ docker container ls -a
```
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_17.png)  
![alt text](../Imagenes/Actividad%20Play%20with%20Docker/ActividadPlaywithDocker_22.png)  
> Representación gráfica de lo realizado en este laboratorio  
