import forca
import advinhacao

print("-------------------------------")
print("       Escolha o seu jogo      ")
print("-------------------------------")

print("(1) Forca")
print("(2) Advinhação")

jogo = int(input("Qual jogo?"))
if (jogo == 1):
    forca.Jogar()
elif (jogo == 2):
    advinhacao.Jogar()
