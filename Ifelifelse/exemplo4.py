usuario = input('Digite seu nome de usuário: ')
senha = input ('Digite sua senha: ')

usuario_bd = 'marcelo'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')
