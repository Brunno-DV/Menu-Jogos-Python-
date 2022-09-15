print("************************************")
print("Olá, bem vindo ao jogo de advinhação")
print("************************************")

num_sec = 42

chute_str = input("Digite o seu chute: ")

print("Você digitou: ", chute_str)

chute = int(chute_str)

if(num_sec == chute):
  print("Você acertou!!!")
else:
  print("Você errou...")

print("Fim do jogo")