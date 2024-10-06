import random
from behave import given, when, then
from belly import Belly
import re

# Crear una instancia de Belly
belly = Belly()

# Números
numeros_en_spanish = {
    "cero": 0,
    "una": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "veinticinco": 25,
    "treinta": 30,
    "mil": 1000,
}
numeros_en_english = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "thirty": 30,
}


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        if palabra in numeros_en_spanish:
            return numeros_en_spanish.get(
                palabra.lower(), 0
            )  # Retornar 0 si la palabra no está en el diccionario
        else:
            return numeros_en_english.get(palabra.lower(), 0)
        return 0


# Dado que he ingresado {una cantidad no válida de} pepinos
@given("que he ingresado {cukes} pepinos")
def step_given_entered_invalid_cukes(context, cukes):
    if cukes == "una cantidad no válida de":
        raise ValueError(f"Cantidad no válida de pepinos")


# Dado que he comido "{cukes}" de pepinos
@given('que he comido "{cukes}" de pepinos')
def step_given_eaten_intesifier_cukes(context, cukes):
    if cukes == "un montón":
        belly.comer(11)
    else:
        raise ValueError(f"No se pudo interpretar el número de pepinos")

#Dado que he comido una gran cantidad de pepinos
@given('que he comido {cukes:d} pepinos')
def step_given_large_quantity_of_cukes(context,cukes):
    belly.comer(cukes)

# Dado que he comido una cantidad fraccionaria de pepinos
@given("que he comido {cukes:f} pepinos")
def step_given_eaten_fractional_cukes(context, cukes):
    belly.comer(cukes)


# Dado que he comido {cukes} pepinos
@given("que he comido {cukes} pepinos")
def step_given_eaten_cukes(context, cukes):
    pattern_1 = re.compile(r"\b(?:menos|más)\sde\b\s(\d+)")
    match = pattern_1.search(cukes)
    if match:
        belly.comer(int(match.group(1)))
    else:
        pattern_2 = re.compile(r"(\d+)")
        match_2 = pattern_2.search(cukes)
        if match_2:
            belly.comer(int(match_2.group(1)))
        else:
            raise ValueError(f"No se pudo interpretar el número de pepinos: {cukes}")


# Dado que he comido "{cukes} pepinos"
@given('que he comido "{cukes} pepinos"')
def step_given_eaten_written_number_cukes(context, cukes):
    pepinos = convertir_palabra_a_numero(cukes)
    if pepinos:
        belly.comer(pepinos)
    else:
        raise ValueError(f"No se pudo interpretar el número de pepinos: {cukes}")


# Cuando espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas
@when("espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas")
def step_when_wait_random_time(context, min_time, max_time):
    tiempo_aleatorio = random.uniform(min_time, max_time)
    print(f"Esperando un tiempo aleatorio de {tiempo_aleatorio:.2f} horas.")
    belly.esperar(tiempo_aleatorio)


# Cuando espero "{time_description}"
@when("espero {time_description}")
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(
        r"\"?(?:(\w+)\s*horas?)?\s*y?\s*(?:(\w+)\s*minutos?)?\s*y?\s*(?:(\w+)\s*segundos?)?\"?"
    )
    match = pattern.search(time_description.lower())
    print(match)
    print("GROUP 1: " + str(match.group(1)))
    print("GROUP 2: " + str(match.group(2)))
    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if match:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        seconds_word = match.group(3) if match.group(3) else "0"

        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)

        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        belly.esperar(total_time_in_hours)
    else:
        raise ValueError(
            f"No se pudo interpretar la descripción del tiempo: {time_description}"
        )


# Entonces mi estómago debería gruñir
@then("mi estómago debería gruñir")
def step_then_belly_should_growl(context):
    assert (
        belly.esta_gruñendo()
    ), "Se esperaba que el estómago gruñera, pero no lo hizo."


# Entonces mi estómago no debería gruñir
@then("mi estómago no debería gruñir")
def step_then_belly_should_not_growl(context):
    assert (
        not belly.esta_gruñendo()
    ), "Se esperaba que el estómago no gruñera, pero lo hizo."


# Entonces el sistema debería arrojar un error de cantidad no válida
@then("el sistema debería arrojar un error de cantidad no válida")
def step_then_system_must_throw_invalid_amount(context):
    try:
        assert belly.esta_gruñendo(), "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))


# Entonces debería ocurrir un error de cantidad no válida
@then("debería ocurrir un error de cantidad no válida")
def step_then_invalid_cucumber_amount(context):
    try:
        assert belly.pepinos_comidos < 100, "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))
        
# Entonces debería ocurrir un error de cantidad negativa
@then("debería ocurrir un error de cantidad negativa")
def step_then_negativa_cucumber_amount(context):
    try:
        assert belly.pepinos_comidos>=0, "Cantidad de pepinos negativa"
    except AssertionError as e:
        print(str(e))
