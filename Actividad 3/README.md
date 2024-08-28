# Actividad: Introducción a Git - conceptos básicos y operaciones esenciales

### Conceptos básicos de Git: Comienza con una experiencia práctica

**git config: Preséntate a Git**  

Definimos nuestro nombre y email a nivel **systema** usando la bandera `--global`:  

```shell
$ git config --global user.name "Lerzundi"
$ git config --global user.email "juan.lerzundi.r@uni.pe"
```

Y confirmamos el cambio usando la bandera `--list`:  

```shell
$ git config --list
```  
![altex text](../Imagenes/Actividad3_1.PNG)  

**git init: Donde comienza tu viaje de código**  

![alt text](../Imagenes/Actividad3_2.PNG)

Luego de crear un directorio y acceder a él, usamos `git init` para inicializar un repositorio  

![alt text](../Imagenes/Actividad3_3.PNG)  
![alt text](../Imagenes/Actividad3_4.PNG)  

Vemos que ahora tenemos una carpeta oculta `.git` donde se guardarán los cambios en el archivo.

**git add: Preparando tu código**  

![alt Text](../Imagenes/Actividad3_5.PNG)  
![alt Text](../Imagenes/Actividad3_6.PNG)  

Creamos un archivo `README.md` que luego rastreamos con el comando `git add README.md`, situándonos en el estado de preparación o index.  

**git commit: registra cambios**  

![alt text](../Imagenes/Actividad3_7.PNG)  
![alt text](../Imagenes/Actividad3_8.PNG)  

Guardamos nuestros cambios usando el `commit`:  

```shell
$ git commit -m "Initial commit with README.md
```