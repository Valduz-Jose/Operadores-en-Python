# Operadores Logicos
# and or not
# and regresa True si ambos operandos son true

print("***Operador And***")
condicion1 = True
condicion2 = True
resultado = condicion1 and condicion2
print(f"Resultado de {condicion1} and {condicion2} es: {resultado}")

# or regresa True si al menos uno de los operandos es true

print("***Operador Or***")
condicion1 = False
condicion2 = True
resultado = condicion1 or condicion2
print(f"Resultado de {condicion1} or {condicion2} es: {resultado}")

# not regresa el valor opuesto al operando

print("***Operador Not***")
condicion1 = False
print(f"Resultado de {condicion1} es {not condicion1}")