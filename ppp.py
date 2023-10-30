import random

def obter_escolha_usuario():
    escolha_usuario = input("pedra, papel ou tesoura?: ").lower()

    if escolha_usuario == "pedra":
        print("Sua escolha foi pedra!")
        return escolha_usuario
    elif escolha_usuario == "papel":
        print("sua escolha foi papel")
        return escolha_usuario
    elif escolha_usuario == "tesoura":
        print("sua escolha foi tesoura")
        return escolha_usuario

def gerar_escolha_computador():
   
    opcao =["papel", "pedra", "tesoura"]
    escolha_computador = random.choice(opcao)
    
    print("o computador escolheu: ", escolha_computador)

    return(escolha_computador)

def determinar_vencedor(obter_escolha_usuario, gerar_escolha_computador):
    
    if (obter_escolha_usuario == "pedra" and gerar_escolha_computador == "tesoura") or \
        (obter_escolha_usuario == "tesoura" and gerar_escolha_computador == "papel") or \
        (obter_escolha_usuario == "papel" and gerar_escolha_computador == "pedra"):
                return "você ganhou! {} é maior que {}" .format(obter_escolha_usuario, gerar_escolha_computador)
    elif obter_escolha_usuario == gerar_escolha_computador:
        return "empate! ambos escolheram {}" .format(obter_escolha_usuario)
    else:
        return "você perdeu. {} é maior que {}" .format(gerar_escolha_computador, obter_escolha_usuario)


def jogar_novamente():
    
    jogarAgain = input("deseja jogar de novo?: ").lower
    
    while jogarAgain == "sim":
        print("ok, vou rodar de novo")
        return jogar_novamente
        
    


def jogar():

if(__name__=="__main__"):
    jogar()