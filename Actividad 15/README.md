# Actividad 15: TDD y pytest

### Tecnologías Usadas
- Docker o Docker Desktop (Windows 10)
- Extensión Dev Containers para vscode (ms-vscode-remote.remote-containers)

## Escribir aserciones en pruebas con pytest

**Objetivos:**  
- Ejecutar casos de prueba con pytest
- Identificar los casos de prueba que fallan
- Escribir pruebas unitarias utilizando aserciones
- Generar informes de cobertura usando pytest-cov

Instalamos pytest y pytest-cov para nuestras pruebas y cobertura de código respectivamente:  

```shell
# Añadida a requirements.txt
python3 -m pip install pytest pytest-cov
```

Nos dirigimos a la carpeta TDD-BDD que es donde se encuentra nuestro proyecto y abrimos vscode:  
```shell
# Ubuntu
cd Actividad\ 15/TDD-BDD/
code .
```

Usaremos los archivos **stack.py** y **test_stack.py** que ya están creados:  
- **stack.py:** La implementación de una pila
  1. push()
  2. pop()
  3. peek()
  4. is_empty() 
- **test_stack.py:** Contiene las pruebas para la pila

Corremos nuestras pruebas con --verbose y --random-order

```shell
pytest --verbose --random-order  Actividades/aserciones_pruebas/
```
![alt text](../Imagenes/Actividad%2015/Actividad15_1.PNG)
Todas las pruebas fallan porque no hemos implementado ningún test

Implementamos pruebas para **pop()** y **is_empty()**:  
```python
def test_is_empty(self):
    stack = Stack()
    assert stack.is_empty() == True  
    stack.push(5)
    assert (
        stack.is_empty() == False
    )  

def test_pop(self):
    self.stack.push(3)  
    self.stack.push(5)
    self.assertEqual(self.stack.pop(), 5)  
    self.assertEqual(self.stack.peek(), 3)  
    self.stack.pop()  
    self.assertTrue(self.stack.is_empty())  
```
Corremos **pytest** :    
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_2.PNG)

```python
Implementamos pruebas para **peek()**:  
def test_peek():
        stack = Stack()
        stack.push(1)  
        stack.push(2)  
        assert stack.peek() == 2
        assert stack.peek() == 2

def test_peek(self):
    self.stack.push(3)
    self.stack.push(5)
    self.assertEqual(self.stack.peek(), 5)
```

Corremos **pytest**:  
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_3.PNG)
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_4.PNG)

Implementamos las últimas pruebas para **push()**:  
```python
def test_push(self):
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 2
```

Corremos **pytest**:  
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_5.PNG)

Corremos **pytest-cov**:  
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_6.PNG)

Creamos un archivo **setup.cfg** que contendrá la configuración para la ejecución de las pruebas y el informe de cobertura de código:  

**setup.cfg**
```shell
[tool:pytest]
addopts = -v --random-order --tb=short --cov=stack --cov-report=term-missing

[coverage:run]
branch = True
omit =
    */tests/*
    */test_*

[coverage:report]
show_missing = True
```

Corremos **pytest** sin ningún comando adicional:  
![alt text](../Imagenes/Actividad%2015/Actividad15-aserciones_pruebas_7.PNG)

## Cobertura de pruebas