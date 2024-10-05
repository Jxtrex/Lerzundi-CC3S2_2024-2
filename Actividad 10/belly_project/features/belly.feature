# language: es
Característica: Característica del Estómago
  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido más de 10 pepinos
    Cuando espero al menos 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido menos de 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido más de 10 pepinos
    Cuando espero menos de 1 hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido más de 10 pepinos
    Cuando espero al menos 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos de tiempo
    Dado que he comido más de 10 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
  
  Escenario: comer diferentes cantidades de pepinos y esperar en varios tiempos
    Dado que he comido más de 10 pepinos
    Cuando espero "una hora y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos sin especificar una cantidad exacta
    Dado que he comido "un montón" de pepinos
    Cuando espero 3 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar un tiempo exacto en minutos
    Dado que he comido más de 10 pepinos
    Cuando espero 120 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos expresados en palabras y esperar el tiempo en minutos
    Dado que he comido "veinticinco pepinos"
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer una cantidad no válida de pepinos
    Dado que he ingresado una cantidad no válida de pepinos
    Cuando espero cualquier cantidad de tiempo
    Entonces el sistema debería arrojar un error de cantidad no válida