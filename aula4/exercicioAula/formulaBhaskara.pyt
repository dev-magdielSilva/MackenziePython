import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 -4 * c * c
raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

print("A primeira raiz é:", raiz1)
print("A segunda raiz é:", raiz2)
