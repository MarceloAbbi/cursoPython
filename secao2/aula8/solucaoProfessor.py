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
peso = 80.5
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
