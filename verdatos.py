import sqlite3

DB_NAME = "sensor.db"

def mostrar_datos():
    """Muestra los datos almacenados en la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturas ORDER BY timestamp DESC")
    datos = cursor.fetchall()
    conn.close()

    if datos:
        print("\n📊 Datos en la base de datos:\n")
        for fila in datos:
            print(f"ID: {fila[0]} | Temp: {fila[1]}°C | Timestamp: {fila[2]}")
    else:
        print("⚠️ No hay datos en la base de datos.")

if __name__ == "__main__":
    mostrar_datos()
