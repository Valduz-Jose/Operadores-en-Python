# Solicitar un valor entre 0 y 5
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor = int(input(f"Proporciona un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}:  "))

# es_dentro_rango = valor >= VALOR_MINIMO and valor <= VALOR_MAXIMO

esta_dentro_rango = VALOR_MINIMO <= valor <= VALOR_MAXIMO

print(f"El valor {valor} está dentro del rango: {esta_dentro_rango}")