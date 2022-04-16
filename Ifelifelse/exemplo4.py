usuario = input('Digite seu nome de usuário: ')
senha = input ('Digite sua senha: ')

usuario_bd = 'marcelo'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')


string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi: {len(string1) + len(string2)}')