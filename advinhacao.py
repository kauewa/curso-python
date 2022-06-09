#Inicio
print ("jogo de advinhação!")
numero = input("Digite um número: ")

print ("seu número é: ", numero)

#Variáveis
chute = int(numero)
numero_chave = 42

acertou = chute == numero_chave
maior   = chute > numero_chave
menor   = chute < numero_chave

#Processamento
if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("seu chute foi maior que o número secreto!")
    if(menor):
        print("seu chute foi menor que o número secreto!")

    print("Errrooooouuuuuu!")

print("fim de jogo")