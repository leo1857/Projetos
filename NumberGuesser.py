#number guesser
import random       #random.randrange(start, end) nao inclui o numero do end 
                    #random.randint(start, end) agora inclui o numero do end

maximo = input("Digite ate que numero pode ser gerado aleatoriamente: ")
if (maximo.isdigit()):
    maximo = int(maximo)
    if maximo <= 0:
        print("Numero deveria ser maior do que zero.")
        quit()
else:
    print("precisava ser um numero.")
    quit()

numero = random.randint(0, maximo)
tentativas = 0
while True:
    tentativas += 1
    teste = input("Faca um chute do numero: ")
    if not(teste.isdigit()):
        print("precisava ser um numero.")
        continue
    else:
        teste = int(teste)
    if teste == numero:
        print("Parabens voce acertou!")
        print("Voce demorou", tentativas,"tentativas para acertar. Obrigado por jogar")
        break
    elif teste < numero:
        print("Voce errou, o numero e maior do que o seu teste")
    else:
        print("Voce errou, o numero e menor do que o seu teste")


