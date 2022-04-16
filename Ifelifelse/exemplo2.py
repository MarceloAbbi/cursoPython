'''
Operadores Relacionais
== > >= < <= !=
'''

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#  Limite para pegar o empréstimo
idade_minima = 20 #  muito jovem
idade_maxima = 30 #  passou da idade

if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

