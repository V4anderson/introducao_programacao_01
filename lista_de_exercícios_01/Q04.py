valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto, apenas o valor sem o sinal de %: "))
resultado = valor_produto - (valor_produto * (percentual_desconto / 100))
print(f"O Valor do produto com desconto é: {resultado}")