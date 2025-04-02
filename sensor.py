import random
import time
import threading
from database import guardar_dato

def simular_sensor():
    """Simula la lectura de un sensor de temperatura y la almacena en la base de datos"""
    while True:
        temperatura = round(random.uniform(20, 30), 2)
        guardar_dato(temperatura)
        print(f"[SENSOR] Temperatura registrada: {temperatura}°C")
        time.sleep(2)  # Genera un nuevo dato cada 2 segundos

# Iniciar el sensor en segundo plano
sensor_thread = threading.Thread(target=simular_sensor, daemon=True)
sensor_thread.start()
