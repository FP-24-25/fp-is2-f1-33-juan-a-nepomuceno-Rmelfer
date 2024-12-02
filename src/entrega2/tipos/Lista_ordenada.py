'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from __future__ import annotations
from _typing import TypeVar
from typing import Callable
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(Agregado_lineal[E]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self.__order = order 
        
        
    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada[E, R]:
        return Lista_ordenada(order)
    
    
    def __index_order(self, e: E) -> int:
        index = 0
        for existing in self._elements:
            if self.__order(e) < self.__order(existing):
                break
            index += 1
        return index
    
    
    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)


    def __str__(self) -> str:
        elements_str = ", ".join(str(e) for e in self._elements)
        return f'ListaOrdenada({elements_str})'





