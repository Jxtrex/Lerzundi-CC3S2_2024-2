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

### <ins>**Intrucciones:**</ins>

### Configuración del entorno:
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
### Pipeline CI/CD  

Usaremos Github Actions para CI, por lo que creamos la siguiente estructura  
```
└── 📁devops-practice
    └── 📁.github
        └── 📁workflows
            └── ci.yml
```

Y creamos nuestro archivo `YAML` dónde definiremos **<i>Events</i>**, **<i>Jobs</i>**, **<i>Runners</i>**, **<i>Steps</i>** y <i>**Actions**</i> .  

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

