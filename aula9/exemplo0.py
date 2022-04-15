nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2022 - int(idade)

print(f'O usuário digitou {nome} e o tipo da variável é 'f'{type(nome)}')
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu no ano de {ano_nascimento}')

