"""
Manipulando Strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

#  positivos
#       [012345678]
texto = 'Python_s2'
#      -[987654321]
#  negativos

url = 'www.google.com.br/'

print(url[:-1])
#  remove a barra do link

nova_string = texto[0::2]
print(nova_string)

print(len(texto))

for letra in texto:
    print(letra)
