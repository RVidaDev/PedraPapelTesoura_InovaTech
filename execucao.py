from funcoes import * 
from time import sleep

def main():

    delay = 1.5
    print("\n\033[1;36m========== Bem vindo ao JOKENPO! ==========\033[m")
    sleep(delay)
    while True:

        
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = gerar_escolha_computador()

        vencedor = determinar_vencedor(escolha_usuario, escolha_computador)

        print(vencedor)

        jogar_dnv = jogar_novamente()
        
        if jogar_dnv == "não" or jogar_dnv == "nao":
            print("Jogo encerrado!!!")
            break

        elif jogar_dnv == "sim" :
            print("Reinicializando o jogo")        




if(__name__=="__main__"):
    main() 