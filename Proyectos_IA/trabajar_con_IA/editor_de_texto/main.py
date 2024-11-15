import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
import os

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto con Tkinter")
        self.root.geometry("600x400")

        # Barra de menú
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menú de archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Guardar Como", command=self.guardar_como)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        # Menú de edición
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cortar", command=self.cortar_texto)
        self.edit_menu.add_command(label="Copiar", command=self.copiar_texto)
        self.edit_menu.add_command(label="Pegar", command=self.pegar_texto)
        self.menu_bar.add_cascade(label="Edición", menu=self.edit_menu)

        # Área de texto
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Ruta del archivo abierto
        self.ruta_archivo = None

    def abrir_archivo(self):
        """Abre un archivo de texto y carga su contenido en el área de texto."""
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    contenido = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.INSERT, contenido)
                    self.ruta_archivo = file_path
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    def guardar_archivo(self):
        """Guarda el contenido del área de texto en un archivo."""
        if self.ruta_archivo:
            try:
                with open(self.ruta_archivo, "w", encoding="utf-8") as file:
                    contenido = self.text_area.get(1.0, tk.END)
                    file.write(contenido.strip())
                    messagebox.showinfo("Guardar Archivo", "Archivo guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            self.guardar_como()

    def guardar_como(self):
        """Guarda el contenido del área de texto en un nuevo archivo."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    contenido = self.text_area.get(1.0, tk.END)
                    file.write(contenido.strip())
                    self.ruta_archivo = file_path
                    messagebox.showinfo("Guardar Archivo", "Archivo guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def cortar_texto(self):
        """Corta el texto seleccionado al portapapeles."""
        self.text_area.event_generate("<<Cut>>")

    def copiar_texto(self):
        """Copia el texto seleccionado al portapapeles."""
        self.text_area.event_generate("<<Copy>>")

    def pegar_texto(self):
        """Pega el texto del portapapeles en el área de texto."""
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
