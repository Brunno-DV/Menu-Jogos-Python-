import random

print("************************************")
print("Olá, bem vindo ao jogo de advinhação")
print("************************************")

num_sec = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

print ("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define nível: "))

if (nivel == 1):
  total_tentativas = 20
elif (nivel == 2):
  total_tentativas = 10
elif (nivel == 3):
  total_tentativas = 5
else:
  print ("Nível inválido")

for rodada in range (1, total_tentativas+1):
  print("tentativas: {} de {}" .format(rodada, total_tentativas))
  
  chute_str = input("Digite o seu chute entre 1 e 100: ")
  print("Você digitou: ", chute_str)
  chute = int(chute_str)
  
  if(chute < 1 or chute > 100):
    print("Você deve digitar um número entre 1 e 100")
    continue

  acertou = num_sec == chute
  maior   = num_sec > chute
  menor   = num_sec < chute

  if(acertou):
    print("Você acertou!!! Fez {} pontos!!!".format(pontos))
    break
  else:
    if (maior):
      print("Você errou... Seu chute foi menor")
    elif (menor):
      print("Você errou... Seu chute foi maior") 
    pontos_perdidos = abs(num_sec - chute)
    pontos = pontos - pontos_perdidos
  
print("Fim do jogo")