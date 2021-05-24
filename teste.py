from random import randint

while True:
    d100 = randint(1,100)
    d20 = randint(1,20)
    d12 = randint(1,12)
    d10 = randint(1,10)
    d8 = randint(1,8)
    d6 = randint(1,6)
    d4 = randint(1,4)

    dado = str(input('Qual dado deseja rolar?(d100,d20,d12,d10,d8,d6,d4 ou 999 pra parar): ')).strip().upper()
    if dado == 'D100':
        print(f'vc rolou {d100}')
    elif dado == 'D20':
        print(f'vc rolou {d20}')
    elif dado == 'D12':
        print(f'vc rolou {d12}')
    elif dado == 'D10':
        print(f'vc rolou {d10}')
    elif dado == 'D8':
        print(f'vc rolou {d8}')
    elif dado == 'D6':
        print(f'vc rolou {d6}')
    elif dado == 'D4':
        print(f'vc rolou {d4}')
    elif dado == '999':
        print('Espero que tenha se divertido,tenha um bom dia!!!')
        break
    else:
        print('Algo deu errado,tente novamente!')

   
        

    