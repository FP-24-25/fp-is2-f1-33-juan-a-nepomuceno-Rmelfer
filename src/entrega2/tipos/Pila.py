'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from __future__ import annotations
from _typing import TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal




E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    
    @staticmethod
    def of() -> Pila[E]:
        return Pila()
    
    def add(self, e:E) -> None:
        self._elements.insert(0, e)
        
        
    def __str__(self) -> str:
        elements_str = ", ".join(str(e) for e in self._elements)
        return f'Pila({elements_str})'