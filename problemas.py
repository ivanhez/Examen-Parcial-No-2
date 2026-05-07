# def hacer_sencillo(monto):
#     monedas = [25, 10, 5, 1]
#     resultado = {}
#     for moneda in monedas:
#         cantidad = monto // moneda
#         resultado[moneda] = cantidad
#         monto =  monto % moneda
#     return resultado, sum(resultado.values())

# print("Hacer sencillo\n")
# for monto in [502, 99, 42]:
#     print(monto, hacer_sencillo(monto))


def knapsack_fraccionado(W, items):
    """
    items: lista de tuplas (nombre, precio_total, unidades_disponibles)
    """
    ordenados = sorted(items, key=lambda x: x[1] / x[2], reverse=True)
    restante = W
    total = 0
    solucion = []

    for nombre, precio, unidades in ordenados:
        if restante == 0:
            break

        densidad = precio / unidades
        tomar = min(unidades, restante)
        valor = tomar * densidad

        solucion.append((nombre, tomar, valor, densidad))
        total += valor
        restante -= tomar

    return total, solucion


print("KNAPSACK FRACCIONADO\n")
casos_knapsack = [
    (50, [("item1", 60, 10), ("item2", 100, 20), ("item3", 120, 30)]),
    (15, [("item1", 100, 10), ("item2", 60, 10), ("item3", 120, 30)]),
    (60, [("item1", 100, 20), ("item2", 60, 10), ("item3", 120, 30), ("item4", 75, 15)]),
]

for W, items in casos_knapsack:
    print(W, knapsack_fraccionado(W, items))