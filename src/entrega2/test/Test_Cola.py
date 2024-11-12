'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from entrega2.tipos.Cola import Cola


print("TEST DE COLA:")
print("################################################")

# Creación de una cola vacía y adición de elementos
cola = Cola.of()
cola.add_all([23, 47, 1, 2, -3, 4, 5])
print(f"Resultado de la cola: {cola}")

print("################################################")

# Eliminar todos los elementos con remove_all
elementos_eliminados = cola.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")