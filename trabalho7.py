def calcular_soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

numeros = [1, 2, 3, 4]
soma, media = calcular_soma_media(numeros)
print("Soma:", soma)
print("Média:", media)

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]


lista_palavras = ["Botafogo", "Fogo", "Tiquinho", "Incendeia"]
palavra_antiga = "Fogo"
palavra_nova = "Lobo"
lista_alterada = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
print(lista_alterada)

def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print("*" * i)

num_linhas = 10
imprimir_triangulo(num_linhas)
