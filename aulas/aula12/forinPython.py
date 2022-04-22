'''
For in em Python
Iterando strings com for
Função range (start=0, sop, step=1)
'''

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

 c = 0
while c < len(texto):
    print(texto[c])
    c += 1


for n, letra in enumerate(texto):
    print(n, letra)

print('#############')

for numero in range(20, 10, -2):
    print(numero)

print('#############')

for n in range(100):
    if n % 8 == 0:
        print(n)
