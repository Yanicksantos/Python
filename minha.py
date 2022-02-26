
print (25*" ", "OLA meu amor\n", 80*"#", "\n\n", 15*" ","SEJA BEM VINDA A NOSSA BRINCADEIRA\n", 80*"#")
print ("\nPrimeiro passo para ter sucesso nessa brincadeira, eh ter atencao aos detathes!!\n")
print ("Ta preparada Fidaputa??\n")
a = str(input ("Digite SIM ou Nao, para continuarmos: "))
a = a.upper()
if a != "SIM" and a != "NAO":
    print ("\n Oh FIIIDAPUTA, eh para digitar sim ou não!!\n")
    print ("A gente vai mais uma fez caraioooo!\n")
    a = str (input ("\nDigite logo esse sim ou nao, pq NAO ME RESPONSABILIZO?:  "))
a = a.upper()

while a != "SIM" and a != "NAO":
    print ("\n SUA CUUUUU \n MAIS UMA VEZ!!!! \n")
    a = str(input ())
    a = a.upper()

if a == "SIM":
    print ("\n Agora vamos la. Testando a sua atenção Take 1")
    print ("\n Qual seu nome?")
    nome = str(input ())
    nome = nome.upper()
    if nome != "FIDAPUTA":
        print ("\nVOCE EH BURRA MEMO")
        print ("\nPista: SEU NOME JA FOI CITADO!")
        print ("\nVai la. Digite de novo:\n")
        nome = str(input ())
        nome = nome.upper()
        if nome != "FIDAPUTA":
            print ("\n\nBURRA PRA CARAIOOOO!!!")
            print ("\nA partir de agora voce tem 3 chances!")
            cont = 1
            while nome != "FIDAPUTA" and cont <= 3:
                print ("\nVOCE USOU A SUA {0} TENTATIVA".format(cont))
                print ("\nVolto a lembrar a senhora que seu nome ja foi citado")
                print ("\nMAIS UMA VEZ. Vamos la!!!!\n")
                print ("\nQual é o seu nome????")
                nome = str(input ())
                nome = nome.upper()
                cont = cont + 1
            print ("\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print ("\nOBRIGADOOOO!!!")
            print ("\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&z\n")
            print ("\n\nNA PROXIMA TEREI APRENDIDO MAIS E VOU BRINCAR MELHOR, PROMETO!\n\n ")
            
else: print ("\n\n===      VOCE QUE PERDE SUA FIDAPUTA. TCHAUUUUUUUUU!!!     ====\n\n ")
