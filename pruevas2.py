# Definición de la clase Motor
class Motor:
    # Variable de clase para el tipo de motor
    tipo_motor = "electrico"
    
    # Constructor de la clase Motor
    def __init__(self, potencia, voltaje, fabricante, vel_max):
        # Inicialización de las propiedades del motor
        self.vel_max = vel_max  # Velocidad máxima del motor
        self.potencia = potencia  # Potencia del motor
        self.voltaje = voltaje  # Voltaje de operación del motor
        self.fabricante = fabricante  # Fabricante del motor
        
        self.velocidad = 0  # Velocidad inicial del motor
        self.estado = False  # Estado inicial del motor (False = parado)
        self.caracteristicas = "trifasico"  # Características del motor (ejemplo: trifásico)
        
    # Método para variar la velocidad del motor
    def variar(self, porcentaje):
        # Limitar porcentaje a un máximo de 100
        if porcentaje > 100:
            porcentaje = 100  
        # Limitar porcentaje a un mínimo de 0
        elif porcentaje < 0:
            porcentaje = 0  
        # Calcular y actualizar la velocidad basada en el porcentaje
        if self.vel_max == None:
            return None
        self.velocidad = int(round((self.vel_max / 100) * porcentaje, 0))
        
    # Método para arrancar el motor
    def arrancar(self, porcentaje=100):
        # Limitar porcentaje a un máximo de 100
        if porcentaje > 100:
            porcentaje = 100  
        # Limitar porcentaje a un mínimo de 0
        elif porcentaje < 0:
            porcentaje = 0  
        
        # Calcular y actualizar la velocidad basada en el porcentaje
        if self.vel_max == None:
            print("el servo esta con tension")
        else:
            self.velocidad = int(round((self.vel_max / 100) * porcentaje, 0))
            print("el motor esta arrancado")  # Mensaje indicando que el motor está arrancado
            
        self.estado = True  # Cambiar el estado del motor a True (arrancado)
        return self.estado  # Devolver el estado actual del motor
        
    # Método para parar el motor
    def parar(self):
        # Establecer la velocidad a 0
        self.velocidad = 0  
        print("el motor esta parado")  # Mensaje indicando que el motor está parado
        self.estado = False  # Cambiar el estado del motor a False (parado)
        return self.estado  # Devolver el estado actual del motor

# Definición de la clase Servo que hereda de Motor
class Servo(Motor):
    # Constructor de la clase Servo
    def __init__(self, potencia, voltaje, fabricante):
        # Inicialización de las propiedades del servo usando el constructor de la clase base (Motor)
        super().__init__(potencia, voltaje, fabricante, vel_max=None)
        self.posicion = 0  # Posición inicial del servo

# Definición de la clase GuardaMotor
class GuardaMotor:
    # Constructor de la clase GuardaMotor
    def __init__(self, estado, motor_a_proteger:Motor):
        self.estado = estado  # Estado de la protección (True = activada, False = desactivada)
        self.motor_a_proteger = motor_a_proteger  # Motor que se protegerá
        
    # Método para activar la protección del motor
    def activar_proteccion(self):
        self.estado = True  # Establecer el estado de la protección como activada
        self.motor_a_proteger.parar()  # Parar el motor protegido
        
    # Método para desactivar la protección del motor
    def desactivar_proteccion(self):
        self.estado = False  # Establecer el estado de la protección como desactivada

# Crear instancias de la clase Motor
motorCinta = Motor(0.5, 220, "siemens", 8000)  # Motor de cinta transportadora
motorMixer = Motor(10, 380, "sew", 800)  # Motor de mezclador
brazo_posicionado = Servo(5, 380, "sew") # Crear una instancia de la clase Servo

# Arrancar el motorMixer con un porcentaje de -25 (se ajustará a 0)
motorMixer.arrancar(-25)
print(motorMixer.velocidad)  # Imprimir la velocidad actual del motorMixer

# Variar la velocidad del motorMixer a 3000 (se ajustará a 100)
motorMixer.variar(3000)
print(motorMixer.velocidad)  # Imprimir la velocidad actual del motorMixer

# Parar el motorMixer
motorMixer.parar()
print(motorMixer.velocidad)  # Imprimir la velocidad actual del motorMixer

# Establecer la posición del servo
brazo_posicionado.posicion = 50

print(brazo_posicionado.posicion)  # Imprimir la posición actual del servo
brazo_posicionado.arrancar()

# Crear instancia de la clase GuardaMotor y activar la protección
q1 = GuardaMotor(False ,motorMixer)

q1.activar_proteccion()
