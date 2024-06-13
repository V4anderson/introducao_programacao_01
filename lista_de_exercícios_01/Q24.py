lista = []
intervalos = []
contador = 0

for a in range(0,100+1):
    intervalos.append(a)


while True:
    num = int(input("Digite um número: "))
    if num < 0:
        print(f'{contador} dos números lidos, estão dentro dos intervalos [0-25], [26-50], [51-75], [76-100]')
        break
    else:
        lista.append(num)    
        if num in intervalos:
            contador+=1

