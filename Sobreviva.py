#Choose your adventure game


nome = input("Digite seu nome: ")
print("Seja bem-vindo %s, espero que esteja pronto para sua aventura"%nome)
print("Regras do jogo: \nO que deve ser digitado para valer a resposta estara entre parenteses;")
print("Voce so tem uma vida, use-a bem;\nSe divirta!")
print("\n\n\n")

print("Voce esta perdido em uma floresta, sem lembrancas de como foi parar nela.\nA primeira coisa que voce precisa fazer e encontrar uma cidade.")
escolha = ("Voce esta em uma bifurcacao. Qual caminho voce quer seguir (Esquerda ou Direita)?").lower()
if (escolha == "esquerda"):
    print("\n....\n")
    escolha = input("Voce encontra um lago. Voce quer nadar para atravessar o lago ou quer seguir ele subindo (Nadar ou Seguir)?").lower()
    if (escolha == "nadar"):
        print("\n......\n")
        print("Voce entra no lago e percebe que o lago e mais fundo do que parecia.")
        print("Quando voce chega na metade do lago voce sente algo passando na sua perna.\nUm crocodilo morde a sua perna...")
        print("Voce perdeu")
        quit()
    elif (escolha == "seguir"):
        print("\n......\n")
        print("Voce segue o riu, depois de alguns minutos andando voce encontra uma casa, ela parece abandonada.")
        print("Entrando na casa voce logo se depara com uma mesa cheia de comidas, mas voce nao encontra ninguem por mais que voce procure.")
        escolha = input("Voce esta com fome, decide comer o que esta na mesa ou ir em bora? (Comer ou Voltar)").lower()
        if (escolha == "comer"):
            print("\n.......\n")
            print("Voce comeca a comer do que estava na mesa e sente que tem alguma coisa errada, voce comeca a perder a consiencia...")
            print("Voce perdeu!!\nSo um gordinho iria comer em uma situacao dessas....")
            quit()
        elif (escolha == "voltar"):
            print("Voce volta para a floresta e continua perdido")
            print("Voce perdeu!!\nAs vezes a gente so nao da sorte no caminho escolhido.")    
            quit()
        else:
            print("Escolha invalida\nVoce perdeu!!")
            quit()
    else:
        print("Escolha invalida\nVoce perdeu!!")
        quit()
