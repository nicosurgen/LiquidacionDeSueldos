from typing import List,Tuple,Dict

# Funciones Para cargar empleados

def CargarEmpleado(Empleados: List[Dict]): # -> Sirve para cargar un empleado a la lista de empleados 
  while True:
    nombre = input("Ingrese el nombre del empleado: ")
    pagaxhora = float(input("Ingrese la paga por hora del empleado: "))
    Empleado = {
                  "Nombre": nombre,
                  "Paga por hora": pagaxhora,
                  "Faltas": 0
                }
    print(Empleado)
    print("Los datos correctos?")
    Flag = True
    while Flag:
      respuesta = input()
      respuesta = respuesta.lower()
      if respuesta in ("si","no"):
        Flag = False
      else: print("Tenes que ingresar si o no")
    if respuesta == "si":
      break

  Empleados.append(Empleado)

def CargarEmpleados(Empleados: List[Dict], Cantidad: int): # -> Sirve para cargar 1 o mas empleados a la lista
  for i in range(1,Cantidad+1):
    print(f"Cargando Empleado {i}")
    CargarEmpleado(Empleados)
    
# FUncion para modificar datos de un empleado
def ModificarDatos(Empleados: List[Dict],NumEmpleado: int): # -> Sirve para modificar los datos de un empleado utilizando su indice 
  seguir = True
  print("Opciones de cambio:\n1: Nombre\n2: Paga por hora\n3: Faltas")
  while seguir:
    opcion = input("Elija la opción deseada: ")
    try:
      opcion = int(opcion)
    except:
      print("Por favor elija una de las opciones validas")
    if opcion in [1,2,3]:
      seguir = False
    else:
      print("Por favor elija una de las opciones validas")

  if opcion == 1:
    while True:
      nombre = input("Ingrese el nombre del empleado: ")
      print(f"Se va a remplazar el nombre por: {nombre}")
      print("Quiere guardar los cambios?")
      Flag = True
      while Flag:
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta in ("si","no"):
          Flag = False
        else: print("Tenes que ingresar si o no")
      if respuesta == "si":
        break
    Empleados[NumEmpleado]["Nombre"] = nombre

  elif opcion == 2:
    while True:
      pagaporhora = float(input("Ingrese la paga por hora del empleado: "))
      print(f"Se va a remplazar la paga por hora por: ${pagaporhora}")
      print("Quiere guardar los cambios?")
      Flag = True
      while Flag:
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta in ("si","no"):
          Flag = False
        else: print("Tenes que ingresar si o no")
      if respuesta == "si":
        break
    Empleados[NumEmpleado]["Paga por hora"] = pagaporhora

  elif opcion == 3:
    while True:
      faltas = int(input("Ingrese las faltas del empleado: "))
      print(f"Se va a remplazar las faltas por: {faltas}")
      print("Quiere guardar los cambios?")
      Flag = True
      while Flag:
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta in ("si","no"):
          Flag = False
        else: print("Tenes que ingresar si o no")
      if respuesta == "si":
        break
    Empleados[NumEmpleado]["Faltas"] = faltas
    

# Obtener Sueldos

#Obtener el salario bruto de cada empleado

def SalarioBruto(valorhoraempleado: float, jornadamensual: int): # -> Sirve para obtener el salario bruto de un empleado
  return jornadamensual * valorhoraempleado

# Obtener el salario neto de cada empleado
def SueldoNeto(valorhoraempleado: float,Faltas: int,jornadamensual: int): # -> Sirve para obtener el salario neto de un empleado
  sueldobruto = SalarioBruto(valorhoraempleado,jornadamensual)
  ganancias = (sueldobruto - 400000)*0.35 if sueldobruto > 400000 else 0
  sueldoneto = sueldobruto - sueldobruto*0.10 - sueldobruto*0.06 - sueldobruto*0.02 - ganancias - (valorhoraempleado*8*Faltas)
  return sueldoneto

# Obtener la liquidación de cada empleado
def LiquidacionCompleta(empleados: List[Dict],jornadamensual: int): # -> retorna una lista de tuplas con ("Nombre","Sueldo Bruto","Sueldo Neto")
  nombres = []
  salbruts = []
  salnetos = []
  for _ in range(len(empleados)):
    nombres.append(empleados[_]["Nombre"])
    salbruts.append(SalarioBruto(empleados[_]["Paga por hora"],jornadamensual))
    salnetos.append(SueldoNeto(empleados[_]["Paga por hora"],empleados[_]["Faltas"],jornadamensual))
  liquidaciones = [_ for _ in zip(nombres, salbruts,salnetos)]
  return liquidaciones

#Obtener algunas estadisticas y valores agregados en cuanto a los sueldos

def brutototal(empleados: List[Dict],jornadamensual: int):
  return sum([x for _,x,__ in LiquidacionCompleta(empleados,jornadamensual)])

def netototal(empleados: List[Dict],jornadamensual: int):
  return sum([x for _,__,x in LiquidacionCompleta(empleados,jornadamensual)])

def netopromedio(empleados: List[Dict],jornadamensual: int):
  return sum([x for _,__,x in LiquidacionCompleta(empleados,jornadamensual)])/len(empleados)

def mejorpago(empleados: List[Dict],jornadamensual: int):
  return max(([(y,x) for y,__,x in LiquidacionCompleta(empleados,jornadamensual)]),key=lambda x: x[1])

def peorpago(empleados: List[Dict],jornadamensual: int):
  return min(([(y,x) for y,__,x in LiquidacionCompleta(empleados,jornadamensual)]),key=lambda x: x[1])

def estadisticas(empleados: List[Dict],jornadamensual: int): # -> Retorna un diccionario con las estadisticas y valores agregados
    estadisticas = {
                        "Sueldos Brutos totales a pagar": brutototal(empleados,jornadamensual),
                        "Sueldos Netos totales": netototal(empleados,jornadamensual),
                        "Sueldo Neto Promedio": netopromedio(empleados,jornadamensual),
                        "Empleado Mejor Pago": mejorpago(empleados,jornadamensual),
                        "Empleado Peor Pago": peorpago(empleados,jornadamensual)
                    }
    return estadisticas