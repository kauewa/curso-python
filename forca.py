from operator import index


def jogo():
    print("jogo da forca")

    palavar_secreta = "banana"

    enforcou = False
    acertou = False


    while(not enforcou and not acertou):
        chute = input("Qual letra?")

        index = 0
        for letra in palavar_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando ...")

    print("Fim de jogo!")




if(__name__ == "__main__"):
    jogo()
