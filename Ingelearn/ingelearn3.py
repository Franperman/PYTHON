from pymodbus.client import ModbusTcpClient as mb
import time

cliente = mb("127.0.0.1")
cliente.connect()

cant_reg = 1
dispositivo = 1
nivel = 0
valvula = 5


cliente.write_register(valvula, 1000, dispositivo)
lectura_valvula = cliente.read_holding_registers(valvula, cant_reg, dispositivo)
print(lectura_valvula.registers[0])

try:
    while True:
        lectura = cliente.read_holding_registers(nivel, cant_reg, dispositivo)
        print(lectura.registers[0])
        time.sleep(2)
except KeyboardInterrupt:
    print("se acabo")