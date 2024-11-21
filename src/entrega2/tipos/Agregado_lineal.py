'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''


from __future__ import annotations
from typing import List, TypeVar, Generic, Callable
from abc import ABC, abstractmethod



E = TypeVar('E')


class Agregado_lineal(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: List[E] = []
    
    @property
    def size(self) -> int:
        return len(self._elements)
    
    
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    
    @property
    def elements(self) -> List[E]:
        return self._elements[:]
    
    
    @abstractmethod
    def add(self, e : E) -> None:
        pass
    
    
    def add_all(self, ls: List[E]) -> None:
        for element in ls:
            self.add(element)
            
            
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado esta vacio'
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements



    ############## MODIFICACIONES DEFENSA 2 ##############
    @abstractmethod 
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):  # Verifica si se cumple la condicion en cada elemento.
                return element
        return None  # Devuelve None en caso de q ninguno la cumpla.
    #####################################################


