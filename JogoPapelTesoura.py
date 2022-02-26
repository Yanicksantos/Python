from random import choice


#PRIMEIRA FUNÇAO A SER CHAMADA
def Apresentacao():
    print (" ", 50*"*")
    print (18*"=", "PEDRA PAPEL TESOURA", 15*"=")
    print (" ", 50*"*")
    print (25*"=", "OLA", 24*"=")
    print (15*"=", "SEJA BEM VINDO AO JOGO", 15*"=")
    print (55*"-")
    print ("\n")
    

#FUNÇAO PARA ENTRADA DO NOME DO JOGADOR
def SeuNome():
    print ("Preciso conhecer o nome do meu desafiador, SEU OUSADO(A)!!!")
    nome = input ("\nQUEM É VOCE, PERDEDOR(A)?:")
    return nome.upper()

#ESCOLHA ALEATORIA DO NOME DA MAQUINA
def NomeMaquina(h):
    b = h
    nomeM = choice (["Kauan", "Meyri", "Isaac", "Julia", "Yanick", "Antunes", "João Vitor"])
    while (b == nomeM.upper()):
        NomeMaquina()
    if (nomeM =="Julia") or (nomeM =="Meyri"):
        return (f"{nomeM}, no modo braba")
    elif (nomeM =="Isaac") or (nomeM =="Kauan") or (nomeM == "Antunes"):
        return (f"{nomeM}, no modo Brabo")
    elif (nomeM =="Yanick"):
        return (f"{nomeM} modo PAPAI")
    else: return (f"{nomeM}, O CHEFE")


#LOGICA DA ESCOLHA DO JOGADOR
def EscolhaDoJogador():
    print (55*"-")
    print (18*"=", "PEDRA PAPEL TESOURA", 15*"=")
    print (55*"-")
    a = input ("\nQual sua escolha agora?\n ")
    if (a.upper() in ["PEDRA", "PAPEL", "TESOURA"] ):
        return a.upper()
    else: 
        cont = 0
        while (cont <= 4):
            if (cont == 0): 
                print ("\nESCOLHA INVALIDA!\nEspero que seja erro de escrita (SE FOR, MAIS ATENCAO NA PROXIMA, pfv)")
                print (55*"-")
                print (18*"=", "PEDRA PAPEL TESOURA", 15*"=")
                print (55*"-")
                a = input ("\nQual sua escolha agora?\n ")
                if (a.upper() in ["PEDRA", "PAPEL", "TESOURA"]): return a.upper()
                else: cont +=1
            elif (cont == 4):
                print ("\nEu Nao tenho tanta PACIENCIA ASSIM TA!!\nTCHAUUUUUU!!!")
                return "4"
            else:
                print ("\nInvalida de novo! Tenta outra vez pfv.")
                print (55*"-")
                print (18*"=", "PEDRA PAPEL TESOURA", 15*"=")
                print (55*"-")
                a = input ("\nQual sua escolha agora?\n ")
                if (a.upper() in ["PEDRA", "PAPEL", "TESOURA"] ): return a.upper()
                else: cont +=1


#ESCOLHA DA MAQUINA
def EscolhaMaquina():
    maquina = choice(["PEDRA", "papel", "Tesoura", "Pedra", "Papel" "TESOURA", "PAPEL", "pedra"])
    
    return maquina.upper()


#DEFININDO O VENCEDOR
def LogicaDoVencedor(opcaoj, opcaom):
    tent_1 = opcaoj
    tent_2 = opcaom
    if (tent_1 == "PEDRA") and (tent_2 == "TESOURA"):
        return "Infelizmente voce venceu\nSaiba que foi sorte"
    elif (tent_1 == "TESOURA") and (tent_2 == "PAPEL"):
        return "Infelizmente voce venceu\nSaiba que foi sorte"
    elif (tent_1 == "PAPEL") and (tent_2 == "PEDRA"):
        return "Infelizmente voce venceu\nSaiba que foi sorte"
    elif (tent_1 == tent_2):
        return "Empatou nessa contra a minha versão\nEu te desafio para mais uma"
    else: return "Voce perdeeeeeeeeu!!!kkkk\nEU JA SABIAAAA KKK\n FRACOTEEE"


#FUNÇÃO PRINCIPAL - Tudo está acontecendo aqui
Apresentacao()
a = SeuNome()
print (55*"-")
print (f"\nOk, ok! senhor(a) {a}, muito prazer!")
b = NomeMaquina(a)
print (f"\nDessa vez voce vai jogar com a minha versao {b}!\n")
OpcaoJ = EscolhaDoJogador()
OpcaoM = EscolhaMaquina()
print("\n")
print (18*"=", "RESULTADO", 18*"=")
print (55*"-")
print (f"{a} Voce escolheu: {OpcaoJ}\nA minha versao {b} escolheu: {OpcaoM}")
print (55*"-")
print("\n")
vamos = LogicaDoVencedor(OpcaoJ, OpcaoM)
print(f"****** | {vamos} | ******")

if (OpcaoJ != "4"):
    while True:
        seguir = input("\nDeseja jogar outra rodada: ")
        if (seguir.upper() in ["SIM", "S"]):
            OpcaoJ = EscolhaDoJogador()
            if (OpcaoJ == "4"):
                print ("\nA VIDA EH O QUE?\n")
                break
            else:
                OpcaoM = EscolhaMaquina()
                print("\n")
                print (18*"=", "RESULTADO", 18*"=")
                print (55*"-")
                print (f"{a} Voce escolheu: {OpcaoJ}\nA minha versao {b} escolheu: {OpcaoM}")
                print (55*"-")
                print("\n")
                vamos = LogicaDoVencedor(OpcaoJ, OpcaoM)
                print(f"****** | {vamos} | ******")
        elif (seguir.upper() in ["NAO", "N"]):
            break
        else: print ("\nEscolha Invalida! Tente Novamente ( lembre-se, sim ou nao).")
        
else: print ("\nA VIDA EH O QUE?\n")
print ("\nOBRIGADOH POR PARTICIPAR!!!\n")