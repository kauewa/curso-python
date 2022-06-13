from operator import index
import random


def jogo():
    print("jogo da forca")

    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavar_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavar_secreta]

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavar_secreta):
            index = 0
            for letra in palavar_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1


        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if(acertou):
        print("Você acertou")
    else:
        print("você perdeu")
    


        print(letras_acertadas)

        print("jogando ...")

    print("Fim de jogo!")




if(__name__ == "__main__"):
    jogo()
