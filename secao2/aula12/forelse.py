'''
For / Else em Python
'''

variavel = ['Marcelo Abbi', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

comeca_com_m = False
for valor in variavel:
    if valor.lower().startswith('m'):
        comeca_com_j = True

if comeca_com_m:
    print('Existe uma palavra que começa com m.')
else:
    print('Não existe uma palavra que começa com m.')

