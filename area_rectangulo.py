# Calcular el area y perimetro de un rectangulo
base = float(input("Proporciona la base del rectangulo: "))
altura = float(input("Proporciona la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")