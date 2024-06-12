inicio = 1000
fim    = 2000
contador = inicio
while contador < fim:
    if contador%11 == 5:
        print(f'{contador} dividido por 11 o resto é 5')
    contador+=1