elif (escolha == "direita"):
    print("Voce caminha pela trilha e sente um cheiro de queimado depois de andar por alguns minutos.")
    escolha = input("Voce quer ir investigar o cheiro ou apenas continuar pela trilha? (Investigar ou Continuar)").lower()
    if (escolha == "investigar"):
        print("\n.....\n")
        print("Voce encontra um acampamento com 3 pessoas se preparando para partir. Voce pode ver onde estao os equipamentos e recursos deles.")
        escolha = input("Voce consegue pegar as coisas deles e seguir com a sua vida ou voce pode tentar falar com eles.\nQual voce escolhe? (Pegar ou Falar)").lower()
        if (escolha == "pegar"):
            print("\n.....\n")
            print("Voce consegue pegar as coisas deles sem ser percebido. Nas mochilas voce encontra uma arma, municao, comida por pelo menos uma semana e um saco de dormir.")
            print("Voce continua andando pela floresta, esta anoitecendo. Voce encontra uma caverna.")
            escolha = input("Voce decide passar a noite na caverna ou procurar um lugar para fazer uma fogueira? (Caverna ou Fogueira)").lower()
            if (escolha == "caverna"):
                print("\n......\n")
                print("Voce abre o saco de dormir e se acomoda da melhor forma possivel para passar a noite.")
                print("No meio da noite voce escuta um barulho estranho e quando voce olha tem um urso se aproximando de voce.")
                print("Voce perdeu!!\nDormir numa caverna sem ter a sua arma pronta nao foi a melhor das ideias.")
                quit()
            elif (escolha == "fogueira"):
                print("\n......\n")
                print("Voce encontra um lugar que parece tranquilo para montar uma fogueira. Com a fogueira acessa voce arruma o saco de dormir e da boa noite para as arvores ao seu redor.")
                print("A noite pra voce passa tranquila e voce acorda com energia suficiente para encontrar a sua salvacao.")
                print("Depois de mais algumas horas voce encontra uma rua e espera um carro passar para pedir ajuda.")
                print("\nMeus parabens, voce foi salvo!!!\nMas voce roubou de gente que voce nem conhecia... Vamos torcer pra que ninguem descubra isso.")
                quit()
            else:
                print("Escolha invalida!\nVoce perdeu!!")
                quit()
        elif (escolha == "falar"):
            print("\n........\n")
            print("Quando voce comeca a falar os tres viram para voce e se assustao com o seu estado. Eles entendem o seu lado e falam que estavam cacando pela area.")
            print("Os cacadores ajudam voce a sair vivo da floresta.")
            print("Meus parabens, voce foi salvo!!!\nQue sorte que voce encontrou pessoas no meio da florestaem.")
            quit()
        else:
            print("Escolha invalida!\nVoce perdeu!!")
            quit()
    elif (escolha == "continuar"):
        print("\n.....\n")
        print("Voce vai seguindo a trilha e a luz do dia vai passando, voce esta sentindo que precisara de um descanso em breve.")
        escolha = input("Voce se sente cansado, mas talvez se caminhar por mais algumas horas vai chegar em algum lugar. Voce decide parar para descansar ou vai continuar a viagem? (Parar ou Continuar)").lower()
        if (escolha == "parar"):
            print("\n......\n")
            print("Voce para e tenta descansar durante a noite, mas sem nenhum equipamento e com o frio da floresta voce nao acorda muito bem")
            print("Mesmo sentindo os efeitos da da hipotermia voce decide continuar no seu caminho....\nDpois de duas horas andando nao encontra nada")
            escolha = input("Voce pensa que tem uma escolha a ser tomada...Voce pode continuar andando pra tentar encontrar algo ou pode so aceitar seu destino.\nQual a sua escolha? (Andar ou Aceitar)").lower()
            if (escolha == "andar"):
                print("Depois de tanto sofrimento voce ainda quer continuar... Impressionante")
                print("Mais 30 minutos andando e voce encontra uma estrada movimentada, voce cai de joelhos no chao, sua expressao e de pura alegria e uma lagrima escorre pelo seu rosto")
                print("Nao demora muito ate alguem parar e te ajudar.")
                print("Meus parabens, voce foi salvo!!!\nAs vezes mais uns minutos de sofrimento valem a pena.")
            elif (escolha == "aceitar"):
                print("\n.....\n")
                print("Voce se senta apoiado numa arvore proxima, fecha os olhos e apenas se deixa levar.")
                print("Voce perdeu....\nApos alguns segundos voce nao escuta mais nada e so se sente em paz....")
                quit()
            else:
                print("Escolha invalida!\nVoce perdeu!!")
                quit()
        elif (escolha == "continuar"):
            print("\n......\n")
            print("Depois de caminhar por mais algumas horas a noite chega e fica dificil de voce andar pela floresta no meio da escuridao")
            print("Voce nao consegue ver direito por onde anda e acaba tropecando em algumas raizes e caindo mais de uma vez.")
            print("Voce sente que chegou numa rua e fica tao feliz com isso que voce se ajoelha no meio da rua")
            print("Um carro vem vindo em sua direcao, mas a rua nao tem iluminacao nenhuma alem dos farois do carro se aproximando")
            print("Sem voce ter tempo de reagir e o motorista nao vendo voce ele acaba te atropelando...")
            print("Voce perdeu!!\nQue jeito triste de perder... Ajoelhado no que seria a sua salvacao...")
        else:
            print("Escolha invalida!\nVoce perdeu!!")
            quit()
    else:
        print("Escolha invalida!\nVoce perdeu!!")
        quit()
else:
    print("Escolha invalida!\nVoce perdeu!!")
    quit()

