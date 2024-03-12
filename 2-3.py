RM = 1250
Min = 120

Num1 = RM*Min
print(f"El valor neto de la llamada es: {Num1}")

porcentaje_aumento = Min
valor_original = RM
descuento = valor_original * (porcentaje_aumento / 20)
valor_con_descuento = valor_original - descuento
print(f"El valor del descuento es: {valor_con_descuento}")

porcentaje_aumento = 20
valor_original = Num1
descuento = valor_original * (porcentaje_aumento / 100)
valor_con_descuento = valor_original - descuento
print(f"El valor con descuento es: {valor_con_descuento}")