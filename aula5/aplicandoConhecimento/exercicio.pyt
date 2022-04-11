# Faça um programa em Python que solicite a quantidade de alunos de uma turma.
# Após esta informação, o usuário deve digitar a médica de cada aluno da turma, e o programa apresentará
# a mensagem, PARABÉNS VOCÊ ESTÁ APROVADO aos alunos com médio maior ou igual a 6.0
# O programa deve calcular e mostrar, no final da entrada de dados, a média geral da turma.
# obs: Casa a quantidade informada de alunos da turma for igual a zero, o programa deve emitir a mensagem: NÃO HOUVE PROCESSAMENTO.

soma = 0.0
ct = 0

quantidadeAlunosTurma = int(input())
if quantidadeAlunosTurma == 0:
        print("NÃO HOUVE PROCESSAMENTO")

while ct < quantidadeAlunosTurma:   
    media = float(input())
    soma = soma + media
    ct = ct + 1
    if media >= 6.0:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    totalMedia = soma / quantidadeAlunosTurma
    
if quantidadeAlunosTurma > 0:
        print(totalMedia)