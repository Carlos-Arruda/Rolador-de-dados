from random import randint
from time import sleep
while True:
    try:
        n1 = randint(1, 20)
        r = str(input('Deseja rolar um dado?: ')).strip().upper()[0]
        while r not in 'S':
            r = str(input('Deseja rolar um dado?: ')).strip().upper()[0]
        print()
        if r in 'S':
            if n1 == 20:
                print(f'Eita,você tirou um {n1} natural,!!!')

            elif n1 == 1:
                print(f'Poxa vida,{n1} natural é complicado hein')

            else:
                print(f'O número rolado foi {n1}')
        '''sleep(1.5)'''
        print()
        r2 = str(input('Deseja continuar? [s/n]: ')).strip().upper()[0]
        while r2 not in 'N' or 'S':
            r2 = str(input('Deseja continuar? [s/n]: ')).strip().upper()[0]
            if r2 in 'N':
                print('Espero que tenha se divertido,tenha um bom dia!!!')
                break

    except(TypeError, ValueError, KeyboardInterrupt):
        print('Opa parece que algo deu errado, tente de novo,acho que agora vai dar certo')