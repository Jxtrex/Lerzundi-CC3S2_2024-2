# Actividad 5: Entendiendo git rebase y git cherry-pick

## Parte Práctica

### Parte 1: git rebase para mantener un historial lineal

Crear una nueva carpeta `try-git-rebase` y dos ramas, `main` y `new-feature`, luego haz cambios en cada una  

En la rama main.  
```shell
$ mkdir try-git-rebase
$ cd try-git-rebase
$ echo "# Mi Proyecto de Rebase" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"
```

En la rama new-feature.  
```shell
$ git checkout -b new-feature
$ echo "Esta es una nueva característica." > NewFeature.md
$ git add NewFeature.md
$ git commit -m "Agregar una nueva característica
```

En este punto, el historial de ramas puede verse algo así:  
![alt text](../Imagenes/Actividad%205/Actividad5_1.PNG)  
![alt text](../Imagenes/Actividad%205/Actividad5_2.PNG)  

Cambiar a main y agregar modificaciones.
```shell
$ git checkout main
$ echo "Updates to the project." >> Update.md
$ git add Updates.md
$ git commit -m "Update main"
```

![alt text](../Imagenes/Actividad%205/Actividad5_4.PNG)  
![alt text](../Imagenes/Actividad%205/Actividad5_3.PNG)  

Realizar el rebase de `new-feature` sobre `main`.  
```shell
$ git checkout new-feature
$ git rebase main
```

Después de esto, las ramas se verían así:  
![alt text](../Imagenes/Actividad%205/Actividad5_5.PNG)
![alt text](../Imagenes/Actividad%205/Actividad5_6.PNG)

Fusionar y completar el proceso de `git rebase`.  
```shell
$ git checkout main
$ git merge new-feature
```
![alt text](../Imagenes/Actividad%205/Actividad5_7.PNG)
![alt text](../Imagenes/Actividad%205/Actividad5_8.PNG)


### Parte 2: git cherry-pick para la integración selectiva de commit  

Iniciar un nuevo repositorio y hacer cambios:  
```shell
$ mkdir try-cherry-pick
$ cd try-cherry-pick
$ echo "$ My Project" > README.md
$ git add README.md
$ git commit -m "Initial commit"
```

En una nueva rama `add-base-documents` hacer cambios.  
```shell
$ git checkout -d add-base-documents
$ echo "# CONTRIBUTING" >> CONTRIBUTING.md
$ git add CONTRIBUTING.md
$ git commit -m "Add CONTRIBUTING.md"
$ echo "LICENSE" >> LICENSE.txt
$ git add LICENSE.txt
$ git commit -m "Add LICENSE.txt"
```

Ahora las ramas se ven asì:  
![alt text](../Imagenes/Actividad%205/Actividad5_9.PNG)
![alt text](../Imagenes/Actividad%205/Actividad5_10.PNG)

Hacer `cherry-pick` de un commit de `add-base-documents` a `main`.  
```shell
$ git checkout main
$ git cherry-pick 7186855
```
![alt text](../Imagenes/Actividad%205/Actividad5_12.PNG)
![alt text](../Imagenes/Actividad%205/Actividad5_11.PNG)

---
## Preguntas de discusión
// TODO
1. **¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?**
2. **¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?**
1. **¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?**
2. **¿Por qué es importante evitar hacer rebase en ramas públicas?**

## Ejercicios Teóricos

###  1. Diferencias entre git merge y git rebase

Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum

> //TODO  
> //TODO  
> //TODO  

### 2. Relación entre git rebase y DevOps
¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

> //TODO  
> //TODO  
> //TODO  

### 3. Impacto del git cherry-pick en un equipo Scrum  
Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones

> //TODO  
> //TODO  
> //TODO  

## Ejercicios Prácticos  

### 1. Simulación de un flujo de trabajo Scrum con git rebasey git merge  


### 2. Cherry-pick para integración selectiva en un pipeline CI/CD  


## Git, Scrum y Sprints
// TODO

### Fase 1: Planificación del Sprint (Sprint Planning)

**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

// TODO  
// TODO  
// TODO  

¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?
> // TODO  
> // TODO  
> // TODO  

### Fase 2: Desarrollo del Sprint (Sprint Execution)  

**Ejercicio 2: Integración continua con `git rebase`**  

// TODO  
// TODO  
// TODO  

¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?
> // TODO  
> // TODO  
> // TODO  

### Fase 3: Revisión del Sprint (Sprint Review)  

**Ejercicio 3: Integración selectiva con git `cherry-pick`**  

// TODO  
// TODO  
// TODO  

¿Cómo ayuda git cherry-pick a mostrar avances de forma selectiva en un sprint review?

> // TODO  
> // TODO  
> // TODO  

### Fase 4: Retrospectiva del Sprint (Sprint Retrospective)  

**Ejercicio 4: Revisión de conflictos y resolución**

// TODO  
// TODO  
// TODO  

¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?

> // TODO  
> // TODO  
> // TODO  

### Fase de desarrollo: automatización de integración continua (CI) con `git rebase`  

**Ejercicio 5: Automatización de Rebase con Hooks de Git**

// TODO  
// TODO  
// TODO  

¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?.

> // TODO  
> // TODO  
> // TODO  