# Escreva uma função que receba dois números e retorne Ture se o primeiro número for múltiplo do segundo.
# Valores esperados:
# multiplo(8,4) = True
# multiplo(7,3) = False
# multiplo(5,5) = True







def multiplo(n1, n2):
    if n1%n2 == 0:
        return True
    return False

def entrada():
    n = int(input('Digite um número:'))
    return n 
def main():
    x = entrada()
    y = entrada()
    print (multiplo(x,y))

main()
