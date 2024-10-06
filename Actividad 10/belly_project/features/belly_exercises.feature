# language: es
Característica: Característica del Estómago Extendida - Ejercicios
  Esquema del escenario: Comer cukes
    Dado que he comido <cukes> pepinos
    Cuando espero <tiempo>
    Entonces mi estómago <gruñir> gruñir

    Ejemplos:
      | cukes | tiempo                                | gruñir     |
      | 35    | 1 hora y 30 minutos y 45 segundos     | debería    |
      | 0.5   | 2 horas                               | no debería |
      | 20    | "two hours and thirty minutes"        | debería    |
      | 25    | un tiempo aleatorio entre 1 y 3 horas | debería    |
      | 1000  | 10 horas                              | debería    |
      | 50    | "1 hora, 30 minutos y 45 segundos"    | debería    |

  Escenario: Validación de cantidades no válidas
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa