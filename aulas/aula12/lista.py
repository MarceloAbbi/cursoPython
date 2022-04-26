string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

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

lista4 = [
    # 0       1        2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Luzitânia'],  # 2
]

print(lista4[2][2])

enumerada = list(enumerate(lista4))
print(enumerada[0][1][2])

# O segundo valor sempre tem que ser 1

for v1 in enumerate(lista4, 51):
    valor_enumerado, minha_lista = v1
    print(minha_lista)
