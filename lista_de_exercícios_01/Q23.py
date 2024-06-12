from os import system
lista = []

def Numeros_negativos(lista_numeros):
    qtd_num_negativos = 0
    for numero_n in lista_numeros:
        if numero_n < 0:
            qtd_num_negativos +=1
    return qtd_num_negativos

def Numeros_positivos(lista_numeros):
    qtd_num_positivos = 0
    for numero_p in lista_numeros:
        if numero_p > 0:
            qtd_num_positivos +=1
    return qtd_num_positivos

def Percentual_nums(numeros_negativos,numeros_positivos):
    perc_negativo = (numeros_negativos * 100) / (numeros_negativos+numeros_positivos)
    perc_positivo = (numeros_positivos * 100) / (numeros_negativos+numeros_positivos)
    resposta = f'{perc_negativo}% dos números são negativos.\n{perc_positivo}% dos números são positivos. \n'
    return resposta
    

while True:
    print(f'Foram digitados {len(lista)} números\n')
    num = input('Digite um numero, (negativo) ou (positivo)\nCaso queira ENCERRAR digite a letra (e):')
    if num == 'e' or num == 'E':
        media = sum(lista) / len(lista)
        print(f'Quantidade de Números negativos: {Numeros_negativos(lista)}')
        print(f'Quantidade de Números positivos: {Numeros_positivos(lista)}')
        print(Percentual_nums(Numeros_negativos(lista),Numeros_positivos(lista)))
        print(f'Média Aritimética: {media}')
        break    
    lista.append(int(num))

        