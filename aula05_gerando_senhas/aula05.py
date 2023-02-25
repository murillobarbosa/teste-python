import random

# GERADOR DE SENHAS !!!!!!!!!

letrasmin = 'abcdefghijklmnopqrstuvwxyz'
letrasmai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '{}[].,;#_-'

posiveis = letrasmin + letrasmai + numeros + simbolos

senha = '' .join(random.sample(posiveis, 10))

print("--------------------")

print(f'A Senha gerada foi: {senha}')


print("--------------------")

#TESTE 1

str = 'reverse me!'
print(str)
print(str[::-1])

print("--------------------")

#TESTE 2

list = [1,2,3,4,5,6,7,8]
print(max(set(list), key = list.count))

print("--------------------")

