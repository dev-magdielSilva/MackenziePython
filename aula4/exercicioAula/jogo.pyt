# Jogo par ou impar

import random
escolha = input("Par ou impar?")
apostaJ = int(input("Quandos dedos você vai lançar?"))
apostaC = random.randint(0,10)
print("Computador:", apostaC)
soma = apostaC + apostaJ
if soma % 2 == 0 and escolha == "par":
    print("Você ganhou")
elif soma % 2 !=0 and escolha == "impar":
    print("Você ganhou!")
else:
    print("Você perdeu!")