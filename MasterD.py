import tkinter as tk

app = tk.Tk()

app.geometry("600x600")
app.configure(background="white")
tk.Wm.wm_title(app, "Armario")
"""
tk.Label(
    app,
    text="Hola Mundo",
    bg="light blue",
    fg="black",
    justify="center",
    ).pack(
        fill=tk.BOTH,
        expand=True)
"""
def saludar():
    print("Hola mundo")

def saludarpene():
    print("Comeme el coño")


tk.Button(app,
        text="Pulsa aqui",
        font=("Arial", 14),
        bg="purple",
        fg="white",
        command=saludar
        ).pack(
        fill=tk.BOTH,
        expand=True
)
tk.Button(app,
        text="Mejor Pulsa aqui",
        font=("Arial", 14),
        bg="dark blue",
        fg="white",
        command=saludarpene
        ).pack(
        fill=tk.BOTH,
        expand=True
)




app.mainloop()