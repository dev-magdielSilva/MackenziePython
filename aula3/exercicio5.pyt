# Escreva um programa que leia um número inteiro de 3 dígitos e
# imprima se o algarismo da dezena é par ou impar"

print("Digite um número inteiro de 3 dígitos")
num = int(input())
if num>999 or num<100:
    print("Número dora do intervalo solicitado.")
else:
    dezena=num%100//10
    if dezena%2==0:
        print("dezena par", dezena)
    else:
        print("dezena impar", dezena)
        
       