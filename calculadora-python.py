# Funções para realizar as operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não permitida"

# Função principal que solicita ao usuário escolher a operação e dois números
def main():
    print("Calculadora Simples")

    while True:  # Laço infinito para continuar pedindo cálculos
        # Exibe o menu de operações
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        try:
            operacao = int(input("Digite o número da operação desejada: "))
            
            if operacao == 5:
                print("Obrigado por usar a calculadora!")
                break  # Sai do laço se o usuário escolher sair

            # Solicita os números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Realiza a operação escolhida
            if operacao == 1:
                resultado = somar(num1, num2)
            elif operacao == 2:
                resultado = subtrair(num1, num2)
            elif operacao == 3:
                resultado = multiplicar(num1, num2)
            elif operacao == 4:
                resultado = dividir(num1, num2)
            else:
                print("Opção inválida! Tente novamente.")
                continue  # Se a opção for inválida, repete o laço

            # Exibe o resultado
            print(f"O resultado da operação é: {resultado}")
        
        except ValueError:
            print("Por favor, digite apenas números válidos.")
        

# Chamando a função principal
if __name__ == "__main__":
    main()

