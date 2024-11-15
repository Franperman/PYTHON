import tkinter as tk
from tkinter import messagebox

def calcular_regla_de_tres():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        valor3 = float(entry3.get())
        resultado = (valor2 * valor3) / valor1
        resultado_label.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo valores numéricos.")

# Configurar la ventana principal
root = tk.Tk()
root.title("Calculadora de Regla de Tres")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Aumentar el tamaño de fuente para mejor accesibilidad
font_large = ("Helvetica", 16, "bold")
font_medium = ("Helvetica", 14)

# Título
titulo_label = tk.Label(root, text="Calculadora de Regla de Tres", font=font_large, bg="#f0f0f0")
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Etiquetas y entradas para los tres valores
label1 = tk.Label(root, text="Valor 1:", font=font_medium, bg="#f0f0f0")
label1.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(root, font=font_medium, width=10)
entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label2 = tk.Label(root, text="Valor 2:", font=font_medium, bg="#f0f0f0")
label2.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(root, font=font_medium, width=10)
entry2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

label3 = tk.Label(root, text="Valor 3:", font=font_medium, bg="#f0f0f0")
label3.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry3 = tk.Entry(root, font=font_medium, width=10)
entry3.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Botón para calcular
calcular_btn = tk.Button(root, text="Calcular", command=calcular_regla_de_tres, font=font_medium, bg="#4caf50", fg="white", width=10)
calcular_btn.grid(row=4, column=0, columnspan=2, pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado: ", font=font_medium, bg="#f0f0f0")
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
