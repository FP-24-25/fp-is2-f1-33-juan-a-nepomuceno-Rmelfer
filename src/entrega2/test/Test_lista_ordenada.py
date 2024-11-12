'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from entrega2.tipos.Lista_ordenada import Lista_ordenada


print("TEST DE LISTA ORDENADA:")
print("################################################")

# Creación de una lista con criterio de orden lambda x: x
lista = Lista_ordenada.of(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)
print(f"Resultado de la lista: {lista}")

print("################################################")

# Eliminar un elemento con remove
elemento_eliminado = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {elemento_eliminado}")

print("################################################")

# Eliminar todos los elementos con remove_all
lista.add(3)
lista.add(1)
lista.add(2)
elementos_eliminados = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")

print("################################################")

# Comprobación de posición correcta
lista.add(3)
lista.add(1)
lista.add(2)
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")
lista.add(10)
print(f"Lista después de añadirle el 10: {lista}")
lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")