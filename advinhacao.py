#Inicio
import random

print ("jogo de advinhação!")

#Variáveis iniciais
numero_chave = random.randrange(1,101)
pontos = 1000
print("Qual nível de dificuldade você quer?")
print("(1) fácil (2) médio (3) díficil")

nivel = int(input("Defina o nível: "))
facil = 1
medio = 2
dificil = 3

    
if(nivel == facil):
    total_de_tentativas = 20
elif(nivel == medio):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



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
        print("Você fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("seu chute foi maior que o número secreto!")
        if(menor):
            print("seu chute foi menor que o número secreto!")
        print("Errrooooouuuuuu!")
        pontos_perdidos = abs(numero_chave - chute)
        pontos = pontos - pontos_perdidos


print("fim de jogo")
