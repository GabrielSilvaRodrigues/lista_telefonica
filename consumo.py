print('Projeto consumo de combustivel em cidade')
Z=True
while(Z!=False):
    QP= float(input('Quilômetros percorridos: '))
    C= float(input('Combustível (diesel) consumido: '))
    TC = QP / C
    print(f'Consumo: {TC:.2f} Km/L')
    if TC<=8.8:
       print('Classificação quanto ao consumo energético: E')
    elif TC<=11.5:
       print('Classificação quanto ao consumo energético: D')
    elif TC<=13.7:
       print('Classificação quanto ao consumo energético: C')
    elif TC<=19:
       print('Classificação quanto ao consumo energético: B')
    elif TC>19:
       print('Classificação quanto ao consumo energético: A')
    N=(input('Deseja acresentar outro veiculo(S/N): '))
    if N.upper()=='S':
       Z=True
    elif N.upper()=='N':
       Z=False

