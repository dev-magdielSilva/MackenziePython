# Este programa em Python recebe 5 números inteiros digitados pelo 
# Usuário e, no final, apresenta a soma destes números.

soma = 0
print("Digite 5 números:")
for ct in range (0,5,1):
    num = int(input("Número:"))
    soma += num
print("Soma = ", soma)

