'''
Exercício utilizando os dados do professor de exemplo

* Criar variáveis para nome (str), idade(int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura)
* Exibir um texto com todos os valores na tela usando F-strings
'''

nome = 'Luiz'
idade = 35
altura = 1.80
peso = 80
ano_atual = 2022
imc = peso / (altura * altura)
data_nascimento = ano_atual - idade

print('{} tem {} anos, {} de altura e pesa {}kg.'.format(nome,idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, data_nascimento))
