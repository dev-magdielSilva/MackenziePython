# Escreva ua função que receba o lado de um quadrado e retorne sua área
# Valores esperados:
# area_quadrado(4) = 16
# area_quadrado(9) = 81

def area_quadrado (lado):
    return lado ** 2
def entrada ():
    lado = float (input("Lado:"))
    return lado
def main():
    l = entrada()
    a = area_quadrado(l)
    print("Area = ", a)
main()
