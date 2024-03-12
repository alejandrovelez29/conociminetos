def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

# Ejemplo de uso
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"El Índice de Masa Corporal (IMC) es: {imc:.2f}")

# f-string
mensaje = (f"Tabla de clasificaciones: \n Desnutricion moderada: 16,01-16,99 .\n Bajo peso: 18,5-22 ."
           f"\n Peso normal: 22,1-24,9 .\n Sobrepeso: 25-29,9")
print(mensaje)