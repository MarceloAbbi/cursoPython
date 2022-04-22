'''
Listas em python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print( lista[::1])
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l2)
# l3 = l1 + l2
#  l1.extend(l2) # junta as duas variaveis
# l2.append('b') #insere letra b na ultima posicao
# l2.insert(0, 'batata') # insere palavra na posição desejada
# print(l2)
# l2.pop() # remove o ultimo indice
# print(l2)
# print(l1)
# print(l2)
# print(l3)

l4 = [1,2,3,4,5,6,7,8,9]
l4.insert(0, 'Batata')
print(l4)
del(l4[3:5])
print(l4)
del(l4[0])
print(l4)

print(max(l4))#
print(min(l4))

# l5 = list(range(0,100,8))
# print(l5)

l5 = [0,1,2,3,4,5,6,7,8,9]

soma = 0

for valor in l5:
    soma = soma + valor
print(soma)

l6 = ['batatinha', True, 10, -20.5]

for elem in l6:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}')

segredo = 'perfume'
digitado = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    digitado.append(letra)
    if letra in segredo:
        print(f'a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'letra "{letra}" não pertence a palavra')
        digitado.pop()

    temp = ''
    for letra_secreta in segredo:
        if letra_secreta in digitado:
            temp += letra_secreta
        else:
            temp += '*'

    if temp == segredo:
        print(f'Resposta correta! {temp}.')
        break
    else:
        print(f'A palavra secreta é: {temp}')

    if letra not in segredo:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
