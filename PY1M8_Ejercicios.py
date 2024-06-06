import threading
import time
import random
import os
import matplotlib.pyplot as plt
from queue import Queue

class Turbina:
    def __init__(self):
        self.pulsador_marcha = False
        self.pulsador_parada = False
        self.parada_emergencia1 = True
        self.parada_emergencia2 = True
        self.sensor_llama_quem1 = False
        self.sensor_llama_quem2 = False
        self.sensor_cierre_valvula_principal = True
        self.sensor_velocidad = 0.0
        
        self.comando_valvula = 0.0
        self.control_automatico = False
        self.comando_motor_arranque = False
        self.comando_junta_neumatica = False
        self.comando_accionamiento_chisperos1 = False
        self.comando_accionamiento_chisperos2 = False
        self.comando_accionamiento_quemador_emergencia = False
        self.comando_chispero_salida_emergencia = False
        self.comando_manual_auto = "MANUAL"
        self.comando_frenos = False
        
        self.etapa_parada = 0
        self.etapa_arranque = 0 
        self.running = True
        self.velocidades = []
        self.aperturas_valvula = []
        self.start_time = time.time()
        
        self.anteriores = []
        self.error_accu = []
        self.error = 0.0
        
        self.update_thread = threading.Thread(target=self.update)
        self.plot_thread = threading.Thread(target=self.plot_data)
        
        self.data_queue = Queue()
        self.update_thread.start()
        self.plot_thread.start()
    
    def update(self):
        while self.running:
            time.sleep(1)
            os.system('cls') 
            
            self.PID(mode_auto=self.comando_manual_auto, input=self.sensor_velocidad, Setpoint=4600) 
            if self.comando_accionamiento_chisperos1:
                self.sensor_llama_quem1 = True
            if self.comando_accionamiento_chisperos2:
                self.sensor_llama_quem2 = True
            
            elapsed_time = time.time() - self.start_time
            
            if elapsed_time >= 200:
                if self.sensor_velocidad <= 0:
                    self.sensor_velocidad = 0
                else:
                    self.sensor_velocidad += self.comando_valvula - (30 + random.uniform(0, 30))
                    self.stop_sequence(True)
            elif self.etapa_arranque == 4:
                self.sensor_velocidad += self.comando_valvula - (30 + random.uniform(0, 30))
                self.start_sequence(True)
            else:
                self.sensor_velocidad = min(6000, self.sensor_velocidad + random.uniform(20, 120))
                self.start_sequence(True)
            
            if self.comando_accionamiento_chisperos1:
                self.sensor_llama_quem1 = True
            if self.comando_accionamiento_chisperos2:
                self.sensor_llama_quem2 = True
                
            self.emergency_stop(True, True)

    def start_sequence(self, start=False):
        if self.emergency_stop(self.parada_emergencia1, self.parada_emergencia2):
            print(f"Etapa de arranque: {self.etapa_arranque}")
            print(f"Apertura de la valvula {self.comando_valvula}%")
            print(f"Velocidad de la turbina {self.sensor_velocidad}RPM")
            self.etapa_parada = 0
            self.pulsador_marcha = start
            if self.etapa_arranque == 0 and self.pulsador_marcha:
                self.comando_frenos = False
                print("Iniciando secuencia de arranque...")
                if self.sensor_cierre_valvula_principal:
                    self.pulsador_parada = False
                    self.comando_motor_arranque = True
                    self.comando_junta_neumatica = True
                    self.etapa_arranque += 1
            elif self.etapa_arranque == 1:
                if self.sensor_velocidad >= 478:
                    self.comando_motor_arranque = False
                    self.comando_accionamiento_chisperos1 = True
                    self.comando_accionamiento_chisperos2 = True
                    time.sleep(2)
                    self.comando_valvula = 10
                    self.etapa_arranque += 1
            elif self.etapa_arranque == 2:
                if self.sensor_llama_quem1 and self.sensor_llama_quem2:
                    self.comando_accionamiento_chisperos1 = False
                    self.comando_accionamiento_chisperos2 = False                
                    self.comando_valvula = 25
                    self.etapa_arranque += 1
            elif self.etapa_arranque == 3:
                if self.sensor_velocidad >= 2750:
                    self.comando_motor_arranque = False
                    self.comando_junta_neumatica = False
                    time.sleep(5)
                    self.comando_motor_arranque = False
                    self.etapa_arranque += 1
            elif self.etapa_arranque == 4:
                if self.sensor_velocidad >= 2750:
                    self.control_automatico = True
                    self.comando_manual_auto = "AUTO"

    def stop_sequence(self, stop=False):
        self.pulsador_parada = stop
        self.etapa_arranque = 0
        if self.pulsador_parada:
            if self.sensor_velocidad > 0:
                print("Iniciando secuencia de parada controlada...")
                print(f"Apertura de la valvula {self.comando_valvula}%")
                print(f"Velocidad de la turbina {self.sensor_velocidad}RPM")
                if self.etapa_parada == 0:
                    self.comando_manual_auto = "MANUAL"
                    self.pulsador_marcha = False
                    self.comando_valvula = 10
                    time.sleep(10)
                    self.comando_valvula = 0
                    self.etapa_parada += 1
                elif self.etapa_parada == 1:
                    if self.sensor_velocidad <= 2500:
                        self.comando_frenos = True
            else:
                print("Secuencia de parada controlada completada.")
    
    # Método para la parada de emergencia de la turbina
    def emergency_stop(self, emergency_stop1=True, emergency_stop2=True):
        self.parada_emergencia1 = emergency_stop1
        self.parada_emergencia2 = emergency_stop2
        # Comprobación de las condiciones de parada de emergencia
        if (self.sensor_velocidad > 5500 or not self.parada_emergencia1 or not self.parada_emergencia2 or 
            (self.etapa_arranque >= 2 and (not self.sensor_llama_quem1 or not self.sensor_llama_quem2))):
            self.pulsador_parada = False
            self.pulsador_marcha = False
            self.etapa_arranque = 0
            self.comando_valvula = 0.0
            self.sensor_velocidad = 0.0
            self.comando_accionamiento_quemador_emergencia = True
            self.comando_chispero_salida_emergencia = True
            self.comando_frenos = True
            self.running = False
            if not self.parada_emergencia1:
                print("¡Parada de emergencia 1 está activada!")
            if not self.parada_emergencia2:
                print("¡Parada de emergencia 2 está activada!")
            if not self.sensor_llama_quem1:
                print("Problemas en el quemador 1. Temperatura no alcanzada")
            if not self.sensor_llama_quem2:
                print("Problemas en el quemador 2. Temperatura no alcanzada")
            if self.sensor_velocidad > 5500:
                print("¡Parada por velocidad excesiva de la turbina!")
            return False
        else:
            return True
    
    def PID(self, mode_auto, input, Setpoint=0.0, kP=0.1, kI=0.0001, kD=1.0):
        if mode_auto == "AUTO":
            self.anteriores.append(round(input, 2))
            if len(self.anteriores) > 100:
                self.anteriores = self.anteriores[-100:]
            
            self.error = Setpoint - input
            self.error_accu  = [(Setpoint - elem) for elem in self.anteriores[-20:]]
            
            aP = self.error * kP
            aI = (kP * (sum(self.error_accu) / (len(self.error_accu) * 0.002) * kI))
            if len(self.anteriores) > 2:
                aD = (self.error_accu[-1] - self.error_accu[-2]) * kD * kP
            else:
                aD = 0.0
            
            Salida = self.comando_valvula + aP + aI + aD
            if Salida < 0:
                self.comando_valvula = 0
            elif Salida > 100:
                self.comando_valvula = 100         
            else:
                self.comando_valvula = Salida

    def plot_data(self):
        
        self.velocidades.append(self.sensor_velocidad)
        self.aperturas_valvula.append(self.comando_valvula * 10)
        
        self.data_queue.put((self.velocidades, self.aperturas_valvula))
        
        if len(self.velocidades) >= 70:
            self.velocidades.pop(0)  
        if len(self.aperturas_valvula) >= 70:
            self.aperturas_valvula.pop(0)
            
        if not self.data_queue.empty():
            plt.pause(1)
            plt.clf()
            plt.plot(self.velocidades, label='Velocidad de la turbina (RPM)', color='blue')
            plt.plot(self.aperturas_valvula, label='Apertura de la válvula escalada x 10 (%)', color='red')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Valor')
            plt.title('Dinámica de la turbina')
            plt.grid(True)
            plt.legend()
            
            
if __name__ == "__main__":
    turbina = Turbina()
    try:
        while True:
            turbina.plot_data()
            time.sleep(1)
    except KeyboardInterrupt:
        turbina.running = False
        print("Ejecución finalizada.")
