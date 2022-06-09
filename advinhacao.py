print ("jogo de advinhação!")

numero = input("Digite um número: ")
chave = int(numero)
print ("seu número é: ", chave)
numero_chave = 42


if(numero_chave == numero):
    print("Você acertou!")
else:
    print("Errrooooouuuuuu!")

print("fim de jogo")