import random
num = int(input('escolha um numero de 1 a 9'))
rand = random.choice([1,9])
sum = num + rand
escolha = input('Par ou Impar?').lower
if(sum % 2 == 0 and escolha == 'par'):
    print('Você ganhou')  
elif(sum % 2 != 0 and escolha == 'impar'):
    print('Você ganhou:'.sum)   
else:
    print('Você perdeu')
    
