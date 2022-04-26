nome = 'Marcelo'
idade = 24
altura = 1.80
e_maior = idade > 18
peso = 70
imc = peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.1f}')
print('{} tem {} anos e seu imc é {:.1f}'.format(nome, idade, imc))

