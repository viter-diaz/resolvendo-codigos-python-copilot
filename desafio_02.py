# Desafio 02 - Calculadora simples

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print(a + b)
elif operacao == "-":
    print(a - b)
elif operacao == "*":
    print(a * b)
elif operacao == "/":
    if b != 0:
        print(a / b)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")