
from gastos import registrar_gasto
from ver_gastos import ver_gastos
from total_gastos import total_gastado

continuar = True
while(continuar):
    print("===== SpendWise =====")
    print("1. Registrar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Salir")
    opcion = int(input("Ingresa el numero de la operación que deseas realizar? "))

    match opcion:
        case 1: registrar_gasto()
        case 2: ver_gastos()
        case 3: total_gastado()
        case 4: continuar = False   
        

