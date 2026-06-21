# Desafio 03 - Calculadora de Média da Turma

quantidade = int(input("Quantos alunos deseja cadastrar? "))

soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma += nota

media = soma / quantidade

print(f"\nMédia da turma: {media:.2f}")

if media >= 7:
    print("Turma aprovada!")
else:
    print("Turma em recuperação.")