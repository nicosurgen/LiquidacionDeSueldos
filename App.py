# Importo las funciones creadas para liquidar los sueldos y otras funcionalidades

import liquidacion as lq
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

# Creo una funcion que al utilizarla pueda usar todas las funcionalidades creadas para mi app

def api(empleados:List[int]):
    seguir = True
    print("Opciones a elegir:\n1: Agregar empleados\n2: Modificar datos de empleado\n3: Liquidar sueldo\n4: Obtener estadísticas")
    while seguir:
        opcion = input("Elija la opción deseada: ")
        try:
            opcion = int(opcion)
        except:
            print("Por favor elija una de las opciones validas")
        if opcion in [1,2,3,4]:
            seguir = False
        else:
            print("Por favor elija una de las opciones validas")
    
    # Opcion para Agregar empleados
    
    if opcion == 1:
        while True:
            try: 
                cantidad = int(input("Ingrese la cantidad de empleados a agregar: "))
                break
            except:
                print("Tenes que ingresar un número entero")
        lq.CargarEmpleados(Empleados=empleados,Cantidad=cantidad)
        
    # Opción para Modificar los datos de un empleado
    
    elif opcion == 2:
        while True:
            try: 
                numempleado = int(input("Ingrese el indice del empleado a modificar: "))
                break
            except:
                print("Tenes que ingresar un número entero")
        lq.ModificarDatos(Empleados=empleados,NumEmpleado=numempleado)
        
    #Obtener la liquidación de sueldos
    
    elif opcion == 3:
        while True:
            try: 
                jornadamensual = int(input("Ingrese el número de horas mensuales trabajadas: "))
                break
            except:
                print("Tenes que ingresar un número entero")
                
        return lq.LiquidacionCompleta(empleados=empleados,jornadamensual=jornadamensual)
    
    # Obtener estadísticas
    
    elif opcion == 4:
        
        return lq.estadisticas(empleados=empleados)