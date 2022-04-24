'''
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - enumerar elementos de lista # iteráveis
'''

string = 'O Brasil é o  país do futebol, o Brasil é penta. Brasil Brasil'
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista2)

palavra = ''
contagem = 0
for valor in lista1:
    print(f'A palavra "{valor}" apareceu {lista1.count(valor)}x na frase')
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é: {palavra} ({contagem}x)')