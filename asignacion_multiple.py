# Asignacion multiple

x,y,z = 10,'Hola',-9.15
print(f"El valor de x es: {x} y el valor de y es: {y} y el valor de z es: {z}")

# Asignacion encadenada 
# se usa el mismo valor para varias variables
a = b = c = 20
print(f"El valor de a es: {a} y el valor de b es: {b} y el valor de c es: {c}")

# Intercambio de valores de una variable sin utilizar una variable temporal
x,y = 5,10
# Aplicando el concepto de asignacion multiple
x,y = y,x
print(f"El valor de x es: {x} y el valor de y es: {y}")

# recibir multiples valores de entrada del usuario
nombre,apellido = input("Ingrese su nombre y apellido separados por una coma: ").split(',')
print(f"El nombre es: {nombre.strip()} y el apellido es: {apellido.strip()}")