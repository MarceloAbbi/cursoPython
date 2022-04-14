"""
Iniciar com letra, pode conter números, separar por _, letras minúsculas
"""

nome = 'Marcelo Abbi'
idade = 24
altura = 1.80
e_maior = idade > 18
peso = 70
imc = peso / (altura * altura)

#  imc = peso / (altura ** 2) //resolucao do professor
#  print('Nome:', nome)
#  print('Idade:', idade)
#  print('Altura:', altura)
#  print('Maior de Idade?', e_maior)
#  print('imc: ', imc)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

if (imc <= 18.5):
    print('Abaixo do peso')
elif (imc >=18.6 ) and (imc <= 24.9):
    print('Peso Normal')
elif (imc >= 25) and (imc <= 29.9):
    print('Sobrepeso')
elif (imc >= 30) and (imc <= 34.9):
    print('Obesidade I')
elif (imc >= 35) and (imc <= 39.9):
    print('Obesidade II')
elif (imc >= 40):
    print('Obesidade Mórbida')
