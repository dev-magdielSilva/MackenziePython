from re import X


# vetor = [0]*10 cria umalista preenchida com 10 zeros
# vetor[0] = 3 coloca o valor 3 na posição 0 da lista
# vator = [3,0,0,0,0,0,0,0,0,0,0]
#  lista = [] cria uma lista vazia
#  lista = [0,1,2,3]
#  lista.insert(1,"dois")
# [0,'dois', 1,2,3]


lista = []
def quantidade():
    x = int(input('Quantidade de números:'))
    return x 
def entrada(x):
    for i in range(x):
        num = int(input('Numeros:'))
        lista.append(num)
def saida():
    for i in range(len(lista)):
        print('Valos:', lista[i])
def main():
    x = quantidade()
    entrada(x)
    print(lista)
main()
