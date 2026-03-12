# Sistema Descuento VIP
print("Bienvenido al sistema de descuentos VIP")

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Cuantos Productos compraste hoy? "))
tiene_membresia = input("Tienes membresia VIP? (si/no) ").strip().lower() == "si"

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO and tiene_membresia)

print(f"¿El cliente es elegible para el descuento VIP? {es_elegible_descuento}")