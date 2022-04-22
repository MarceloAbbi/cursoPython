segredo = 'perfume'
digitado = []
chances = 3

print('****JOGO DA FORCA****\n Voce tem 3 chances de errar. \n Apenas letras minusculas\n')

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    digitado.append(letra)
    if letra in segredo:
        print(f'a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'letra "{letra}" não pertence a palavra')
        digitado.pop()

    temp = ''
    for letra_secreta in segredo:
        if letra_secreta in digitado:
            temp += letra_secreta
        else:
            temp += '*'

    if temp == segredo:
        print(f'Resposta correta! {temp}.')
        break
    else:
        print(f'A PALAVRA SECRETA É: {temp}')

    if letra not in segredo:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
