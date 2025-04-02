import io
from flask import Flask, render_template, jsonify, request 
import matplotlib.pyplot as plt 
import base64
from database import obtener_datos, guardar_dato
import sensor  # Inicia el sensor en segundo plano

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal con datos y gráfica"""
    datos = obtener_datos(10)
    temperaturas, tiempos = zip(*datos) if datos else ([], [])
    
    # Generar gráfica
    plt.figure(figsize=(8, 4))
    plt.plot(tiempos, temperaturas, marker='o', linestyle='-', color='b')
    plt.xticks(rotation=45)
    plt.xlabel("Hora")
    plt.ylabel("Temperatura (°C)")
    plt.title("Últimas lecturas del sensor")
    plt.grid(True)
    
    # Convertir a imagen
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    grafico_base64 = base64.b64encode(img.getvalue()).decode()

    return render_template("index.html", datos=datos, grafico_base64=grafico_base64)

@app.route('/datos', methods=['GET'])
def api_datos():
    """Devuelve las lecturas en formato JSON"""
    return jsonify(obtener_datos(10))

@app.route('/agregar', methods=['POST'])
def agregar_dato():
    """Agrega una lectura manualmente"""
    temperatura = request.json.get('temperatura')
    if temperatura is not None:
        guardar_dato(temperatura)
        return jsonify({"mensaje": "Dato guardado"}), 201
    return jsonify({"error": "Temperatura requerida"}), 400

if __name__ == '__main__':
    app.run(debug=True)
