print('Imposto de renda')
S=float(input('Informe seu salário: R$'))
if S<=2259.2:
    print('Isento')
elif S<=2826.65:
    R=S*7.5/100
    print('Imposto de: R$',R)
elif S<=3751.05:
    R=S*15/100
    print('Imposto de: R$',R)
elif S<=4664.68:
    R=S*22.5/100
    print('Imposto de: R$',R)
elif S>4664.68:
    R=S*27.5/100
    print('Imposto de: R$',R)