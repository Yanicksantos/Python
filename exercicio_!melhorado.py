#Escreva um programa que leia 5 valores e encontre o maior e o menor deles. 
# Mostre o resultado.

print ("\nPor favor digite uma sequencia de 5 numeros!!!\n")
lista = []
pos = 1
for x in range (5):
    a = int (input (f"digite o {pos} numero: "))
    lista.append (a)
    pos += 1
print (f"\nos numeros digitados sao: {lista} respetivamente!\n")
b = max(lista)
c = min(lista)
print (f"Desses numeros, o maior deles eh {b} e o menor eh {c}.")
print ("\nOBRIGADOOOOOOOO!")