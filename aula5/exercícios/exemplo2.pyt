# Faça um programa que leia 5 números, apresentando, no final, a soma destes números.
soma = 0
ct = 0
print("Digite 5 números:")
while ct<5:
    num = int(input(""))
    soma += num
    ct += 1
print ("Soma =", soma)
