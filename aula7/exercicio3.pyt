# Escreva uma função que retorne o maior de dois números.
# Valores esperados:
# maximo(5,6) = 6
# maximo (2,1) = 2
# maximo (7,7) = 7

from tkinter import N


def maximo (n1, n2):
    if n1 > n2:
        return n1
    return n2
def entrada ():
    n = int(input("Digite um número:"))
    return n
def main():
    x = entrada()
    y = entrada()
    print(maximo(x, y))

main()
