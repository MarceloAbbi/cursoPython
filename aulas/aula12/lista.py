string = 'O Brasil é penta.'
lista = string.split(' ')
# string2 = ' '.join(lista)
#
# print(string)
# print(lista)
# print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista2 = [
    [0, 'Marcelo'],
    [1,'João'],
    [2,'Maria'],
]

for indice, nome in lista2:
    print(indice, nome)

lista3 = ['Marcelo', 'João', 'Maria']

n1, n2, n3 = lista3

print(n2)
