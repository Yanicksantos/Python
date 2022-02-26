"""02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros)."""

def Inicio():
    print (6*" ", 50*"*")
    print(15*"=", "EXERCICIO 2 - POTENCIACAO: CHAMADA DE FUNCOES", 15*"=")
    print (6*" ", 50*"*")


def potenciacao(BASE, EXP):
    pot = BASE**EXP
    print("\nAguarde!!")
    print(f"\n{BASE} elevado a {EXP} resulta em: {pot}")


Inicio()
while True:
        print (55*"-")
        base = int (input("Digite a sua base: "))
        exp = int (input("Digite o expoente: "))
        potenciacao(base, exp)
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

