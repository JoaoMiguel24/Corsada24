def gravar_nome_em_arquivo():
    
    nome = input("Digite seu nome: ")

    
    with open("nomes.txt", "w") as arquivo:
        
        arquivo.write(nome)

    print("Nome gravado no arquivo 'nomes.txt'.")


gravar_nome_em_arquivo()

def imprimir_conteudo_arquivo():
    
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    
    with open(nome_arquivo, "r") as arquivo:
        
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)


imprimir_conteudo_arquivo()

def copiar_arquivo():
    
    arquivo_origem = "exemplo.txt"
    
    novo_arquivo = "copia_exemplo.txt"

    
    with open(arquivo_origem, "r") as arquivo_origem:
        
        conteudo = arquivo_origem.read()

        
        with open(novo_arquivo, "w") as arquivo_destino:
            arquivo_destino.write(conteudo)

    print(f"O conteúdo do arquivo '{arquivo_origem}' foi copiado para o arquivo '{novo_arquivo}'.")


copiar_arquivo()

def encontrar_nome_por_numero(numero):
    
    arquivo_exemplo = "exemplo.txt"

    
    with open(arquivo_exemplo, "r") as arquivo:
       
        linhas = arquivo.readlines()

        
        if 0 <= numero < len(linhas):
           
            nome_correspondente = linhas[numero].strip()
            print(f"O nome correspondente ao número {numero} é: {nome_correspondente}")
        else:
            print("Número fora do intervalo válido.")


numero = int(input("Digite um número para encontrar o nome correspondente: "))
encontrar_nome_por_numero(numero)
