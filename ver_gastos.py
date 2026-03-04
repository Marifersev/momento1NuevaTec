from gastos import gastos
def ver_gastos():
    if not gastos:
        print("No hay gastos registrados.\n")
        return
    print("\n--- Lista de Gastos ---")
    i = 1 
    for g in gastos:
        print(f"{i}. {g['fecha']} | {g['categoria']} | ${g['monto']} | {g['descripcion']}")
        i += 1
    print()