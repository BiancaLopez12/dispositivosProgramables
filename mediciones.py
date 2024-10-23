import serial
import sqlite3
import time

# Configura la conexión con el puerto serie
puerto_serial = '/dev/ttyUSB0'  # Cambia esto al puerto correspondiente
baud_rate = 9600

# Conectar al puerto serie
ser = serial.Serial(puerto_serial, baud_rate)

# Conectar a la base de datos SQLite
conn = sqlite3.connect('mediciones.db')
cursor = conn.cursor()

# Leer y almacenar datos del sensor
try:
    while True:
        # Leer línea del puerto serie
        line = ser.readline().decode('utf-8').strip()
        
        # Supongamos que el valor del sensor está en la línea
        valor_sensor = int(line)

        # Insertar en la base de datos
        cursor.execute("INSERT INTO mediciones (valor_sensor) VALUES (?)", (valor_sensor,))
        conn.commit()
        
        print(f"Medición guardada: {valor_sensor}")

        # Espera 1 segundo antes de la próxima lectura
        time.sleep(1)

except KeyboardInterrupt:
    print("Terminando la lectura del sensor.")
finally:
    # Cerrar conexiones
    ser.close()
    conn.close()
