# Ticket de venta
print("Generacion ticket venta")

precio_leche = float(input("Proporciona el precio de la leche: "))
precio_pan = float(input("Proporciona el precio de la pan: "))
precio_lechuga = float(input("Proporciona el precio de la lechuga: "))
precio_platanos = float(input("Proporciona el precio de la platanos: "))

# calculo del subtotal sin impuestos
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

descuento = int(input("Proporciona el descuento en porcentaje (ejemplo: 10 para 10%): "))

# aplico descuento
descuento_aplicado = subtotal * (descuento / 100)
subtotal_con_descuento = subtotal - descuento_aplicado


# calculo con impuestos
impuesto = subtotal_con_descuento * 0.16

# total de compra
costo_total = subtotal_con_descuento + impuesto
print(f"""
      Subtotal: ${subtotal_con_descuento:.2f}
      Descuento aplicado: ${descuento:.2f}%
      Descuento en dinero: ${descuento_aplicado:.2f}
      Impuesto: ${impuesto:.2f}
      Total: ${costo_total:.2f}""")