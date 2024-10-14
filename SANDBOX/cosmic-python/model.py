from dataclasses import dataclass
from datetime import date
from typing import List, NewType, Optional, Set

# That would allow our type checker to make sure that we don’t pass a Sku where a Reference is expected, for example.
Quantity = NewType("Quantity", int)
Reference = NewType("Reference", str)
Sku = NewType("Sku", str)
OrderReference = NewType("OrderReference", Reference)
ProductReference = NewType("ProductReference", Reference)


# OrderLine is an immutable dataclass with no behavior.
@dataclass(frozen=True)
class OrderLine:
    orderid: OrderReference
    sku: ProductReference
    qty: Quantity


# We can allocate lines to a batch, or change the date that we expect it to arrive, and it will still be the same entity. We usually make this explicit in code by implementing equality operators on entities
class Batch:

    def __init__(self, ref: Reference, sku: Sku, qty: Quantity, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[OrderLine]

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference


    # Typically, __hash__ is implemented in classes that are immutable (like Value Objects) to ensure that the hash value remains consistent throughout the object's lifetime
    # For value objects, the hash should be based on all the value attributes, and we should ensure that the objects are immutable. We get this for free by specifying @frozen=True on the dataclass
    # For entities, the simplest option is to say that the hash is None
    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty


# Domain Service Function
def allocate(line: OrderLine, batches: List[Batch]) -> str:
    batch = next(b for b in sorted(batches) if b.can_allocate(line))
    batch.allocate(line)
    return batch.reference

class OutOfStock(Exception):
    pass
