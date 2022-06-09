print("Bem vindo ao jogo de advinhação")
numero_secreto = 42
numero = input("digite seu número: ")
chute = int(numero)
print("voce digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
