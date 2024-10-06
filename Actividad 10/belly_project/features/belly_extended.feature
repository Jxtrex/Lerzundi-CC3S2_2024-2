# language: es
Característica: Característica del Estómago Extendida
  Escenario: Comer diferentes cantidades de pepinos en varios tiempos
    Dado que he comido 30 pepinos
    Cuando espero "una hora y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos sin especificar cantidad exacta
    Dado que he comido "un montón" de pepinos
    Cuando espero 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar un tiempo exacto en minutos
    Dado que he comido 20 pepinos
    Cuando espero 120 minutos
    Entonces mi estómago debería gruñir
  
  Escenario: Comer pepinos en palabras y tiempos en minutos
    Dado que he comido "veinticinco pepinos"
    Cuando espero "noventa minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad no válida de pepinos
    Dado que he comido "mil pepinos"
    Cuando espero 2 horas
    Entonces debería ocurrir un error de cantidad no válida
  
  Escenario: Comer pepinos y esperar en segundos
    Dado que he comido 40 pepinos
    Cuando espero "3600 segundos"
    Entonces mi estómago debería gruñir
  
  Escenario: Comer pepinos y esperar en inglés
    Dado que he comido 15 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir
  
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir
  
  Escenario: Comer medio pepino y esperar
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer una cantidad negativa de pepinos
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa

  Escenario: Comer grandes cantidades de pepinos y esperar mucho tiempo
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir