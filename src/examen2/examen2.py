'''
Created on 21 nov 2024

@author: raulmelgarfernandez
'''
from __future__ import annotations
from typing import TypeVar, Callable
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self._capacidad = capacidad  # Capacidad máxima 

    @staticmethod
    def of(capacidad: int) -> ColaConLimite[E]:
        return ColaConLimite(capacidad)

    def add(self, e: E) -> None:
        if self.is_full:
            raise OverflowError("La cola está llena")  # Lanzar excepción si la cola está llena
        self._elements.append(e)  # Anade elemento al final de la cola

    @property
    def is_full(self) -> bool:
        return len(self._elements) >= self._capacidad  # True si cola está llena

    def __str__(self) -> str:
        elements_str = ", ".join(str(e) for e in self._elements)
        return f"ColaConLimite({elements_str})"
    
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):  # Verifica si se cumple la condicion en cada elemento.
                return element
        return None  # Devuelve None en caso de q ninguno la cumpla.
    
    
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        return [element for element in self._elements if func(element)]
    
    
cola = ColaConLimite(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")
try: 
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
print(cola.remove())

######## TESTS ########


#ColaConLimite
cola = ColaConLimite.of(3)

cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)

assert cola.remove() == "Tarea 1"
assert cola.contains("Tarea 2")
assert not cola.contains("Tarea 1")

#contains
cola = ColaConLimite.of(10)
cola.add_all([1, 2, 3, 4, 5])
assert cola.contains(3)
assert not cola.contains(10)

#find
cola = ColaConLimite.of(10)  # Capacidad suficientemente alta para pruebas
cola.add_all([1, 2, 3, 4, 5])

assert cola.find(lambda x: x > 3) == 4
assert cola.find(lambda x: x > 10) is None

#filter
cola = ColaConLimite.of(10)  # Capacidad suficientemente alta para pruebas
cola.add_all([1, 2, 3, 4, 5, 6])

assert cola.filter(lambda x: x > 3) == [4, 5, 6]
assert cola.filter(lambda x: x % 2 == 0) == [2, 4, 6]









