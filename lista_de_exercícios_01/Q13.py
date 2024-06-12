produto = "Teclado LoginTech MK220"
qtd_minima = int(input(f"Qtd minima para {produto}: "))
qtd_maxima = int(input(f"Qtd Maxima para {produto}: "))
qtd_estoque = int(input(f"Qtd em estoque para {produto}: "))

if qtd_estoque < qtd_maxima / 2:
    print("Atenção!, seu estoque está a baixo da média")
elif qtd_estoque > qtd_maxima / 2:
    print("Estoque a cima da média, não é necessario adquirir mais produtos!")
else:
    print("Estoque na média, em breve séra necessário adquirir novos produtos!")