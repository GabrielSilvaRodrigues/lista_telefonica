p=True
c=0
print('Cachorro Quente = 1')
print('Bauru Simples = 2')
print('Bauru c/Ovo = 3')
print('Hamburger = 4')
print('Cheeseburger = 5')
print('Refrigerante = 6')
while(p!=False):
    a = int(input('Coloque o número do pedido: '))
    if a == 1:
      ca = 'Cachorro Quente'
      print(f"{ca}")
      qa=int(input(f'Quantidade de {ca}: '))
      c=c+(8.10*qa)
    elif a == 2:
      cb = 'Bauru Simples'
      print(f"{cb}")
      qb=int(input(f'Quantidade de {cb}: '))
      c=c+(11.30*qb)
    elif a == 3:
      cc = 'Bauru c/Ovo'
      print(f"{cc}")
      qc=int(input(f'Quantidade de {cc}: '))
      c=c+(15.50*qc)
    elif a == 4:
      cd = 'Hamburger'
      print(f"{cd}")
      qd=int(input(f'Quantidade de {cd}: '))
      c=c+(13.10*qd)
    elif a == 5:
      ce = 'Cheeseburger'
      print(f"{ce}")
      qe=int(input(f'Quantidade de {ce}: '))
      c=c+(14.30*qe)
    elif a == 6:
      cf = 'Refrigerante'
      print(f"{cf}")
      qf=int(input(f'Quantidade de {cf}: '))
      c=c+(5.00*qf)
    co=input('Deseja acrescentar algo (s/n): ')
    if co == 's':
      p=True
    elif co == 'n':
      print(f'Total: R$ {c:.2f}')
      p=False