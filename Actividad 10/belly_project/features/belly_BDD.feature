# language: es
Característica: Característica del Estómago para BDD
  Escenario: Comer muchos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir
  
  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 15 pepinos
    Entonces debería haber comido 15 pepinos
  
  Escenario: Verificar que el estómago gruñe después de comer suficientes pepinos y esperar el tiempo correcto
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
  
  Escenario: Predecir si mi estómago gruñirá tras comer y esperar
    Dado que he comido 12 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir