# Faça um programa em python qe receba o consumo de uma residência em m³, calcula 
# e mostra o valor da conta de água daquela residência.

n = int(input("Consumo em metros cúbidos: "))
if n <= 10:
    conta = 7
elif n>= 11 and n <= 30:
    conta = (n-10) * 1 + 7
elif n>=31 and n <=100:
    conta = (n-30) * 2 + 27
else:
    conta = (n-100) * 5 + 167

print(f"valor da conta = {conta}")

