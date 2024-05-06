print('Jogo de adivinhação')
N=3
Pa=0
Pb=0
La=0
Lb=0
while(La != 10 or Lb != 10):
    if Pa == 0:
        A = input('Insira o seu nome player 1: ')
    if Pb == 0:
        B = input('Insira o seu nome player 2: ')
    print('')
    Aa = int(input(f'Insira o seu palpite {A} de 1 a 10: '))
    Bb = int(input(f'Insira o seu palpite {B} de 1 a 10: '))
    while(Aa>10 or Aa<0):
        Aa = int(input(f'{Aa} não está dentro de 0 a 10, insira um novo palpite {A}: '))
    while(Bb>10 or Bb<0):
        Bb = int(input(f'{Bb} não está dentro de 0 a 10, insira um novo palpite {B}: '))
    if N>=10:
            N=N-5
    if Aa == N:
        print('')
        print(f'Você acertou {A} !')
        print('')
        Pa=Pa+10
        La=La+1
        N=N+7
        if N>=10:
            N=N-5
    elif Aa != N:
        print(f'Você errou {A} ! Tente novamente.')
        Pa=Pa-5
        print(f'O resultado era: {N}')
        N=N-1
    if N>=10:
            N=N-5
    if Bb == N:
        print(f'Você acertou {B} !')
        Pb=Pb+10
        Lb=Lb+1
        N=N+7
        if N>=10:
            N=N-5
    elif Bb != N:
        print(f'Você errou {B} ! Tente novamente.')
        Pb=Pb-5
        print(f'O resultado era: {N}')
        N=N-1
    if N>=10:
        N=N-5
    print('')
    print(f'Pontuação do {A} é {Pa} e está no nivel {La}')
    print(f'Pontuação do {B} é {Pb} e está no nivel {Lb}')
    print('')
if La > Lb:
    print(f'Você ganhou {A} !')
elif Pa > Pb:
    print(f'Você ganhou {A} !')
if La < Lb:
    print(f'Você ganhou {B} !')
elif Pa < Pb:
    print(f'Você ganhou {B} !')
if La == Lb and Pb == Pa:
    print('Empate!')