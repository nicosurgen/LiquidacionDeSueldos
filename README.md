# Liquidacion De Sueldos

Para cada empleado de una fabrica se debe calcular su liquidación de salario.
    
Los empleados se encuentran precargados, pero se pueden agregar mas segun ingresaron antes de la liquidación mensual.
    
Para cada empleado se conoce:
*nombre
*paga por hora
*faltas.

Los empleado trabajan una jornada mensual de 160 hs.
    
    
El salario neto a liquidar es el bruto (paga por hora * jornada mensual de hora ) menos las retenciones.

Las retenciones son:
- 10% para jubilación
- 6% para obra social
- 2% sindicato
- Se descuenta 1 día de paga por cada falta (el día se calcula como una jornada de 8hs)
- Si el salario bruto es mayor a 400.000 se retiene un 35% sobre el monto excedido

Mostrar un menú hasta que el usuario lo indica con las opciones:
- 1 nuevo empleado (agrega un empleado a la plantilla de empleado)
- Sumar falta empleado (buscar el empleado por nombre y le suma una falta)
- liquidar salarios (muestra un reporte con el salario bruto y neto a pagar a cada empleado)

La funciones para calcular las retenciones se deben incluir en un módulo liquidacion.py