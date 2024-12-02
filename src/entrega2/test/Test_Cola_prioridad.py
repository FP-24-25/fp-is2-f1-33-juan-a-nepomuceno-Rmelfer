'''
Created on 10 nov 2024

@author: raulmelgarfernandez
'''
from entrega2.tipos.Cola_prioridad import Cola_prioridad




def test_cola_prioridad():
    cola = Cola_prioridad[str,int]()
    
    cola.add('Paciente A', 3)
    cola.add('Paciente B', 2)
    cola.add('Paciente C', 1)
    
    assert cola.elements==['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto"
    
    atencion = []
    while not cola.is_empty:
        atencion.append(cola.remove())
    
    assert atencion == ["Paciente C", "Paciente B", "Paciente A"], "El orden de atencion no es correcto"
    
    print("Pruebas superadas exitosamente")
    
    

if __name__ == '__main__':
    test_cola_prioridad()