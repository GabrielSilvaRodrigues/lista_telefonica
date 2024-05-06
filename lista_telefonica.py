R = 's'
nome=[""]
telefone=[""]
email=[""]
i=1
menu=input('\n**********MENU***********\n\n 0 - SAIR\n 1 - INSERIR NOVO CONTATO\n 2 - PESQUISAR CONTATOS\n 3 - VER CONTATOS\n 4 - EDITAR CONTATO\n R: ')
while(menu!='0'):
    if menu == '1':
        while(R=='s'):
            nome_=input('Nome: ')
            nome.append(f"{nome_}")
            telefone_=input('Telefone: ')
            telefone.append(f"{telefone_}")
            email_=input('E-mail: ')
            email.append(f"{email_}")
            R=input('Outro contato s/n: ')
            i=i+1
    elif menu == '2':
        R ='s'
        while(R=='s'):
            n=int(input('Qual possição do contato você deseja ver (0 = não sei): '))
            if n==0:
                n=input('Informe o nome do contato você deseja ver (n = não sei): ')
                if n=='n':
                    n=input('Informe o telefone do contato você deseja ver (n = não sei): ')
                    if n=='n':
                        n=input('Informe o email do contato você deseja ver (n = não sei): ')
                        if n=='n':
                            print('Ai você me comprica!')
                        else:
                            for i in range (len(email)):
                                if email[i] == n:
                                    print(f"Nome: {nome[i]}")
                                    print(f"Telefone: {telefone[i]}")
                                    print(f"E-mail: {email[i]}")
                                    flag = True    
                    else:
                        for i in range (len(telefone)):
                            if telefone[i] == n:
                                print(f"Nome: {nome[i]}")
                                print(f"Telefone: {telefone[i]}")
                                print(f"E-mail: {email[i]}")
                                flag = True
                else:
                    for i in range (len(nome)):
                        if nome[i] == n:
                            print(f"Nome: {nome[i]}")
                            print(f"Telefone: {telefone[i]}")
                            print(f"E-mail: {email[i]}")
                            flag = True
            else:
                print(f"Nome: {nome[n]}")
                print(f"Telefone: {telefone[n]}")
                print(f"E-mail: {email[n]}")
            R=input('Deseja encontrar outro contato s/n: ')
    elif menu == '3':
        for k in range(len(nome)):
            print("")
            print(f"Possição: {k}")
            print("")
            print(f"Nome: {nome[k]}")
            print(f"Telefone: {telefone[k]}")
            print(f"E-mail: {email[k]}")
    elif menu == '4':
        n=input('Qual o contato que você deseja editar?\n R: ')
        if n in nome:
            for i in range (len(nome)):
                if nome[i] == n:
                    nome_editar=input(f"Editar o nome: {nome[i]} (s/n)")
                    if nome_editar == 's':
                        nome.remove(f"{nome[i]}")
                        nome_=input('Novo nome: ')
                        nome.insert(i,f"{nome_}")
                    else:
                        print(f"Nome: {nome[i]}")
                    telefone_editar=input(f"Editar o telefone: {telefone[i]} (s/n)")
                    if telefone_editar == 's':
                        telefone.remove(f"{telefone[i]}")
                        telefone_=input('Novo telefone: ')
                        telefone.insert(i,f"{telefone_}")
                    else:
                        print(f"Telefone: {telefone[i]}")
                    email_editar=input(f"Editar o e-mail: {email[i]} (s/n)")
                    if email_editar == 's':
                        email.remove(f"{email[i]}")
                        email_=input('Novo email: ')
                        email.insert(i,f"{email_}")
                    else:
                        print(f"E-mail: {email[i]}")
                    flag = True
        elif n in telefone:
            for i in range (len(telefone)):
                if telefone[i] == n:
                    nome_editar=input(f"Editar o nome: {nome[i]} (s/n)")
                    if nome_editar == 's':
                        nome.remove(f"{nome[i]}")
                        nome_=input('Novo nome: ')
                        nome.insert(i,f"{nome_}")
                    else:
                        print(f"Nome: {nome[i]}")
                    telefone_editar=input(f"Editar o telefone: {telefone[i]} (s/n)")
                    if telefone_editar == 's':
                        telefone.remove(f"{telefone[i]}")
                        telefone_=input('Novo telefone: ')
                        telefone.insert(i,f"{telefone_}")
                    else:
                        print(f"Telefone: {telefone[i]}")
                    email_editar=input(f"Editar o e-mail: {email[i]} (s/n)")
                    if email_editar == 's':
                        email.remove(f"{email[i]}")
                        email_=input('Novo email: ')
                        email.insert(i,f"{email_}")
                    else:
                        print(f"E-mail: {email[i]}")
                    flag = True
        elif n in email:
            for i in range (len(email)):
                if email[i] == n:
                    nome_editar=input(f"Editar o nome: {nome[i]} (s/n)")
                    if nome_editar == 's':
                        nome.remove(f"{nome[i]}")
                        nome_=input('Novo nome: ')
                        nome.insert(i,f"{nome_}")
                    else:
                        print(f"Nome: {nome[i]}")
                    telefone_editar=input(f"Editar o telefone: {telefone[i]} (s/n)")
                    if telefone_editar == 's':
                        telefone.remove(f"{telefone[i]}")
                        telefone_=input('Novo telefone: ')
                        telefone.insert(i,f"{telefone_}")
                    else:
                        print(f"Telefone: {telefone[i]}")
                    email_editar=input(f"Editar o e-mail: {email[i]} (s/n)")
                    if email_editar == 's':
                        email.remove(f"{email[i]}")
                        email_=input('Novo email: ')
                        email.insert(i,f"{email_}")
                    else:
                        print(f"E-mail: {email[i]}")
                    flag = True
        else:
            print('Não encontrado ou inesistente')
    menu=input('\n**********MENU***********\n\n 0 - SAIR\n 1 - INSERIR NOVO CONTATO\n 2 - PESQUISAR CONTATOS\n 3 - VER CONTATOS\n 4 - EDITAR CONTATO\n R: ')