glossario = {
    'variavel' : 'Um dado é classificado como variável quando tem a possibilidade de ser alterado em algum instante no decorrer do tempo, ou seja, durante a execução do algoritmo em que é utilizado',
    'open-source' : '(Código Aberto): software cujo código-fonte está disponível publicamente e pode ser\n modificado e distribuído por qualquer pessoa.',
    'api' :'(Interface de Programação de Aplicativos): um conjunto de regras e protocolos que permite que\n diferentes softwares se comuniquem entre si.\n É usado para acessar recursos e funcionalidades de outros programas.',
    'algoritimo' : 'Um algoritmo pode ser definido como uma sequência de passos\n que visam a atingir um objetivo bem definido',
    'compilacao': 'É o processo de tradução de código-fonte em linguagem de máquina ou bytecode\n, que pode ser executado por um computador.'
}
for line in glossario:
    print(line+': '+glossario[line]+'\n')
