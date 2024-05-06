print("Projeto calendario")
P=False
while(P!=True):
   A=int(input('Coloque o Ano: '))
   M=int(input('Coloque o Mês: '))
   D=int(input('Coloque o Dia: '))
   B=A/4
   if M==1:
       M=0
   elif M==2:
       M=31
   elif M==3:
       M=59
   elif M==4:
       M=90
   elif M==5:
       M=120
   elif M==6:
       M=151
   elif M==7:
       M=181
   elif M==8:
       M=212
   elif M==9:
       M=243
   elif M==10:
       M=273
   elif M==11:
       M=304
   elif M==12:
       M=334
   if B.is_integer():
        if M>=33:
           M=M+1
   if B.is_integer()==False:
        M=M+1
   if A<4:
        M=M-1
   C=A*365.25+M+D
   import math
   T=math.floor(C)
   Qui=T/7
   S=(T-1)/7
   Sa=(T-2)/7
   Do=(T-3)/7
   Se=(T-4)/7
   Te=(T-5)/7
   Qua=(T-6)/7
   if Sa.is_integer():
        print('Sábado')
   elif Do.is_integer():
        print('Domingo')
   elif Se.is_integer():
        print('Segunda')
   elif Te.is_integer():
        print('Terça')
   elif Qua.is_integer():
        print('Quarta')
   elif Qui.is_integer():
        print('Quinta')
   elif S.is_integer():
        print('Sexta')
   N=(input('Deseja acresentar outra data(S/N): '))
   if N=='N':
        P=True
   elif N=='S':
        P=False