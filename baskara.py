S='S'
while(S=='S'):
    sim_ou_nao=["S", "N"]
    a=int(input("Insira a variavel 'A': "))
    while(a==0):
        print("0 não é valido")
        a=int(input("Insira a variavel 'A': "))
    if a > 0:
        sinal_a='+'
    elif a < 0:
        sinal_a=''
    b=int(input("Insira a variavel 'B': "))
    if b == 0:
        b=''
        sinal_b=''
        x=''
    elif b > 0:
        sinal_b='+'
        x='x'
    elif b < 0:
        sinal_b=''
        x='x'
    c=int(input("Insira a variavel 'C': "))
    if c == 0:
        c=''
        sinal_c=''
    elif c > 0:
        sinal_c='+'
    elif c < 0:
        sinal_c=''
    print(f"Expressão: {a}x²{sinal_b}{b}{x}{sinal_c}{c}=0")
    continuar=input("Deseja mudar alguma variavel?(S/N)\nR: ")
    continuar=continuar.upper()
    while continuar not in sim_ou_nao:
        print(f"Sua resposta deve ser S ou N, não {continuar}")
        continuar=input("Deseja mudar alguma variavel?(S/N)\nR: ")
        continuar=continuar.upper()
    print('')
    while continuar == "S":
        if continuar=="S":
            a_=input(f"Deseja mudar A={a}?(S/N)\nR: ")
            a_=a_.upper()
            while a_ not in sim_ou_nao:
                print(f"Sua resposta deve ser S ou N, não {a_}")
                a_=input(f"Deseja mudar A={a}?(S/N)\nR: ")
                a_=a_.upper()
            if a_ == "S":
                a=int(input("Insira a nova variavel 'A': "))
                while(a==0):
                    print("0 não é valido")
                    a=int(input("Insira a nova variavel 'A': "))
            if b == '':
                b=0
            b_=input(f"Deseja mudar B={b}?(S/N)\nR: ")
            b_=b_.upper()
            while b_ not in sim_ou_nao:
                print(f"Sua resposta deve ser S ou N, não {b_}")
                b_=input(f"Deseja mudar B={b}?(S/N)\nR: ")
                b_=b_.upper()
            if b_ == "S":
                b=int(input("Insira a nova variavel 'B': "))
                if b == 0:
                    b=''
                    sinal_b=''
                    x=''
                elif b > 0:
                    sinal_b='+'
                    x='x'
                elif b < 0:
                    sinal_b=''
                    x='x'
            if b == 0:
                b=''
            if c == '':
                c=0
            c_=input(f"Deseja mudar C={c}?(S/N)\nR: ")
            c_=c_.upper()
            while c_ not in sim_ou_nao:
                print(f"Sua resposta deve ser S ou N, não {c_}")
                c_=input(f"Deseja mudar C={c}?(S/N)\nR: ")
                c_=c_.upper()
            if c_ == "S":
                c=int(input("Insira a nova variavel 'C': "))
                if c == 0:
                    c=''
                    sinal_c=''
                elif c > 0:
                    sinal_c='+'
                elif c < 0:
                    sinal_c=''
            if c == 0:
                c=''
            print(f"Expressão: {a}x²{sinal_b}{b}{x}{sinal_c}{c}=0")
            continuar=input("Deseja mudar alguma variavel?(S/N)\nR: ")
            continuar=continuar.upper()
            while continuar not in sim_ou_nao:
                print(f"Sua resposta deve ser S ou N, não {continuar}")
                continuar=input("Deseja mudar alguma variavel?(S/N)\nR: ")
                continuar=continuar.upper()
    if b == '':
        b=0
    if c == '':
        c=0
    delta_=(b*b)-4*a*c
    sinal_necessario=''
    imaginario=''
    if delta_ < 0:
        delta_=delta_/-1
        imaginario="*i"
        sinal_necessario='-'
    import math
    delta_2=math.sqrt(delta_)
    x_1=(-b+delta_2)/(2*a)
    x_2=(-b-delta_2)/(2*a)
    print(f"∆={b}²-4*{a}*{c}")
    b_2=b*b
    print(f"∆={b_2}-4*{a}*{c}")
    a_c=-4*a*c
    sinal_ac=''
    if a_c>0:
        sinal_ac='+'
    b=-b
    a_2=2*a
    if delta_2>=0:
        sinal_x1='+'
        sinal_x2='-'
    if delta_<0:
        sinal_x1='-'
        sinal_x2='+'
    print(f"∆={b_2}{sinal_ac}{a_c}")
    print(f"∆={sinal_necessario}{delta_}\n")
    print(f"x={b}±√{delta_}")
    print(f"  ———————————")
    print(f"     2*{a}\n")
    print(f"x={b}±{delta_2}{imaginario}")
    print(f"  ———————————")
    print(f"     {a_2}\n\n")
    print(f"x1={b}{sinal_x1}{delta_2}{imaginario}")
    print(f"   ———————————")
    print(f"     {a_2}\n")
    print(f"x1={b + delta_2}{imaginario}")
    print(f"   ———————————")
    print(f"     {a_2}\n")
    print(f"x1={x_1}{imaginario}\n\n")
    print(f"x2={b}{sinal_x2}{delta_2}{imaginario}")
    print(f"   ———————————")
    print(f"     {a_2}\n")
    print(f"x2={b - delta_2}{imaginario}")
    print(f"   ———————————")
    print(f"     {a_2}\n")
    print(f"x2={x_2}{imaginario}\n\n")
    S=input("Deseja colocar novas variaveis?(S/N)\nR: ")
    S=S.upper()
    while S not in sim_ou_nao:
        print(f"Sua resposta deve ser S ou N, não {c_}")
        S=input("Deseja colocar novas variaveis?(S/N)\nR: ")
        S=S.upper()
    print('')