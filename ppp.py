import random

def obter_escolha_usuario():


    while True:
        escolha_usuario = input("\nEscolha entre:  Pedra🪨   Papel🧻  Tesoura✂ \n ").lower()

        if escolha_usuario == "pedra":
            print("Sua escolha foi 'Pedra🪨 ' !")
            return escolha_usuario
        elif escolha_usuario == "papel":
            print("Sua escolha foi 'Papel🧻 ' !")
            return escolha_usuario
        elif escolha_usuario == "tesoura":
            print("Sua escolha foi 'Tesoura✂ ' !")
            return escolha_usuario
        else:
            print("Escolha inválida. Por favor, escolha entre pedra🪨, papel🧻 ou tesoura✂.")


def gerar_escolha_computador():
   
    opcao =["papel", "pedra", "tesoura"]
    escolha_computador = random.choice(opcao)

    
    print("O seu oponente escolheu: '", escolha_computador, "'. \n")

    return(escolha_computador)

def determinar_vencedor(escolha_usuario, escolha_computador):
    
    if (escolha_usuario == "pedra" and escolha_computador == "tesoura"):
        return "você ganhou! (/^▽^)/ \n {}🪨 quebra a {}✂" .format(escolha_usuario, escolha_computador)
    elif(escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "você ganhou! (/^▽^)/ \n {}✂ corta o {}🧻" .format(escolha_usuario, escolha_computador)
    elif(escolha_usuario == "papel" and escolha_computador == "pedra"):
        return "você ganhou! (/^▽^)/ \n {}🧻 cobre a {}🪨" .format(escolha_usuario, escolha_computador)
    

    if (escolha_computador == "pedra" and escolha_usuario == "tesoura"):
        return "você perdeu! (╯︵╰,) \n {}🪨 quebra a {}✂" .format(escolha_computador, escolha_usuario)
    elif(escolha_computador == "tesoura" and escolha_usuario == "papel"):
        return "você perdeu! (╯︵╰,) \n {}✂ corta o {}🧻" .format(escolha_computador, escolha_usuario)
    elif(escolha_computador == "papel" and escolha_usuario == "pedra"):
        return "você perdeu! (╯︵╰,) \n {}🧻 cobre a {}🪨" .format(escolha_computador, escolha_usuario)
    

    elif escolha_usuario == escolha_computador:
        return "empate! ambos escolheram {}" .format(escolha_usuario)
    


def jogar_novamente():

    jogar_dnv = input("Deseja jogar de novo? (sim/não): ").lower()

    return jogar_dnv()


