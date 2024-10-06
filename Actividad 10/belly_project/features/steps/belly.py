# src/belly.py
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):

        if pepinos >= 0:
            print(f"He comido {pepinos} pepinos.")
            self.pepinos_comidos += pepinos
        else:
            print("La cantidad de pepinos debe ser positiva.")

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")

        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if (
            self.tiempo_esperado >= 1.5
            and self.pepinos_comidos > 10
            and self.pepinos_comidos != -1
        ):
            # Reseteamos el número de pepinos
            self.pepinos_comidos = 0
            return True
        if self.pepinos_comidos < 5:
            return False
        return False
