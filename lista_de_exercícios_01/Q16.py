msg_padrao = 'Você foi convidado para festa!'
lista_convidados = ['Bruce Wayne','tony stark','Peter Parker']

print(f'{lista_convidados[2]} sera retirado da lista')

novo_convidado = input('Nome do novo convidado: ')
lista_convidados.insert(lista_convidados.index('Peter Parker'),f'{novo_convidado}')
lista_convidados.remove('Peter Parker')

while True:
    opcao = int(input("1 - Adicionar convidado querido ao inicio da lista: \n2 - Convidado no meio da lista: \n3 - Convidado no final da lista: \n0 - Finalizar: \nEscolha uma opção: "))
    if opcao == 0:
        break
    elif opcao == 1:
        nome_do_convidado = input("nome do convidado: ")
        lista_convidados.insert(lista_convidados.index('Bruce Wayne'),nome_do_convidado)
    elif opcao == 2:
        nome_do_convidado = input("nome do convidado: ")
        lista_convidados.insert(lista_convidados.index('tony stark'),nome_do_convidado) 
    elif opcao == 3:
        nome_do_convidado = input("nome do convidado: ")
        lista_convidados.append(nome_do_convidado)     
    print('\nLista de convidados:')
    for convidado in lista_convidados:
        print(convidado)