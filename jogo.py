import forca
import advinhacao

def escolhendo_jogo():
    print("Escolha seu jogo!")
    print("(1)jogo da forca  (2)Jogo de advinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("jogo da forca")
        forca.jogo()
    elif(jogo == 2):
        print("jogo de advinhacao")
        advinhacao.jogo()


if(__name__ == "__main__"):
    escolhendo_jogo()
