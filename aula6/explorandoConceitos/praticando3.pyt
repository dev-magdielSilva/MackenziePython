# Escreva um programa em Python que calcule e apresente a soma das seguinte série:
#  SOMA = 1 + 3/2 + 5/3 + 7/4...90/50

s = 0
num = 1
for den in range(1, 51):
    s += num/den
    if den!=50:
        print(f"{num}/{den} + ", end = "")
    else:
        print(f"{num}/{den} = ", end = "")
    num += 2
print(s)