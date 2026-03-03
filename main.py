
from gastos import registrar_gasto


continuar = True
while(continuar):
    print("===== SpendWise =====")
    print("1. Registrar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Salir")
    opcion = int(input("Ingresa el numero de la operación que deseas realizar?"))

    match opcion:
        case 1: resultado = registrar_gasto()
        case 2: resultado = ver_gastos()
        case 3: resultado = total_gastado()
        case 4: continuar = False   
        
    if(opcion != 4):
        print(f" {resultado}")
