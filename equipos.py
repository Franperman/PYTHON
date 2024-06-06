import math as ma
import time

class Tanque:
    def __init__(self, lista_vacia=[], valvulas=[], diametro=1.0, altura=1.0):
        self.diametro = diametro 
        self.altura = altura
        self.valvulas = valvulas
        self.lista_vacia = lista_vacia
    
        self.nivelActual = 1  # Inicializamos nivelActual a 1 (esto puede variar según la lógica de tu aplicación)
        self.caudal = 0
        self.volumenActual = 1  # Inicializamos volumenActual a 1 (esto puede variar según la lógica de tu aplicación)
        
    def calcularNivel(self):
        # Calcula el nivel actual del tanque en metros cúbicos y lo muestra en la consola
        volumen = (self.altura * ma.pi * (self.diametro/2)**2) / 1000
        print(f"Nivel actual del tanque: {volumen} metros cúbicos")
        
    def update(self, tiempo=1):
        # Actualiza el estado del tanque
        # Calcula el nivel actual del tanque en función del volumen actual
        self.nivelActual = self.altura - round(self.volumenActual / (ma.pi * (self.diametro / 2) ** 2), 2)
        
        # Calcula el caudal total sumando el caudal actual de todas las válvulas
        caudal_total = sum(valvula.caudalActual for valvula in self.valvulas)
        
        # Calcula el volumen que entra al tanque en función del caudal total y el tiempo
        volumen_entrado = caudal_total * tiempo
        
        # Actualiza el volumen actual del tanque sumándole el volumen entrante y asegurándose de que esté dentro de los límites
        volumen_maximo = self.altura * ma.pi * (self.diametro / 2) ** 2 * 1000
        self.volumenActual = max(0, min(self.volumenActual + volumen_entrado, volumen_maximo))
        
        # Muestra el nivel y volumen actual en la consola
        print(f"el tanque tiene un nivel de {self.nivelActual} cm")
        print(f"Volumen actual: {self.volumenActual} litros")
        
    def cargarTanque(self):
        # Llena el tanque abriendo las válvulas de entrada y cerrando las de salida
        self.caudal = 0
        print("LLenado tanque")
        for valvula in self.valvulas:
            if valvula.tipo == "E":
                valvula.abrirValvula()
                self.caudal = valvula.abrirValvula() + self.caudal
            elif valvula.tipo == "S":
                valvula.cerrarValvula()
                self.caudal = valvula.cerrarValvula() + self.caudal
        print(f"Caudal llenando tanque {self.caudal}")
        
    def vaciarTanque(self):
        # Vacia el tanque cerrando las válvulas de entrada y abriendo las de salida
        self.caudal = 0
        print("Vaciando tanque")
        for valvula in self.valvulas:
            if valvula.tipo == "E":
                valvula.cerrarValvula()
                self.caudal = valvula.cerrarValvula() + self.caudal
            elif valvula.tipo == "S":
                valvula.abrirValvula()
                self.caudal = valvula.abrirValvula() + self.caudal
        print(f"Caudal vaciando tanque {self.caudal}")

class Valvula:
    def __init__(self, tipo="E", caudal=1.0):
        self.tipo = tipo
        self.caudal = caudal
        
        self.caudalActual = 0
        
    def abrirValvula(self):
        # Abre la válvula y establece el caudal actual
        if self.tipo == "E":
            self.caudalActual = self.caudal
            return self.caudalActual
        elif self.tipo == "S":
            self.caudalActual = -self.caudal
            return self.caudalActual
        
    def cerrarValvula(self):
        # Cierra la válvula y establece el caudal actual en 0
        self.caudalActual = 0
        return self.caudalActual


v1 = Valvula("E", 15)
v2 = Valvula("S", 20)
v3 = Valvula("S", 25)
v4 = Valvula("E", 15)

residuos = Tanque(valvulas=[v1, v2, v3, v4], diametro=8.0, altura=80.0)

residuos.volumenActual = 100

residuos.calcularNivel()
residuos.vaciarTanque()

tres = 0
while tres != 5:
    residuos.update(0.5)
    time.sleep(1)
    tres += 1

residuos.cargarTanque()

tres = 0
while tres != 5:
    residuos.update(0.5)
    time.sleep(1)
    tres += 1

v1.cerrarValvula()
v2.cerrarValvula()
v3.cerrarValvula()
v4.cerrarValvula()
print("-------")
tres = 0
while tres != 5:
    residuos.update(0.5)
    time.sleep(1)
    tres += 1