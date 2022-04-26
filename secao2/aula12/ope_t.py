'''
Operador ternário em Python
'''

# idade = input('Qual a sua idade? ')
# e_de_maior = (idade >= 18)
# msg = 'Pode acessar' if e_de_maior else 'Não pode menor ok.'

# msg1 = idade if idade >= 18 else 'Usuario menor de idade'
# logged_user = True
# msg = 'Usuário Logado.' if logged_user else 'Usuário precisa Logar'

# if logged_user:
#     msg = 'Usuário Logado.'
# else:
#     msg = 'Usuário precisa Logar.'

# print(msg)

# if idade >=18:
#     print('Pode Acessar.')
# else:
#     print('Não pode de menor ok.')

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode menor ok.'
    print(msg)
