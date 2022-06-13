import random



def jogo():
    abertura()
    palavra_secreta = palavra_Secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
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




def abertura():
    print("jogo da forca")



def palavra_Secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta



def inicializa_letras_acertadas(palavra):
    ["_" for letra in palavra]



def pede_chute():
    input("Qual letra?")
    chute = chute.strip().upper()
    return chute



def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1





if(__name__ == "__main__"):
    jogo()
