dato = int(input("Proporciona un dato entero: "))
esta_dentro_rango = 1 <= dato <= 10
print(f"El dato {dato} está dentro del rango: {esta_dentro_rango}")

esta_fuera_rando = not esta_dentro_rango
print(f"El dato {dato} está fuera del rango: {esta_fuera_rando}")