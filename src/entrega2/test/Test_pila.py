'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from entrega2.tipos.Pila import Pila
print("TEST DE PILA:")
print("################################################")

# Creación de una pila y adición de elementos
pila = Pila.of()
pila.add(5)
pila.add(3)
pila.add(7)
print(f"Resultado de la pila: {pila}")

print("################################################")

# Eliminar todos los elementos con remove_all
elementos_eliminados = pila.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")