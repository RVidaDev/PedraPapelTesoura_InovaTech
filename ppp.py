import random

def obter_escolha_usuario():

    while True:
        escolha_usuario = input("Escolha entre: pedra, papel ou tesoura : ").lower()

        if escolha_usuario == "pedra":
            print("Sua escolha foi pedra!")
            return escolha_usuario
        elif escolha_usuario == "papel":
            print("sua escolha foi papel")
            return escolha_usuario
        elif escolha_usuario == "tesoura":
            print("sua escolha foi tesoura")
            return escolha_usuario
        else:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")

def gerar_escolha_computador():
   
    opcao =["papel", "pedra", "tesoura"]
    escolha_computador = random.choice(opcao)
    
    print("o computador escolheu: ", escolha_computador)

    return(escolha_computador)

def determinar_vencedor(escolha_usuario, escolha_computador):
    
    if (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
        (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
        (escolha_usuario == "papel" and escolha_computador == "pedra"):
                return "você ganhou! {} é maior que {}" .format(escolha_usuario, escolha_computador)
    elif escolha_usuario == escolha_computador:
        return "empate! ambos escolheram {}" .format(escolha_usuario)
    else:
        return "você perdeu. {} é maior que {}" .format(escolha_computador, escolha_usuario)


def jogar_novamente():

    jogar_dnv = input("Deseja jogar de novo? (sim/não): ").lower()