numeros = [9, 5, 8, 7, 4, 1, 2, 9, 3, 6, 2, 5, 1, 8, 5, 6, 6, 7, 3, 4, 1, 2, 7, 4, 8, 5, 9, 6, 7, 8, 3, 4, 1, 2, 3]

print(len(numeros))

print(sorted(numeros))

print(sum(numeros))

pedo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in pedo:
    numeros.append(i)

numeros.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# numeros = set(numeros)

numeros = list(numeros)

for z in pedo:
    numeros.append(z)

numeros.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

numeros.append(99)

print(sorted(numeros))

ultimo = []

while len(numeros) != 0:
    t = numeros.pop()
    ultimo.append(t)

ultimo.remove(99)

print(sorted(ultimo))


cinta = ["vacio", "vacio", "vacio", "vacio", "vacio", "vacio", "vacio", "vacio", "caja", "vacio", "vacio", "vacio", "vacio", "vacio", "vacio"]

print("caja" in cinta)

