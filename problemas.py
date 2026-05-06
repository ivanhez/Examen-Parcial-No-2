def hacer_sencillo(monto):
    monedas = [25, 10, 5, 1]
    resultado = {}
    for moneda in monedas:
        cantidad = monto // moneda
        resultado[moneda] = cantidad
        monto =  monto % moneda
    return resultado, sum(resultado.values())


# Resultados
print("Hacer sencillo")
for monto in [502, 99, 42]:
    print(monto, hacer_sencillo(monto))
