caudal = 12.85

if caudal > 40.0:
    estado_tanque = "muy lleno"
elif caudal > 20.20:
    estado_tanque = "su puta madre"
else:
    estado_tanque = "le robo un gitano"

print(estado_tanque)

planetas = ["mercurio", "venus", "tierra", "marte", "Jupiter", "saturno", "Urano", "nepturno", "puuuuutooooooon"]

for planeta in planetas:
    print(planeta)

flipado = "caudalimetro"
print(flipado)
gran_rencor = []
for cafre in flipado:
    gran_rencor.append(cafre)
gran_rencor = list(set(gran_rencor))
gran_rencor.sort()
gran_rencor.reverse()
gran_rencor_str = ''.join(gran_rencor)
print(gran_rencor_str)

for muder in range(7):
    print(f"tengo ganas de canas { muder + 1} veces")

i = 0
while True:
    i += 1
    if (i % 2 == 1):
        continue
    print("dentro del bucle")
    print("repetición",i)
    if i >= 10:
        break
print("-------------")
print("fuera del puto bucle")

pares = []

for n in range(11):
    if n % 2 == 0:
        pares.append(n)

print(pares)

peres = [p for p in range(11) if(p % 2 == 1)]

print(peres)

sensores_de_temperatura = {"sala de producción": 25.5,
                    "oficina administrativas": 22.1,
                    "almacén principal": 18.7,
                    "area de carga y descarga": 27.8,
                    "laboratorio de control de calidad": 24.3,
                    "zona de empaque": 21.6,
                    "area de refrigeración": 15.9,
                    "sala de maquinas": 28.2,
                    "comedor de empleados": 20.5,
                    "pasillo de distribución": 23.8}

namer = [1, 6, -6, 45, -23, 12, -3, 5, 9]
negativos = [g for g in namer if g < 0]
print(negativos)

calefacciones = [sensor for sensor, temperatura in sensores_de_temperatura.items() if temperatura < 22.0]

for sensor, temperatura in sensores_de_temperatura.items():
    if temperatura < 22:
        print(sensor, temperatura)

print(calefacciones)

def pene(cacharro = 0, comillas = 2):
    excremento = cacharro + comillas - 65
    if excremento >= 566:
        return "no funciona"
    return excremento 

print(pene(comillas=45))