# Actividad 1

**Preguntas de Reflexión(Sobre la lectura 1)**
- **¿Por qué surgió la necesidad de DevOps en el desarrollo de software?**  
> Por las consecuencias de la separación marcada de las responsabilidades entre el equipo de Desarrollo y el de Operaciones de IT. Estas son: la falta de comunicación efectiva, la carencia de un plan organizado que incluya a los dos equipos y el costo temporal necesario para adecuar el software a los estándares que tenía cada equipo.
- **Describe cómo el principio de mejora continua afecta tanto a los aspectos técnicos como culturales de una organización.**  
> En el aspecto técnico la mejora continua asegura que el software mantenga un estándar de calidad, que sea fácilmente mutable y eficiente , lo que culmina con el fortalecimiento de la entrega de software. En el aspecto cultural la mejora continua contribuye a la eliminación de los silos en las organizaciones teniendo como eje central el desarrollo colaborativo el cual otorga a cada participante una tarea de la que pueda sentirse responsable y que al culminarla le otorge realización personal.  
- **¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?**  
> Que reducir DevOps a alguna de esas cosas merma considerablemente el significado real de DevOps. Si nos centramos en las herramientas, podemos adecuar herramientas diseñadas para DevOps a metodologías lineales y arcaicas; si nos centramos en personas, se crean roles centrados en la aplicación de DevOps que reducen esta filosofía al accionar de una persona sin considerar la cultura de la empresa que lo rodea; si nos centramos en procesos, la definición de DevOps abarca más allá de la etapa de construcción del software por lo que limitarse a la etapa de desarrollo incide en un error de la propia definición de la filosofía DevOps.
- **Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?**  
> Los equipos usan esa autonomía para realizar decisiones rápidas y relevantes respecto al ciclo completo del software y su posterior mantenimiento, esto agiliza el proceso creativo y otorga adaptabilidad frente a los cambios.  
- **Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado ha llevado a la creación de DevOps.**  
> Habiendo sido reconocido el problema de la falta de comunicación las organizaciones se dieron a la tarea de implementar medidas que contrarresten esta limitación, DevOps nació como una solución tentativa a este problema, teniendo como característica el ir en una dirección contraria a muchas de las taras que sufrían los euqipos involucrados como: apostar por la integración entre IT y Devs en vez de respetar silos establecidos, integración continua en vez de lanzamientos poco frecuentes y más estables, llevar la infraestructura al campo del código de configuración (Docker), responsabilidad compartida en aras de la solución de problemas.  
<hr></hr>

Aplicar los conceptos de DevOps en un entorno práctico, configurando un pipeline básico de CI/CD para
un proyecto de software y experimentando con la automatización de procesos en un entorno local
utilizando Docker.

 <big><big><big><ins>**Instrucciones:**</ins></big></big></big>

## Configuración del entorno:
Dentro de `/devops-practice/` creamos un proyecto con npm  

- `npm init -y`: inicializa un proyecto y omite las preguntas

Esto nos generará **package.json**

```json
{
  "name": "devops-practice",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}
```
Instalamos dependencias  

- `npm install express jest supertest`  

Creamos la estructura que usaremos para el proyecto  

```
└── 📁devops-practice
    └── 📁src
        └── app.js
    └── 📁tests
        └── app.test.js
```

Implementamos nuestra **API REST** dentro de `src/app.js`  

<big>****app.js****</big>  

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

module.exports = app;
```

Escribimos un test en `tests/app.test.js`  

<big>**app.test.js**</big>

```javascript
const request = require('supertest');

const app = require('../src/app');

describe('GET /', () => {
    it('should return Hello, World!', async () => {
        const res = await request(app).get('/');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('Hello, World!');
    });
});
```

Configuramos el script de test en `package.json`  

<big>**package.json**</big>  

```json
{
  "name": "devops-practice",
  "version": "1.0.0",
  "scripts": {
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "jest": "^27.0.0",
    "supertest": "^6.1.3"
  }
}
```
## Pipeline CI/CD  

### Parte 1: Configura integración continua (CI) con Github Actions  

Usaremos Github Actions para CI, por lo que creamos la siguiente estructura  
```
└── 📁Lerzundi-CC3S2_2024-2
    └── 📁.github
        └── 📁workflows
            └── ci.yml
