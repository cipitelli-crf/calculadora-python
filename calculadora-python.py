
# Função para somar dois números
def somar(a, b):
    return a + b

# Função principal que solicita ao usuário dois números e chama a função de soma
def main():
    print("Calculadora Simples")
    
    while True:  # Laço infinito para continuar pedindo cálculos
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            resultado = somar(num1, num2)
            print(f"O resultado da soma de {num1} + {num2} é: {resultado}")
        
        except ValueError:
            print("Por favor, digite apenas números válidos.")
        
        # Pergunta ao usuário se ele deseja fazer outro cálculo
        continuar = input("Deseja fazer outra soma? (s/n): ").strip().lower()
        
        if continuar != 's':
            print("Obrigado por usar a calculadora!")
            break  # Sai do laço se o usuário não quiser continuar

# Chamando a função principal
if __name__ == "__main__":
    main()
