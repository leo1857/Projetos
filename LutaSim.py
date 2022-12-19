#Teste de combate 1v1, tentando otimizar o que puder
import random

"""
def sorte (x,y):
    baixo = random.randint(x,y)
    alto = random.randint(x,y)
    if baixo < alto:
        return alto
    else:
        return sorte(x,y)
"""


def overcura(x,y,z):
    overheal = x + y - z
    x = x + y - overheal
    return x



movimentos = ["ataque","bloqueio","curar", "ataque"]
vida_inimigo_max = random.randint(10, 50)
dano_inimigo_min = random.randint(3, 8)
dano_inimigo_max = random.randint(10, 15)
bloq_inimigo_min = random.randint(2, 4)
bloq_inimigo_max = random.randint(6, 10)
cura_inimigo_min = random.randint(1, 4)
cura_inimigo_max = random.randint(6, 10)
vida_inimigo = vida_inimigo_max

hp_max = 20
hp = hp_max
print("Voce encontra um inimigo. Preparado para luta?")
print("Seus status sao:\nAtaque: 5-10\nBloqueio: 3-6\nCura: 2-4\nHP: 20")
print("Os status do seu oponente serao escolidos aleatoriamente\nO fugir vai permitir voce fugir se o inimigo nao te atacar nesse turno.")
while (vida_inimigo > 0) and (hp > 0):
    #resetar os valores das mecanicas, volta elas pra 0
    dano = 0
    bloq = 0
    cura = 0
    dano_inimigo = 0
    bloq_inimigo = 0
    cura_inimigo = 0
    
    #pular algumas linhas para nao ficar tudo junto
    print("\n\n\n")

    #recebe o movimento do player, mostra os status do inimigo e a vida atual do player
    print("Vida do inimigo: %d\nDano do inimigo: %d-%d\nBloqueio do inimigo: %d-%d\nCura do inimigo: %d-%d"% (vida_inimigo, dano_inimigo_min, dano_inimigo_max,bloq_inimigo_min,bloq_inimigo_max,cura_inimigo_min,cura_inimigo_max))
    print ("Seu hp = %d" %hp)
    player = input("O que voce quer fazer? (Ataque, Bloqueio, Curar ou Fugir) ").lower()
    while (player != "ataque") and (player != "bloqueio") and (player != "curar") and (player != "fugir"):
        print("Escolha invalida")
        player = input("O que voce quer fazer? (Ataque, Bloqueio ou Curar)").lower()
    
    #Escolhe o movimento do inimigo
    inimigo = random.randint(0,3)
    inimigo = movimentos[inimigo]

    #faz as mecanicas do que o player escolheu
    if (player == "ataque"):
        dano = random.randint(5,10)
    elif (player == "bloqueio"):
        bloq = random.randint(3,6)  
        print("Voce consegue bloquear %d de dano esse turno"%bloq)  
    elif (player == "curar"):
        cura = random.randint(2,4)
        print("Sua cura foi de %d" %cura)
    else:
        if (inimigo != "ataque"):
            print("Voce conseguiu fugir e o inimigo nao conseguiu te alcancar!")
            break
        else:
            print("Quando voce tenta fugir o inimigo te ataca pelas costas.")

    #faz as mecanicas do que o inimigo escolheu
    if (inimigo == "ataque"):
        dano_inimigo = random.randint(dano_inimigo_min,dano_inimigo_max)
    elif (inimigo == "bloqueio"):
        bloq_inimigo = random.randint(bloq_inimigo_min,bloq_inimigo_max)
        print("O inimigo esta tentando bloquear %d de dano esse turno"%bloq_inimigo)
    else:
        cura_inimigo = random.randint(cura_inimigo_min,cura_inimigo_max)
        print("Inimigo curou %d de vida"%cura_inimigo)
    
    #cura tanto do player quanto do inimigo quando eles curarem
    if (player == "cura"):
        if (hp + cura <= hp_max):
            hp += cura
        else: 
            overcura(hp,cura,hp_max)
    if (inimigo == "cura"):
        if (vida_inimigo + cura_inimigo <= vida_inimigo_max):
            vida_inimigo += cura_inimigo
        else: 
            overcura(vida_inimigo,cura_inimigo,vida_inimigo_max)
    
    #reduzir o dano do ataque com o bloqueio do inimigo e do player e realizar os ataques
    dano -= bloq_inimigo
    dano_inimigo -= bloq
    if (dano > 0):
        vida_inimigo -= dano
        print("Voce deu %d de dano no inimigo"%dano)
    elif (dano <= 0) and (inimigo == "bloqueio"):
        print("O inimigo bloqueou todo seu ataque!")
    if (vida_inimigo > 0):    
        if (dano_inimigo > 0):
            hp -= dano_inimigo
            print("Voce recebeu %d de dano do inimigo"%dano_inimigo)
        elif (dano_inimigo <= 0) and (player == "bloqueio"):
            print("Voce bloqueou todo o dano do ataque inimigo!")
    
#Identificacao de quem ganhou o combate e as mensagens apropriadas
if (vida_inimigo < 0):
    print("Voce conseguiu derrotar o inimigo! Parabens!!")
if (hp < 0):
    print("Voce morreu.... Melhor sorte da proxima vez.")  

        