from random import randint

altura_pessoas = []
for a in range(15):
    altura_pessoas.append(f'1.{randint(45,99)}')
print(f'Grupo: {altura_pessoas}')

print(f'Altura maxima do grupo: {max(altura_pessoas)}')
print(f'Altura minima do grupo: {min(altura_pessoas)}')
