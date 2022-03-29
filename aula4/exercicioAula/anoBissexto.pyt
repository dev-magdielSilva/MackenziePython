# Faça um programa em Python que receba um valor referente ao ano e emita mensagem se
#  este ano é ou não bissexto.

# São bissextos todos os anos múltiplos de 400.
# São bissextos todos os multiplos de 4, exceto se for multiplo de 100 mas não de 400.

print("Insira o ano a ser analisado: ")
a = int(input())
if (a % 400 == 0) or (a % 4 == 0 and a %100 != 0):
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto")