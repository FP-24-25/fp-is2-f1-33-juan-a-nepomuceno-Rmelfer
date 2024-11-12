'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''

# from __future__ import annotations
# from typing import List, TypeVar, Tuple
# from entrega2.tipos.Agregado_lineal import Agregado_lineal
#
# E = TypeVar('E')
# P = TypeVar('P')
#
#
# class Cola_prioridad(Agregado_lineal[E]):
#
#     def __init__(self):
#         super().__init__()
#         self._priorities: List[P] = []
#
#
#     @staticmethod 
#     def of() -> Cola_prioridad[E, P]:
#         return Cola_prioridad()
#
#
#     @property
#     def priorities(self) -> List[P]:
#         return self._priorities[:]
#
#     def add(self, e: E, priority: P) ->None:
#         index = 0 
#
#         for existing_priority in self._priorities:
#             if priority < existing_priority:
#                 break
#             index += 1
#         self._elements.insert(index, e)
#         self._priorities.insert(index, priority)
#
#
#     def add_all(self, ls: List[Tuple[E, P]]) -> None:
#         for element, priority in ls: 
#             self.add(element, priority)
#
#     def remove(self) -> List[E]:
#         assert len(self._elements) > 0, 'El agregado esta vacio'
#         self._priorities.pop(0)
#         return self._elements.pop(0)
#
#     def remove_all(self) -> List[E]:
#         removed_elements = []
#         while not self.is_empty:
#             removed_elements.append(self.remove())
#         return removed_elements
#
#
#     def decrease_priority(self, e: E, new_priority: P) -> None:
#         if e in self._elements:
#             current_index = self._elements.index(e)
#             current_priority =self._priorities[current_index]
#             if new_priority < current_priority:
#                 self._elements.pop(current_index)
#                 self._priorities.pop(current_index)
#                 self.add(e, new_priority)
#
#
#     def __str__(self) -> str:
#         elements_with_priorities = ", ".join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities))
#         return f"ColaPrioridad({elements_with_priorities})"
#

    
from __future__ import annotations
from typing import List, TypeVar, Tuple, Generic
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
P = TypeVar('P')

class Cola_prioridad(Agregado_lineal[E], Generic[E, P]):
    def __init__(self):
        super().__init__()
        self._priorities: List[P] = []

    @staticmethod
    def of() -> Cola_prioridad[E, P]:
        return Cola_prioridad()

    @property
    def priorities(self) -> List[P]:
        return self._priorities[:]

    def __index_order(self, priority: P) -> int:
        index = 0
        for existing_priority in self._priorities:
            if priority < existing_priority:
                break
            index += 1
        return index

    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for element, priority in ls:
            self.add(element, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            current_index = self._elements.index(e)
            current_priority = self._priorities[current_index]
            if new_priority < current_priority:
                self._elements.pop(current_index)
                self._priorities.pop(current_index)
                self.add(e, new_priority)

    def __str__(self) -> str:
        elements_with_priorities = ", ".join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities))
        return f"ColaPrioridad[{elements_with_priorities}]"

    
    
    
    
    
    
    
    
    
            