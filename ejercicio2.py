def escalarValores(analogico):
    escalado = round((analogico / 32767) * 100, 3)
    print(escalado)

t = 0
while t != 5:
    escalarValores(float(input()))
    t += 1

productos_stock = {'producto1': 15, 'producto2': 7, 'producto3': 11, 'producto4': 5}


for produt, repo in productos_stock.items():
    if repo < 10:
        print(f"Por favor señor operario, seria tan amable de reponer este {produt}, que esta por debajo de su reposición \n tiene actualmente {repo} unidades \n")


temperaturas = [28, 29, 31, 27, 33, 29, 30, 31, 32, 28]

temperaturas_anormales = [t for t in temperaturas if t > 30]

print(f"Tenemos {len(temperaturas_anormales)} temperaturas que superan los 30 grados que son {temperaturas_anormales}")