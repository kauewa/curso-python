#Inicio
print ("jogo de advinhação!")

#Variáveis iniciais
numero_chave = 42
total_de_tentativas = 3
rodada = 1

#Processamento
while(rodada <= total_de_tentativas):

    print("Tentativas", rodada, "de 3")
    
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
        total_de_tentativas = 0
    else:
        if(maior):
            print("seu chute foi maior que o número secreto!")
        if(menor):
            print("seu chute foi menor que o número secreto!")
        print("Errrooooouuuuuu!")
        rodada = rodada + 1

print("fim de jogo")
