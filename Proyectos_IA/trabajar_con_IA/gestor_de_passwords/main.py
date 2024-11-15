import tkinter as tk
from tkinter import messagebox
import random
import string

# Esta función hace la contraseña
def generar_contraseña():
    try:
        # Tomamos el número que el usuario escribió
        longitud = int(entry_longitud.get())
        if longitud < 1:
            raise ValueError("La longitud debe ser mayor que 0")
    except ValueError as e:
        # Si el usuario escribió algo que no es un número, mostramos un error
        messagebox.showerror("Error", f"Entrada no válida: {e}")
        return

    # Aquí tenemos todas las letras, números y símbolos que podemos usar
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Elegimos al azar tantos caracteres como el número que el usuario escribió
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    # Borramos lo que había antes en la caja de texto de la contraseña
    entry_contraseña.delete(0, tk.END)
    # Ponemos la nueva contraseña en la caja de texto
    entry_contraseña.insert(0, contraseña)

# Funciones para el menú contextual
def copiar():
    root.clipboard_clear()
    root.clipboard_append(entry_contraseña.selection_get())

def cortar():
    copiar()
    entry_contraseña.delete("sel.first", "sel.last")

def pegar():
    try:
        texto = root.clipboard_get()
        entry_contraseña.insert(tk.INSERT, texto)
    except tk.TclError:
        pass

# Función para mostrar el menú contextual
def mostrar_menu(event):
    menu_contextual.post(event.x_root, event.y_root)

# Aquí hacemos la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")  # Le ponemos un título a la ventana

# Hacemos una etiqueta que dice "Longitud de la contraseña:"
label_longitud = tk.Label(root, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)  # La ponemos en la ventana con un poco de espacio

# Hacemos una caja de texto donde el usuario puede escribir un número
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)  # La ponemos en la ventana con un poco de espacio

# Hacemos un botón que dice "Generar Contraseña"
boton_generar = tk.Button(root, text="Generar Contraseña", command=generar_contraseña)
boton_generar.pack(pady=10)  # Lo ponemos en la ventana con un poco de espacio

# Hacemos una etiqueta que dice "Contraseña Generada:"
label_contraseña = tk.Label(root, text="Contraseña Generada:")
label_contraseña.pack(pady=5)  # La ponemos en la ventana con un poco de espacio

# Hacemos una caja de texto donde mostraremos la contraseña generada
entry_contraseña = tk.Entry(root, width=50)
entry_contraseña.pack(pady=5)  # La ponemos en la ventana con un poco de espacio

# Creamos el menú contextual
menu_contextual = tk.Menu(root, tearoff=0)
menu_contextual.add_command(label="Cortar", command=cortar)
menu_contextual.add_command(label="Copiar", command=copiar)
menu_contextual.add_command(label="Pegar", command=pegar)

# Añadimos el menú contextual al campo de entrada de la contraseña
entry_contraseña.bind("<Button-3>", mostrar_menu)

# Hacemos que la ventana se quede abierta y funcione
root.mainloop()
