print("### Medido de IMC - Índice de Massa Corporal ###")
peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('peso normal')
elif imc >= 25 and imc <= 30:
    print('acima do peso')
else:
    print('obeso')
