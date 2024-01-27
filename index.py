import random

mercado = ['padaria','pizzaria','hamburgueria','restaurante']
residencia = ['casa','apartamento','trailer','kitnet']

escolha = random.choice([mercado,residencia])
palavra = random.choice(escolha)
atempt = 0
valu = ['*'] * len(palavra)

while valu != list(palavra):
    letra = input('digite uma letra: ')
    if letra in palavra:
        for i, w in enumerate(palavra):
            if letra == w:
                valu[i] = letra
    else:
        print("Letter not in the word")
        atempt +=1
    if atempt == 5:
        print('você perdeu')
        break 
        
print(valu)