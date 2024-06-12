contador = 0
for a in range(501):
    print("Pula a primeira linha!")
    if a > 0:
        #verifica se é multiplo de 3
        if a%3 == 0:
            #verifica se é ímpar, caso seja, adiciona na lista
            if a%2 != 0:                    
                contador +=a
print(f"A Soma do total de numeros que são impares e multiplo de 3 no intervalo de 1 a 500 é: {contador}")
        