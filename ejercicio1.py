Temperaturas1 = [27.1, 22.3, 26.8, 23.5, 22.7, 15.3, 26.6, 16.9, 
            18.1, 24.7, 23.8, 18.4, 26.1, 27.5, 27.3, 21.9, 25.4, 
            25.1, 20.4, 16.2, 27.5, 22.7, 25.9, 21.2]

Temperaturas2 = [25.4, 21.5, 27.3, 25.5, 20.2, 26.6, 16.1, 27.7,
                26.4, 24.0, 22.6, 19.4, 27.0, 18.3, 25.0, 24.3,
                25.6, 27.1, 15.6, 27.1, 26.6, 22.7, 20.4, 23.3]

Temperaturas3 = [16.4, 20.5, 23.5, 17.3, 26.2, 26.2, 22.9, 21.2,
                24.2, 26.0, 18.7, 27.5, 25.0, 22.7, 21.7, 22.7,
                23.3, 25.0, 26.7, 18.7, 19.6, 23.9, 20.0, 17.2]

def analizar_temp(temp):
    lista_valores = []
    lista_valores.append(round(sum(temp) / len(temp), 3))
    lista_valores.append(min(temp))
    lista_valores.append(max(temp))
    
    conteo = 0
    for t in temp:
        if t <= 22:
            conteo += 1
    lista_valores.append(conteo)

    return lista_valores

"""
def legible_operario(temp):
    lista_valores = []
    lista_valores.append(round(sum(temp) / len(temp), 3))
    lista_valores.append(min(temp))
    lista_valores.append(max(temp))
    
    conteo = 0
    for t in temp:
        if t <= 22:
            conteo += 1
    lista_valores.append(conteo)
    print(f"La temperatura media de los sensores es de: {lista_valores[0]}")
    print(f"La temperatura minima de los sensores es de: {lista_valores[1]}")
    print(f"La temperatura maxima de los sensores es de: {lista_valores[2]}")
    print(f"El numero de sensores que superaron los 22 grados son: {lista_valores[3]}")

No se si se esperaba que hiciera una función que recogiera la función 1 
o que recogiera directamente la lista. aquí dejo comentada la segunda.
"""
def legible_operario(Lint_valor):
    print(f"La temperatura media de los sensores es de: {Lint_valor[0]}")
    print(f"La temperatura minima de los sensores es de: {Lint_valor[1]}")
    print(f"La temperatura maxima de los sensores es de: {Lint_valor[2]}")
    print(f"El numero de sensores que superaron los 22 grados son: {Lint_valor[3]}")

legible_operario(Temperaturas1)
legible_operario(Temperaturas2)
legible_operario(Temperaturas3)