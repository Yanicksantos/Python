"""01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;"""

def Inicio():
    print (6*" ", 50*"*")
    print(15*"=", "EXERCICIO 1 - CHAMADA DE 2 FUNCOES", 15*"=")
    print (6*" ", 50*"*")
    print ("\n     ANTES DE INICIARMOS, VOCE VAI PRECISAR DIGITAR 2 NUMEROS!\n")


def Menu():
    print (" ", 50*"*")
    print(8*" ",15*"=", "MENU", 15*"=")
    print (" ", 50*"*")
    print("\n")
    print("Escolha uma das opcoes!")
    print (55*"-")
    print("1 - O MAIOR ENTRE ELES\n2 - A MEDIA ARITMETRICA DELES")
    print (55*"-")


def Maior(n1, n2):
    print (55*"-")
    print(f"\nVoce digitou {n1} e {n2}") 
    if n1 == n2: print (f"\n Nenhum deles eh maior. {n2} e {n1} São iguais. ")
    elif n1 > n2: print(f"\n----> {n1} eh maior que {n2}\n")
    else: print(f"\n----> {n2} eh maior que {n1}\n")


def Media(n1, n2):
    print (55*"-")
    med = float((n1 + n2)/2)
    print(f"\nVoce digitou {n1} e {n2}") 
    print ("\nA sua media eh: {:.2f}".format(med))


#FUNÇÃO PRINCIPAL
Inicio()
while True:
    Num1 = int (input("\nPode digitar o primeiro: "))
    Num2 = int (input("\nAgora pode digitar o segundo: "))
    print (55*"-")
    Menu()
    while True:
        Escolha = int (input("O que pretente saber agora?\n"))
        if (Escolha == 1 or Escolha == 2):break
        else: print ("Opcao INVALIDA. tente novamente!\n")
    if Escolha == 1:
        Maior(Num1, Num2)
    else:
        Media(Num1, Num2)
    print (80*"*")
    botao = input ("\nDeseja repetir?\nSIM - Para continuar\nNAO - para SAIR\n")
    if botao in ["SIM", "S", "sim", "s"]:
        print (" ", 50*"*")
    elif botao in ["NAO", "N", "nao", "n"]:
        print (" ", 50*"*")
        print("\n Espero ter ajudado.\n ======== Obrigado!!! ======== ")
        break
    else:
        print (" ", 50*"*")
        botao = input("Estamos com dificuldades de entende-lo no momento!\nPROGRAMA IRA ENCERRAR APOS CLICAR ENTER")
        print("\n Espero ter ajudado.\n ======== Obrigado!!! ======== ")            
        break

    