#Escreva um programa que leia 5 valores e encontre o maior e o menor deles. 
# Mostre o resultado.
print ("\nPor favor digite uma sequencia de 5 numeros!!!\n")
a = int (input ("digite o 1 numero: "))
b = int (input ("digite o 2 numero: "))
c = int (input ("digite o 3 numero: "))
d = int (input ("digite o 4 numero: "))
e = int (input ("digite o 5 numero: "))
menor = a
maior = b
if menor > maior:
    menor = b
    maior = a
if menor > c: menor = c
if maior < c: maior = c
if maior < d: maior = d
if menor > d: menor = d
if maior < e: maior = e
if menor > e: menor = e
print (f"\nOs numeros digitados : [{a}, {b}, {c}, {d}, {e}] respetivamente!\n")
print (f"Desses numeros, o maior deles eh {maior} e o menor eh {menor}.")
print ("\nOBRIGADOOOOOOOO!\n")