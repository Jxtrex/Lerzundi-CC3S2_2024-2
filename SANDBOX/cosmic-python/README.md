# cosmic-python Book
# Domain Modeling

## Ejecución
1. Instala los paquetes necesarios:  
```shell
# https://pytest-cov.readthedocs.io/en/latest/index.html
pip install -r requirements.txt
``` 
2. Ejecuta pytest-cov:
```python
# Módulo en específico
pytest --cov=my_module

# Todo el workdir, exportar a HTML en dir y un archivo contiene los tests
pytest --cov=. --cov-report=html:dir test_batches.py
```
