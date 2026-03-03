
gastos = []
def registrar_gasto():
    print("\n--- Registrar Gasto ---")
    fecha = input("Fecha (dd/mm/aaaa): ")
    categoria = input("Categoría (café, snacks, transporte, otros): ")
    descripcion = input("Descripción: ")
    try:
        monto = float(input("Monto: $"))
    except ValueError:
        print("Monto inválido.")
        return
    gasto = {
        "fecha": fecha,
        "categoria": categoria,
        "descripcion": descripcion,
        "monto": monto
    }
    gastos.append(gasto)
    print("Gasto registrado correctamente.\n")