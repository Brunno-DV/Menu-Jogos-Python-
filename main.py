print("************************************")
print("Olá, bem vindo ao jogo de advinhação")
print("************************************")

num_sec = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
  print("tentativas: {} de {}" .format(rodada, total_tentativas))
  
  chute_str = input("Digite o seu chute: ")
  print("Você digitou: ", chute_str)
  chute = int(chute_str)
  
  acertou = num_sec == chute
  maior   = num_sec > chute
  menor   = num_sec < chute

  if(acertou):
    print("Você acertou!!!")
  else:
    if (maior):
      print("Você errou... Seu chute foi menor")
    elif (menor):
      print("Você errou... Seu chute foi maior")

  rodada = rodada + 1  
  
print("Fim do jogo")