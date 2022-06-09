#Inicio
print ("jogo de advinhação!")

#Variáveis iniciais
numero_chave = 42
total_de_tentativas = 3
rodada = 1

#Processamento
for rodada in range(1, total_de_tentativas + 1):

    print("Tentativas {} de {}".format(rodada, total_de_tentativas))
    
    #Capturando e verificando valor do usuário
    numero = input("Digite um número entre 1 e 100: ")
    chute = int(numero)
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue



    #variáveis de resultado
    acertou = chute == numero_chave
    maior   = chute > numero_chave
    menor   = chute < numero_chave  
    
    #Checagem do acerto
    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("seu chute foi maior que o número secreto!")
        if(menor):
            print("seu chute foi menor que o número secreto!")
        print("Errrooooouuuuuu!")


print("fim de jogo")
