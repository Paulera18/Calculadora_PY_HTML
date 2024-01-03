def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Encerrando a calculadora.")
            break

        if escolha in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite números válidos.")
                continue

            if escolha == '1':
                resultado = soma(num1, num2)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = divisao(num1, num2)

            print(f"Resultado: {resultado}")
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    calculadora()

