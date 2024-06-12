valor_n1 = float(input("Valor 1:"))
operacao = str(input("(+) - Adição:\n(-) - Subtração:\n(*) - Multiplicação:\n(/) - Divisão:\n(**) - Potenciação:"))
valor_n2 = float(input("Valor 2: "))

match operacao:
    case "+":
        calculo = valor_n1 + valor_n2
        print(f"Resultado: {calculo}")
    case "-":
        calculo = valor_n1 - valor_n2
        print(f"Resultado: {calculo}") 
    case "*":
        calculo = valor_n1 * valor_n2
        print(f"Resultado: {calculo}") 
    case "/":
        calculo = valor_n1 / valor_n2
        print(f"Resultado: {calculo}")       
    case "**":
        calculo = valor_n1 + valor_n2
        print(f"Resultado: {calculo}")                       