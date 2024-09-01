# Actividad 1

**Preguntas de Reflexión(Sobre la lectura 1)**
- **¿Por qué surgió la necesidad de DevOps en el desarrollo de software?**
- **Describe cómo el principio de mejora continua afecta tanto a los aspectos técnicos como culturales de una organización.**
- **¿Qué significa que DevOps no se trata solo de herramientas, individuoso procesos?**
- **Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?**

- **Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado ha llevadoa la creación de DevOps.**
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

- `npm install express jest`  

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