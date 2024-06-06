import time

class Tanque:
    def __init__(self, capacidad):
        # Inicializa el tanque con la capacidad dada
        self.capacidad = capacidad
        
        # Inicializa la carga actual y el caudal a cero
        self.cargaActual = 0
        self.caudal = 0
        
    def cargar(self):
        # Establece el caudal de carga a 20
        self.caudal = 20
        
    def vaciar(self):
        # Establece el caudal de vaciado a -20
        self.caudal = -20
        
    def cerrarValvulas(self):
        # Cierra las válvulas, estableciendo el caudal a cero
        self.caudal = 0
        
    def update(self):
        # Actualiza la carga actual del tanque según el caudal, 
        # asegurándose de no sobrepasar la capacidad ni ir por debajo de cero
        if 0 <= self.cargaActual < self.capacidad:
            self.cargaActual += self.caudal

# Crea una instancia del tanque con una capacidad de 2000 litros
tk1 = Tanque(2000)

# Inicia el proceso de carga del tanque
tk1.cargar()

# Bucle infinito para actualizar el estado del tanque periódicamente
while True:
    # Actualiza el estado del tanque
    tk1.update()
    
    # Imprime el total de carga actual del tanque
    print(f"Total cargado: {tk1.cargaActual} litros")
    
    # Si la carga actual alcanza o supera los 200 litros, inicia el vaciado del tanque
    if tk1.cargaActual >= 200:
        tk1.vaciar()
    
    # Espera 0.5 segundos antes de la siguiente actualización
    time.sleep(0.5)
