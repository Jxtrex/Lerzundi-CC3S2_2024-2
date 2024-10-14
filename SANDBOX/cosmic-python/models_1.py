from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple


    
    
@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

# Entities, unlike values, have identity equality.
#  We can change their values, and they are still recognizably the same thing.
class Person:
    def __init__(self,name:Name):
        self.name = name


#That's the definition of a value object: any object that is identified only by its data and doesn’t have a long-lived identity
class Money(NamedTuple):
    currency: str
    value: int

    def __add__(self, other) -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value + other.value)

    def __sub__(self, other) -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"Cannot substract {other.currency} from {self.currency}")
        return Money(self.currency, self.value - other.value)

    def __mul__(self, other) -> "Money":
        if isinstance(other, int):
            return Money(self.currency, self.value * other)
        raise TypeError(
            f"Cannot multiply Money by {type(other).__name__}; only scalars are allowed."
        )


Line = namedtuple("Line", ["sku", "qty"])


def test_equality():
    assert Money("gbp", 10) == Money("gbp", 10)
    assert Name("Harry", "Percival") != Name("Bob", "Gregory")
    assert Line("RED-CHAIR", 5) == Line("RED-CHAIR", 5)
