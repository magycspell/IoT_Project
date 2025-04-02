import sqlite3

DB_NAME = "sensor.db"

def crear_base_datos():
    """Crea la base de datos y la tabla si no existen"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def guardar_dato(temperatura):
    """Guarda una lectura en la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lecturas (temperatura) VALUES (?)", (temperatura,))
    conn.commit()
    conn.close()

def obtener_datos(limit=10):
    """Obtiene las últimas lecturas"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT temperatura, timestamp FROM lecturas ORDER BY timestamp DESC LIMIT ?", (limit,))
    datos = cursor.fetchall()
    conn.close()
    return datos

# Ejecutar al inicio para crear la base
crear_base_datos()
