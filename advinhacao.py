#Inicio
print ("jogo de advinhação!")

#Variáveis iniciais
numero_chave = 42
total_de_tentativas = 3
rodada = 1

#Processamento
for rodada in range(1, total_de_tentativas + 1):

    print("Tentativas {} de {}".format(rodada, total_de_tentativas))
    
    #Capturando valor do usuário
    numero = input("Digite um número: ")
    chute = int(numero)

    #variáveis de resultado
    acertou = chute == numero_chave
    maior   = chute > numero_chave
    menor   = chute < numero_chave  
    
    #Checagem do acerto
    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("seu chute foi maior que o número secreto!")
        if(menor):
            print("seu chute foi menor que o número secreto!")
        print("Errrooooouuuuuu!")


print("fim de jogo")
