"""
Formatando valores com modificadores - aula 11
:s - Texto (Strings)
:d - Inteiros (int)
:f - Float
:. (NÚMERO) f - quantidade de casas decimais (float)
:(CARACTERE) <> ou ^)(Quantidade) (TIPO -s, d ou f)

> - Esquerda
< - Direita
^- Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0>10.2f}')

nome = 'Marcelo Abbi'
print((50-len(nome)) / 2)

print(f'{nome:#^50}')

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)
