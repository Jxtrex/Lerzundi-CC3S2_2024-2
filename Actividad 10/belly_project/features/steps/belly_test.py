from belly import Belly


def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15
    
def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
    
def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True