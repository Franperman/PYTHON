
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class ProductViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Productos JSON")
        self.root.geometry("700x400")

        # Crear un Treeview para mostrar los productos en una tabla
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(expand=True, fill='both')

        # Definir las columnas
        self.tree['columns'] = ('ID', 'Nombre', 'Descripción', 'Precio')

        # Formatear las columnas
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=80)
        self.tree.column('Nombre', anchor=tk.W, width=120)
        self.tree.column('Descripción', anchor=tk.W, width=300)
        self.tree.column('Precio', anchor=tk.CENTER, width=100)

        # Definir encabezados
        self.tree.heading('#0', text='', anchor=tk.W)
        self.tree.heading('ID', text='ID', anchor=tk.CENTER)
        self.tree.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tree.heading('Descripción', text='Descripción', anchor=tk.W)
        self.tree.heading('Precio', text='Precio', anchor=tk.CENTER)

        # Cargar contenido del archivo JSON al iniciar
        self.cargar_productos()

    def cargar_productos(self):
        """Carga el contenido del archivo productos.json y lo muestra en el Treeview."""
        file_path = "C:/Users/Fanper/Documents/PYTHON/Proyectos_IA/trabajar_con_IA/lector_ficheros_json/productos.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    productos = json.load(file)
                    # Limpiar el Treeview
                    for item in self.tree.get_children():
                        self.tree.delete(item)
                    # Insertar productos en el Treeview
                    for producto in productos:
                        self.tree.insert('', tk.END, values=(producto['ID'], producto['Nombre'], producto['Descripcion'], producto['Precio']))
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo JSON: {e}")
        else:
            messagebox.showwarning("Archivo no encontrado", "El archivo 'productos.json' no se encontró.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductViewerApp(root)
    root.mainloop()
