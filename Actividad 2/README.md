# Actividad 2

// TODO
**Preguntas de Reflexión(Sobre la lectura 2)**
- **¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?.**
- **Explica cómo IaC mejora la consistencia y escablabilidad en la gestión de infraestructuras.**
- **¿Cuál es la diferencia entre monitorio y observabilidad?¿Por qué es crucial la observabilidad en sistemas complejos?.**
- **¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?**
- **Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.**
- **¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**

<hr></hr>

>[!IMPORTANT] Se usará el proyecto devops-practice de la Actividad 1 con mínimas modificaciones para esta Actividad 2.  

Aplicar los conceptos de DevSecOps, IaC, y Observabilidad en un entorno práctico, utilizando herramientas que permiten integrar seguridad, gestionar infraestructura como código, y mejorar la visibilidad del sistema en tiempo real.


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

## Implementación de DevSecOps

### Integración de Seguridad

Usamos `npm audit` para detectar vulnerabilidades en las dependencias. 

![alt text](../Imagenes/Actividad%202/Actividad2_1.PNG)  

Automatizamos el análisis de seguridad en Github Actions:  

**<big>ci.yml</big>**

## Implementación de Infraestructura como Código (IaC)

### Usa Docker para contenerizar la aplicación:

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

### Automatiza la gestión de contenedores usando Docker Compose:  

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

## Implementación de Observabilidad

### Configura Prometheus y Grafana

Creamos el archivo de configuración de Prometheus  

**<big>prometheus.yml</big>**  

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node-app'
    static_configs:
      - targets: ['app:3000']
```

Y añadimos a nuestro archivo `docker-compose.yml` la configuración para Prometheus y Grafana

**<big>docker-compose.yml</big>**

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production

# Comandos de la Actividad 2

  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
  
  grafana:
    image: grafana/grafana
    ports:
      - "3001:3001"
```

## Conclusiones