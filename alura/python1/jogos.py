import forca
import adivinhacao

print("Escolha seu jogo: ")

jogo = int(input("1- adivinhacao \n2- forca"))

if(jogo == 1):
    print("jogando adivinhacao")
    forca.jogar()
elif(jogo == 2):
    print("jogando forca")
    adivinhacao.jogar()