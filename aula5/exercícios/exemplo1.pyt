# Faça um programa que solicita ao usuário um número e mostra os próximos 5 números 
# a partir do número digitado.

from tkinter import N


numeroUsuario = int(input("Digite um número:"))
ct = 0
x = numeroUsuario
while ct <5:
    x = x +1
    print (x, end = '')
    ct = ct +1
    
