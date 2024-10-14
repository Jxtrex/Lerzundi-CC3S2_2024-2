from models_1 import Money, Name, Person
import pytest

fiver = Money("gbp", 5)
tenner = Money("gbp", 10)


def test_can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner


def test_can_substract_money_values():
    assert tenner - fiver == fiver


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money("usd", 10) + Money("gbp", 10)


def test_can_multiply_money_by_a_number():
    assert fiver * 5 == Money("gbp", 25)


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver


def test_name_equality():
    assert Name("Harry", "Percival") != Name("Barry", "Percival")


def test_barry_is_harry():
    harry = Person(Name("Harry", "Percival"))
    barry = harry

    barry.name = Name("Barry", "Percival")
    assert harry is barry and barry is harry
