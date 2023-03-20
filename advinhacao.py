import random


def Jogar():
    print("-------------------------------")
    print("Bem vindo no jogo de Advinhação")
    print("-------------------------------")

    numero_secreto = random.randrange(1, 101)
    tentativas_total = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")
    nivel = int(input("Defina a Dificuldade:"))

    if (nivel == 1):
        tentativas_total = 20
    elif (nivel == 2):
        tentativas_total = 10
    else:
        tentativas_total = 5

    # tentativa_atual = 1
    # while (tentativa_atual <= tentativas_total):
    for tentativa_atual in range(1, tentativas_total + 1):
        print("Tentativas: {}/{}".format(tentativa_atual, tentativas_total))
        chute = int(input("Digite o seu número entre 1 e 100:"))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve chutar números entre 1 e 100")
            continue

        chute_acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (chute_acertou):
            print("Você Acertou!")
            break
        else:
            if (chute_maior):
                print("Você Errou!, O seu Chute foi maior que o número secreto")
            elif (chute_menor):
                print("Você Errou!, O seu Chute foi menor que o número secreto")
        # tentativa_atual += 1

    print("Resposta: ", numero_secreto)
    print("Fim do Jogo!")


if (__name__ == "__main__"):
    Jogar()
