from ppp import * 

def main():

    while True:
        
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = gerar_escolha_computador()

        vencedor = determinar_vencedor(escolha_usuario, escolha_computador)

        print(vencedor)

        jogar_dnv = jogar_novamente()
        
        if jogar_dnv == "não":
            print("Jogo encerrado!!!")
            break

        elif jogar_dnv == "sim" :
            print("Reinicializando o jogo")        




if(__name__=="__main__"):
    main()