def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, "Idade:", idade, "Cidade:", cidade, sep=", ", end="\n")


imprimir_informacoes("João", 21, "Rio de Janeiro")

def calcular():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return
    else:
        print("Operação inválida!")
        return


    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")


calcular()

def lista_de_compras():
    
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    
    itens = entrada.split(", ")

   
    for i, item in enumerate(itens, start=1):
        print(f"Item {i}: {item}")


lista_de_compras()

def converter_para_fahrenheit():
    
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    
    fahrenheit = (celsius * 9/5) + 32


def digitar_nomes():
    nomes = []

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)

    print("Nomes digitados:")
    for nome in nomes:
        print(nome)


digitar_nomes()
