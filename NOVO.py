"""lista = input().split()
A = round(float (lista[0]), 1)
B = round(float (lista[1]), 1)
C = round(float (lista[2]), 1)
area1 = ((A*C)/2)
print ("TRIANGULO: {:.3f}".format(area1))
pi = 3.14159
area2 = (pi*(C**2))
print ("CIRCULO: {:.3f}".format(area2))
area3 = ((A+B)*(C/2))
print ("TRAPEZIO: {:.3f}".format(area3))
area4 = (B**2)
print ("QUADRADO: {:.3f}".format(area4))
area5 = (A*B)
print ("RETANGULO: {:.3f}".format(area5))"""

"""lista_1 = input().split()
c1 = int (lista_1[0])
n1 = int (lista_1[1])
v1 = round (float(lista_1[2]),2)
lista_2 = input().split()
c2 = int (lista_2[0])
n2 = int (lista_2[1])
v2 = round (float(lista_2[2]),2)
valor = ((n1*v1)+(n2*v2))
print ("VALOR A PAGAR: R$ {:.2f}".format(valor))"""

"""while True:
    n = int (input())
    if n>0 and n<1000000: break
print (f"{n}")
cont = 0
while n >= 100:
    cont += 1
    n -= 100
print (f"{cont} nota (s) de R$ 100,00")
cont = 0
while n >= 50:
    cont += 1
    n -= 50
print (f"{cont} nota (s) de R$ 50,00")
cont = 0
while n >= 20:
    cont += 1
    n -= 20
print (f"{cont} nota (s) de R$ 20,00")
cont = 0
while n >= 10:
    cont += 1
    n -= 10
print (f"{cont} nota (s) de R$ 10,00")
cont = 0
while n >= 5:
    cont += 1
    n -= 5
print (f"{cont} nota (s) de R$ 5,00")
cont = 0
while n >= 2:
    cont += 1
    n -= 2
print (f"{cont} nota (s) de R$ 2,00")
cont = 0
while n >= 1:
    cont += 1
    n -= 1
print (f"{cont} nota (s) de R$ 1,00")"""

"""valor = int (input())
print (valor)
for x in [100, 50, 20, 10, 5, 2, 1]:
    n = valor // x
    print (f"{n} nota(s) de R$ {x},00")
    valor = valor%x"""


"""N = int (input())
h = N // 3600
m = (N % 3600) // 60
s = (N % 3600) % 60
print (f"{h}:{m}:{s}")"""

'''d = int (input())
a = d // 365
m = (d % 365) // 30
dias = (d % 365) % 30
print (f"{a} ano(s)")
print (f"{m} mes(es)")
print (f"{dias} dia(s)")'''

'''valor = float(input())
print ("NOTAS:")
for x in [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]:
    n =  int (valor / x)
    print ( "{} nota(s) de R$ {:.2f}".format(n,x))
    valor = valor % x
print ("MOEDAS:")
for x in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
    n = int (round (valor,2) / x)
    print ("{} moeda(s) de R$ {:.2f}".format(n,x))
    valor = valor % x'''

valores = input().split()
A = int (valores [0])
B = int (valores [1])
C = int (valores [2])
D = int (valores [3])
if B > C and D > A:
    if (C + D) > (A + B):
        if C > 0 and D > 0:
            if A % 2 == 0:
                print ("Valores aceitos")
            else: print ("Valores nao aceitos")        
        else: print ("Valores nao aceitos")
    else: print ("Valores nao aceitos")    
else: print ("Valores nao aceitos")    