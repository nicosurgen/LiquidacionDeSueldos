# Importo las funciones creadas para liquidar los sueldos y otras funcionalidades

from App import api
from typing import List

# Voy a definir unas listas con Nombres, Valor por hora y Faltas de empleados para poder ir probando la api

nombres = ["Nicolas","Juan Cruz","Ramiro","Agustin","Charly","Pedro","Gustavo","Noelia","Catalina"]

valorxhora = [3000,3200,2150,1500,4000,1000,1500,2500,2550]

faltas = [2,0,1,0,0,0,3,1,0]

empleados = []
for n,v,f in zip(nombres,valorxhora,faltas):
    empleados.append({
                        "Nombre":n,
                        "Paga por hora":v,
                        "Faltas":f
                    })

""""
        Esto Crea una lista de diccionarios del tipo:
        {"Nombre":...,"Paga por hora":...,"Faltas"}
"""


print(empleados)
