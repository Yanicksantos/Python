
numero = int(input("\nDigite um numero para a nossa avaliacao:\n "))
x = 1
cont = 1
if numero <= 1:
    numero = int (input("Digite um numero maior que 1, por favor: "))
    while numero <= 1 and cont <=2:
        cont += 1
        numero = int (input("\nMinha paciencia ACABA. Digite logo um numero valido:\n  "))
if cont < 2 or numero > 1:
    while x != 100:
        x += 1
        if (numero % x) == 0:
            if numero == 2:
                print ("\n2 eh um numero primo\n\n OBRIGADO!!!\n")
            elif numero == x: pass
            else: print (f"\n {numero} Nao eh numero primo.\n \n OBRIGADO!!!\n")
            break
        else: print (f" {numero} eh um numero primo.\n \n OBRIGADO!!!\n")
        break
else:
    print ("\nAchou que eu tava brinacando?\n")
    print ("VSF Fidaputa\n")





