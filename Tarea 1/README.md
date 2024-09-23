# Juego de Trivia con FastAPI, PostgreSQL y DevOps  
Juego de trivia dónde respondes una serie de preguntas de opción múltiple presentadas por consola.
### Reglas y funcionamiento
- **Inicio:** Al iniciar el juego se muestra un mensaje de bienvenida.
- **Rondas:** El juego consta de 10 rondas cada una con respuesta única.
- **Preguntas:** Cada pregunta tiene cuatro opciones de respuesta.
- **Selección de respuesta:** El jugador elige una respuesta ingresando el número correspondiente.
- **Puntuación:** Cada respuesta otorga un punto, no hay puntos en contra.
- **Fin del Juego:** Al final se muestra la puntuación del jugador, junto con la cantidad de respuesta correctas e incorrectas.

# Construcción del juego
## Sprint 1

### Objetivo: Configurar el entorno del proyecto y desarrollar la lógica básica para la manipulación y presenrtación de preguntas y respuesta  

1. Configuración del proyecto con FastAPI y Docker:  
```shell
$ mkdir Sprint\ 1
$ cd Sprint\ 1
$ mkdir trivia-game-python
$ cd trivia-game-python
$ python3 -m venv venv
```

> En este caso se usa la interfaz de vscode para crear el .venv

```shell
$ source .venv\Scripts\activate
$ pip install fastapi uvicorn
$ pip install asyncpg databases
```

Creamos un Dockerfile para el entorno de FastAPI y PostgreSQL.

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r  requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host","0.0.0.0","--port","8000"]
```

Y un archivo docker-compose.yml  

**docker-compose.yml**
```yml
version: '3.8'

services:
  db:
    image: postgres:13
    
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: trivia_db
    
    ports:
      - "5432:5432"
    
  web:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      DATABASE_URL: postgres://user:password@db:5432/trivia_db
    depends_on:
      - db
```
2. Implementación de la clase `Question`:  

**trivia.py**  
```python
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
    def is_correct(self, answer):
        return self.correct_answer == answer
```

3. Implementación de la clase `Quiz`:  

**trivia.py**
```python
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
    def add_question(self, question):
        self.questions.append(question)
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
```

4. Configuración de pytest y pruebas unitarias para la clase Question  

```shell
$ pip install pytest
```
**test_trivia.py**
```python
import pytest
from trivia import Question
def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")
```  

![alt text](../Imagenes/Tarea%201/Tarea1_1.PNG)  