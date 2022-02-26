"""03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10."""
def Inicio():
    print (6*" ", 50*"*")
    print(15*"=", "EXERCICIO 1 - CALCULADORA: CHAMADA DE FUNCOES", 15*"=")
    print (6*" ", 50*"*")
    print (55*"-")


def Menu():
    print (" ", 50*"*")
    print(5*" ",15*"=", "CALCULADORA", 15*"=")
    print (" ", 50*"*")
    print (55*"-")
    print("1 - SOMA", 21*" ",  "2 - SUBTRACAO\n")
    print("3 - MULTICACAO", 15*" ",  "4 - DIVISAO\n")
    print("5 - RAIZ QUADRADA", 12*" ",  "6 - PERCENTAGEM\n")
    print("7 - FRACAO INVERSA (1/X)", 5*" ",  "8 - POTENCIACAO (POR 2)")
    print (55*"-")


def Somar():
    print (55*"-")
    print ("=========== SOMAR ============")
    print("Digite 2 numeros para saber o resultado da soma.")
    n1 = float(input("digite o primeiro numero:  \n"))
    n2 = float(input("digite o segundo numero:  \n"))
    soma = n1 + n2
    print (55*"-")
    print(f"\nResultado da SOMA:  {soma}\n")


def Subtrair():
    print (55*"-")
    print ("=========== SUBTRAIR ============")
    print("Digite 2 numeros para saber o resultado da subtracao.")
    n1 = float(input("digite o primeiro numero:  \n"))
    n2 = float(input("digite o segundo numero:  \n"))
    sub = n1 - n2
    print (55*"-")
    print(f"\nResultado da SUBTRACAO:  {sub}\n")


def Multicar():
    print (55*"-")
    print ("=========== MULTIPLICAR ============")
    print("Digite 2 numeros para saber o resultado da multiplicacao.")
    n1 = float(input("digite o primeiro numero:  \n"))
    n2 = float(input("digite o segundo numero:  \n"))
    multi = n1 * n2
    print (55*"-")
    print(f"\nResultado da MULTIPLICACAO:  {multi}\n")


def Dividir ():
    print (55*"-")
    print ("=========== DIVIDIR ============")
    print("Digite 2 numeros para saber o resultado da divisao.")
    n1 = float(input("digite o primeiro numero:  \n"))
    n2 = float(input("digite o segundo numero:  \n"))
    divis = n1 / n2
    print (55*"-")
    print("\nResultado da DIVISAO:  {:.3f}\n".format(divis))


def RaizQuadrada():
    print (55*"-")
    print ("=========== RAIZ QUADRADA ============")
    print("Digite o numero para saber o resultado da raiz quadrada dele.")
    n1 = float(input("digite o numero:  \n"))
    raizqua = n1**0.5
    print (55*"-")
    print("\nResultado da RAIZ QUADRADA:  {:.3f}\n".format(raizqua))


def Percentagem():
    print (55*"-")
    print ("=========== PERCENTAGEM ============")
    print("Digite os numeros para saber o resultado.")
    n1 = float(input("Qual numero voce quer saber a pergentagem:  \n"))
    n2 = float(input(f"Quantos % vc quer de {n1}:  \n"))
    per = (n1*n2)/100
    print (55*"-")
    print("\nResultado da PERCENTAGEM:  {:.2f}\n".format(per))


def FracaoInversa():
    print (55*"-")
    print ("=========== FRACAO INVERSA (1/X) ============")
    print("Digite O numero para saber o resultado da sua fracao inversa.")
    n1 = float(input("digite o numero:  \n"))
    fracc = 1 / n1
    print (55*"-")
    print("\nResultado da FRACAO INVERSA:  {:.5f}\n".format(fracc))


def Potencia ():
    print (55*"-")
    print ("=========== POTENCIA (POR 2) ============")
    print("Digite O numero para saber o sua potencia quadratica.")
    n1 = float(input("digite o numero:  \n"))
    quadrad = n1**2
    print (55*"-")
    print("\nResultado :  {:.2f}\n".format(quadrad))


cont = 0
while True:
    Menu()
    while True:
        if cont == 5: break
        escolha = int(input("Escolha uma das opcoes:  "))
        if escolha in [1, 2, 3, 4, 5, 6, 7, 8]:
            break
        else: 
            print ("Opcao Invalida!\n TENTE OUTRA VEZ\n")
            cont +=1
    if cont == 5:
        print (" ", 50*"*")
        botao = input("Estamos com dificuldades de entende-lo no momento!\nPROGRAMA IRA ENCERRAR APOS CLICAR ENTER")
        print("\n Espero ter ajudado.\n ======== Obrigado!!! ======== ")            
        break
    print (55*"-")
    if escolha == 1: Somar()
    elif escolha == 2: Subtrair()
    elif escolha == 3: Multicar()
    elif escolha == 4: Dividir()
    elif escolha == 5: RaizQuadrada()
    elif escolha == 6: Percentagem()
    elif escolha == 7: FracaoInversa()
    else: Potencia()
    botao = input ("\nDeseja voltar ao Menu\nSIM - Para continuar\nNAO - para SAIR\n")
    if botao in ["SIM", "S", "sim", "s"]:
        pass
    elif botao in ["NAO", "N", "nao", "n"]:
        print (" ", 50*"*")
        print("\n Espero ter ajudado.\n ======== Obrigado!!! ======== ")
        break
    else:
        print (" ", 50*"*")
        botao = input("Estamos com dificuldades de entende-lo no momento!\nPROGRAMA IRA ENCERRAR APOS CLICAR ENTER")
        print("\n Espero ter ajudado.\n ======== Obrigado!!! ======== ")            
        break

#Comandos try, catch e finally