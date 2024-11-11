'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''

from __future__ import annotations
from typing import TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')


class Cola(Agregado_lineal[E]):
    
    @staticmethod
    def of() -> Cola[E]:
        return Cola()
    
    def add(self, e:E) -> None:
        self._elements.append(e)
        
        
    def __str__(self) -> str:
        elements_str = ", ".join(str(e) for e in self._elements)
        return f'Cola({elements_str})'