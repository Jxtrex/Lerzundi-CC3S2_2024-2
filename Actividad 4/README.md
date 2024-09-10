# Actividad 4: Explorando diferentes formas de fusionar en Git – Parte 1



## Ejemplos Prácticos

### 1. Fusión Fast-forward (git merge --ff)

**Pasos**

Crea el directorio de trabajo:

```shell
$ mkdir try-fast-forward-merge
$ cd try-fast-forward-merge
```

Agrega un archivo a `main` y realiza cambios:  

```shell
$ echo "# Mi Proyecto" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"
```

Dirígite a una nueva rama y realiza cambios:

```shell
$ git checkout -b add-description
```

```shell
$ echo "Este proyecto es un ejemplo de cómo usar Git." >> README.md
$ git add README.md
$ git commit -m "Agregar descripción al README.md"
```
La estructura de commits se ve así:  

![alt text](../Imagenes/Actividad%204/Actividad4_1.png)

Cambia de vuelta a `main` y realiza fusión **fast-forward**:  

```shell
$ git checkout main
$ git merge add-description
```

```shell
$ git log --graph --oneline
```

Ahora, el historial se verá así:  

![alt text](../Imagenes/Actividad%204/Actividad4_2.png)

### 2. Fusión No-fast-forward (git merge --no-ff)

**Pasos**

Crear un nuevo directorio y realiza cambios:  

```shell
$ mkdir try-no-fast-forward-merge
$ cd try-no-fast-forward-merge
```

```shell
$ echo "# Mi Proyecto" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"
```

Cambiar a una nueva rama y hacer cambios:  

```shell
$ git checkout -b add-feature
```

```shell
$ echo "Implementando una nueva característica..." >> README.md
$ git add README.md
$ git commit -m "Implementar nueva característica"
```

Ahora el log de commits se ve así:  

![alt text](../Imagenes/Actividad%204/Actividad4_3.png)

Volver a `main` y realizar la fusión no-fast-forward:  

```shell
$ git checkout main
$ git merge --no-ff add-feature
```

Ver el log ahora:  

```shell
$ git log --graph --oneline
```

![alt text](../Imagenes/Actividad%204/Actividad4_4.png)

### 3. Fusión squash (git merge --squash)

**Pasos**

Crear un nuevo directorio y realizar cambios:  

```shell
$ mkdir try-squash-merge
$ cd try-squash-merge
```

```shell
$ echo "# Mi Proyecto" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"
```

Crear una nueva rama y realizar cambios:  

```shell
$ git checkout -b add-basic-files

```

```shell
$ echo "# CÓMO CONTRIBUIR" >> CONTRIBUTING.md
$ git add CONTRIBUTING.md
$ git commit -m "Agregar CONTRIBUTING.md
```

```shell
$ echo "# LICENCIA" >> LICENCIA.txt
$ git add LICENSE.txt
$ git commit -m "Agregar LICENSE.txt"
```

Ahora tu estructura de commits debería verse como la imagen:  
![alt text](../Imagenes/Actividad%204/Actividad4_5.png)  

Cambiar a la rama mainy realizar la función squash:  

```shell
$ git checkout main
$ git merge --squash add-basic-files
```

Los commits luego se aplastan y se convierten en un solo commit.
Para completar la fusión squash, realiza un commit:  

$ git add .
$ git commit -m "Agregar documentación estándar del repositorio"
$ git log --graph --oneline

Esto combinará todos los cambios de la rama add-basic-files en un solo nuevo commit en la rama main:  
