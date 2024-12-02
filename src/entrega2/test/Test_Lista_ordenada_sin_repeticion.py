'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion


print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
print("################################################")

# Creación de una lista con criterio de orden lambda x: -x
lista_sin_rep = Lista_ordenada_sin_repeticion.of(lambda x: -x)
for valor in [23, 47, 47, 1, 2, -3, 4, 5]:
    lista_sin_rep.add(valor)
print(f"Resultado de la lista ordenada sin repetición: {lista_sin_rep}")

print("################################################")

# Eliminar un elemento con remove
elemento_eliminado = lista_sin_rep.remove()
print(f"El elemento eliminado al utilizar remove(): {elemento_eliminado}")

print("################################################")

# Eliminar todos los elementos con remove_all
elementos_eliminados = lista_sin_rep.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")

print("################################################")

# Comprobación de posición correcta
lista_sin_rep.add(0)
print(f"Lista después de añadirle el 0: {lista_sin_rep}")
lista_sin_rep.add(0)
print(f"Lista después de añadirle el 0: {lista_sin_rep}")
lista_sin_rep.add(7)
print(f"Lista después de añadirle el 7: {lista_sin_rep}")