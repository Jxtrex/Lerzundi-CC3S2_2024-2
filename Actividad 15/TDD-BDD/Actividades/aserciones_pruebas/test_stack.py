from unittest import TestCase
from stack import Stack


"""Casos de prueba para la Pila"""


class TestStack(TestCase):

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.stack = Stack()

    def test_is_empty(self):
        """Prueba de si la pila está vacía"""
        stack = Stack()
        assert stack.is_empty() == True  # la pila recién creada está vacía
        stack.push(5)
        assert (
            stack.is_empty() == False
        )  # Después de agregar un elemento la pila no debería estar vacía

    def test_pop(self):
        """Prueba de eliminar un elemento de la pila"""
        self.stack.push(3)  # Agregamos dos elementos a la pila
        self.stack.push(5)
        self.assertEqual(
            self.stack.pop(), 5
        )  # pop retorna el último elemento agregado y lo elimina
        self.assertEqual(
            self.stack.peek(), 3
        )  # peek solo retorna el último elemento agregado
        self.stack.pop()  # Eliminamos el último elemento agregado
        self.assertTrue(self.stack.is_empty())  # Ahora la pila debería estar vacía

    def test_peek():
        """Prueba de observar el elemento superior de la pila"""
        stack = Stack()
        stack.push(1)  # Agregamos elementos a la pila
        stack.push(
            2
        )  # Y no debe cambiar si usamos peek para retornar el último elemento
        assert stack.peek() == 2
        assert stack.peek() == 2

    def test_peek(self):
        """Prueba de observar el elemento superior de la pila"""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.peek() == 1

    def test_push(self):
        """Prueba de insertar un elemento en la pila"""
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
