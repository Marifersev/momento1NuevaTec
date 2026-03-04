from gastos import gastos
def total_gastado():
    total = sum(g['monto'] for g in gastos)
    print(f"\nTotal gastado: ${total:.2f}\n")