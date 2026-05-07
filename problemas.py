def hacer_sencillo(monto):
    monedas = [25, 10, 5, 1]
    resultado = {}
    for moneda in monedas:
        cantidad = monto // moneda
        resultado[moneda] = cantidad
        monto =  monto % moneda
    return resultado, sum(resultado.values())

print("\nHacer sencillo")
for monto in [293, 502, 99, 42, 1337]:
    print(monto, hacer_sencillo(monto))


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


print("\nKNAPSACK FRACCIONADO")
casos_knapsack = [
    (50, [("item1", 60, 10), ("item2", 100, 20), ("item3", 120, 30)]),
    (15, [("item1", 100, 10), ("item2", 60, 10), ("item3", 120, 30)]),
    (60, [("item1", 100, 20), ("item2", 60, 10), ("item3", 120, 30), ("item4", 75, 15)]),
    (37, [("item1", 64, 52), ("item2", 56, 11), ("item3", 92, 26), ("item4", 111, 43)]),
]

for W, items in casos_knapsack:
    print(W, knapsack_fraccionado(W, items))


VECINOS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [2, 1, 3, 5],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 5, 7, 9, 0],
    9: [9, 6, 8],
}


def contar_teclado(n):
    if n <= 0:
        return 0, []

    combinaciones = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for _ in range(2, n + 1):
        nuevas_combinaciones = []

        for numero in combinaciones:
            ultimo_digito = int(numero[-1])

            for siguiente in VECINOS[ultimo_digito]:
                nuevas_combinaciones.append(numero + str(siguiente))

        combinaciones = nuevas_combinaciones

    return len(combinaciones), combinaciones


print("\nTeclado Nokia")

for n in [2, 3, 4, 5]:
    total, lista = contar_teclado(n)

    print(f"\nn = {n}")
    print(f"Total de combinaciones: {total}")
    print("Lista de combinaciones:")
    print(lista)