```
Nuestra carpeta .githubd tiene que estar en el primer nivel dentro de nuestro repositorio, de otro modo github no lo reconocerá como workflow válido.


Luego creamos nuestro archivo `YAML` dónde definiremos **<i>Events</i>**, **<i>Jobs</i>**, **<i>Runners</i>**, **<i>Steps</i>** y <i>**Actions**</i> .  

<big>**ci.yml**</big>

```yml
name: CI Pipeline

on:
    push:
        branches:
            - main
    pull_request:
        branches:
            - main

jobs:
    build:
        runs-on: ubuntu-latest

        steps:
            - name: Checkout code
              uses: actions/checkout@v2

            - name: Set up Node.js
              uses: actions/setup-node@v2
              with:
                node-version: '14'
            - name: Install dependencies
              run: npm install

            - name: Run tests
              run: npm test
```

Si hacemos push luego de crear este archivo podremos ver como Github ejecuta automáticamente ejecuta este workflow:

![alt text](../Imagenes/Actividad%201/Actividad1_4.PNG)  

### Parte 2: Configura entrega continua (CD) con Docker  

Creamos nuestro dockerfile para inicializar nuestro contenedor:

**Dockerfile**

```dockerfile
# Usa la imagen oficial de Node.js
FROM node:14

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 3000

# Comando para iniciar la aplicación
CMD [ "node" , "src/app.js"]
```
Nos ubicamos en el directorio `/Actividad 1/devops-practice/` en donde está nuestro archivo `Dockerfile` y construimos una nueva imagen Docker a partir de este archivo  

```shell
$ docker build -t devops-practice .
```

Usamos `docker images` para verificar que se creó la imagen correctamente  

![alt text](../Imagenes/Actividad%201/Actividad1_1.PNG)  

Creamos un contenedor a partir de nuestra imagen  

```shell
$ docker run -p 3000:3000 devops-practice
```
![alt text](../Imagenes/Actividad%201/Actividad1_2.PNG)  
![alt text](../Imagenes/Actividad%201/Actividad1_3.PNG)  

## Automatiza el despliegue con Github Actions:  

### Actualiza el archivo `.github/workflows/ci.yml` para construir y desplegar la imagen de Docker:

```yaml
- name: Run Docker image
  run: docker build -t devops-practice .

- name: Run Docker container
  run: docker run -d -p 3000:3000 devops-practice
```

### Verifica que la aplicación se despliegue correctamente localmente usando Docker:

Verificamos que la aplicación se ejecute correctamente yendo a loca `http://localhost:3000`  

![alt text](../Imagenes/Actividad%201/Actividad1_5.PNG)  

### Automatización  

Usamos docker compose para definir el entorno de nuestra aplicación  

<big>**docker-compose.yml**</big>  

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```
Corremos la aplicación desde nuestro archivo .yml  

```shell
$ docker compose up --build -d
```
![alt text](../Imagenes/Actividad%201/Actividad1_6.PNG)  

Y podemos comprobar que el contenedor se está ejecutando correctamente  
![alt text](../Imagenes/Actividad%201/Actividad1_7.PNG) 

Y que nuestro mensaje `Hello, World!` se visualiza correctamente en la dirección `http://localhost:3000/`  

![alt text](../Imagenes/Actividad%201/Actividad1_8.PNG)

## Conclusiones

El uso de CI nos permite ahorrar tiempo usado en filtrar y analizar el código que estamos subiendo y mediante un criterio estandarizado dentro de nuestra organización, aceptar que se integre a nuestra línea principal de desarrollo o no. En este caso solo hemos usado CI para definir el entorno básico de Node.js y correr un test básico, sin embargo ya podemos reconocer la utilidad que tiene el automatizar el proceso de integración de código.

Para el caso de CD usamos docker y docker compose, el primero nos permite aislar el entorno dónde reside nuestra aplicación, el segundo nos permite hacer lo mismo para múltiples contenedores con las mismas espicificaciones. Esto nos permite asegurar la reproducibilidad de nuestra aplicación, lo que permite al equipo encargado del mantenimiendo de código trabajar con la misma versión del software. 

El procesor completo permite delimitar las funciones del tratamiento de software y minimiza las probabilidades de errores por incompatibilidad, revisiones no supervisadas y conflictos al implementar nuevas funcionalidades. Por consiguiente, los desarrolladores puede concentrarse en la construcción del código sabiendo que pueden integrar su contribución al proyecto con seguridad y respeto de los lineamientos de calidad, por otro lado el equipo de operaciones puede dedicarse al soporte del código bajo condiciones determinísticas, es decir, que cumplan con las expectativas que tienen del código y que no tengan el riesgo de variar en medio del proceso de mantenimiento de código.

