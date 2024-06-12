qtd_desejada = int(input("Quantidade desejada: "))
subtotal = qtd_desejada * 1.37
if qtd_desejada >= 12 :
    total = subtotal - (subtotal * 0.10)
    print(f"Total da compra R${total}")
else:
    print(f"Total da compra R${subtotal}")
