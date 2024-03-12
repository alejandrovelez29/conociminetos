"""""1.	Calcular y mostrar el índice masa corporal de una persona."""

def calcular_imc(peso, altura):
    # Calcular el IMC
    imc = peso / (altura ** 2)
    return imc

def evaluar_imc(imc):
    # Evaluar el IMC y proporcionar un mensaje personalizado
    if imc < 18.5:
        return "Bajo peso, ¡come un poco más!"
    elif 18.5 <= imc < 25:
        return "Peso saludable, ¡bien hecho!"
    elif 25 <= imc < 30:
        return "Sobrepeso, ¡cuidado con la dieta!"
    else:
        return "Obesidad, ¡consulta a un profesional de la salud!"

# Solicitar al usuario que ingrese su peso en kilogramos
peso = float(input("Ingresa tu peso en kilogramos: "))

# Solicitar al usuario que ingrese su altura en metros
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC llamando a la función
imc_resultado = calcular_imc(peso, altura)

# Evaluar el IMC y mostrar un mensaje personalizado
mensaje = evaluar_imc(imc_resultado)

# Mostrar el resultado
print("Tu Índice de Masa Corporal (IMC) es:", imc_resultado)
print("Mensaje:", mensaje)