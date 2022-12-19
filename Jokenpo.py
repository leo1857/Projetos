#pedra papel ou tesoura
import random

usuario = 0
computer = 0
movimentos = ["pedra","papel","tesoura"]

while True:
    p1 = input("Faca seu movimento (Pedra/Papel/Tesoura) ou digite Q para sair: ").lower()
    if (p1 == "q"):
        break
    
    if p1 not in movimentos:
        print("Digitou uma opcao invalida!")
        continue
    
    p2 = random.randint(0,2)
    p2 = movimentos[p2]
    print("O computador escolheu %s" %p2)
    if (p1 == "pedra") and (p2 == "tesoura"):
        print("voce ganhou!")
        usuario += 1
    elif (p1 == "papel") and (p2 == "pedra"):
        print("voce ganhou!")
        usuario += 1
    elif (p1 == "tesoura") and (p2 == "papel"):
        print("voce ganhou!")
        usuario += 1
    elif (p1 == "tesoura") and (p2 == "pedra"):
        print("voce perdeu!")
        computer += 1
    elif (p1 == "pedra") and (p2 == "papel"):
        print("voce perdeu!")
        computer += 1
    elif (p1 == "papel") and (p2 == "tesoura"):
        print("voce perdeu!")
        computer += 1
    else:
        print("Empatamos!")

print("A sua pontuacao foi: %d."%usuario)
print("A pontuacao do computador foi: %d."%computer)
if usuario > computer:
    print("Voce ganhou!!!")
elif usuario == computer:
    print("Voces empataram")
else:
    print("O computador ganhou")
