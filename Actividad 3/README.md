# Actividad: Introducción a Git - conceptos básicos y operaciones esenciales

## Conceptos básicos de Git: Comienza con una experiencia práctica

### git config: Preséntate a Git  

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

<hr></hr>

### git init: Donde comienza tu viaje de código  

![alt text](../Imagenes/Actividad3_2.PNG)

Luego de crear un directorio y acceder a él, usamos `git init` para inicializar un repositorio  

![alt text](../Imagenes/Actividad3_3.PNG)  
![alt text](../Imagenes/Actividad3_4.PNG)  

Vemos que ahora tenemos una carpeta oculta `.git` donde se guardarán los cambios en el archivo.

<hr></hr>

### git add: Preparando tu código  

![alt Text](../Imagenes/Actividad3_5.PNG)  
![alt Text](../Imagenes/Actividad3_6.PNG)  

Creamos un archivo `README.md` que luego rastreamos con el comando `git add README.md`, situándonos en el estado de preparación o index.  

<hr></hr>

### git commit: registra cambios  

![alt text](../Imagenes/Actividad3_7.PNG)  
![alt text](../Imagenes/Actividad3_8.PNG)  

Guardamos nuestros cambios usando el `commit`:  

```shell
$ git commit -m "Initial commit with README.md
```  

Y ya no vemos al archivo `README.md` como no seguido.  

<hr></hr>

### git log: Recorrer el árbol de commits  

![alt tex](../Imagenes/Actividad3_9.PNG)  


**¿Cuál es la salida de este comando?**

```shell
$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
```

![alt text](../Imagenes/Actividad3_10.PNG)  

Usemos el comando `git log` para una siguiente actividad, creamos el archivo `CONTRIBUTING.md` y editamos el archivo `README.md` con el texto `"README\n\nWelcome to the project"`.
Luego los añadimos a `git` y hacemos un commit.

Finalmente, agregamos el archivo `main.py` y lo llenamos con un código de ejemplo:  

```shell
$ echo "print('Hello World')" > main.py
```

Y hacemos un commit luego de registrar los cambios.

```shell
git log --oneline
```  
![alt text](../Imagenes/Actividad3_11.PNG)  

## Trabajar con branches: La piedra angular de la colaboración

### git branch: Entendiendo los conceptos básicos de Git branch

![alt text](../Imagenes/Actividad3_11.PNG)  
![alt text](../Imagenes/Actividad3_12.PNG)  

**Crear una branch desde una branch específica**  

```shell
$ git branch <new-branch-name> <base-branch-name>
```  

**Crear una branch desde un commit específico**  

```shell
$ git branch <new-branch-name> <commit-hash>
```  

### git checkout/git switch: Cambiar entre branches 

**Cambiar a la branch feature/new-feature:** `$ git checkout feature/new-feature`