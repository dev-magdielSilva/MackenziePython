# Faça um programa que receba três notas de um aluno, calcule e mostre a média
# aritmética e a mensagem constrante na tabela a seguir. Aos alunos que ficaram para exame, 
# calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6

n1 = float (input("Insira a nota 1:"))
n2 = float (input("Insira a nota 2:"))
n3 = float (input("Insira a nota 3:"))

media = float (n1+n2+n3)/3
print ("Média = %.1f" %media)

if media>=0 and media<3:
    print("Reprovado")
elif media <7:
    print("Exame")
    print ("Você precisa tirar nota %.1f para se aprovado" %(12-media))
else:
    print("Aprovado")