import tkinter as tk
from tkinter import messagebox

# Funções para as operações
def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

def subtrair():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero não permitida.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Configuração da interface
label_num1 = tk.Label(root, text="Primeiro número:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Segundo número:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Botões de operação
botao_somar = tk.Button(root, text="Somar", command=somar)
botao_somar.grid(row=2, column=0)

botao_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
botao_subtrair.grid(row=2, column=1)

botao_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
botao_multiplicar.grid(row=3, column=0)

botao_dividir = tk.Button(root, text="Dividir", command=dividir)
botao_dividir.grid(row=3, column=1)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar a interface
root.mainloop()

