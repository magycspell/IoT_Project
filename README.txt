# Proyecto IoT: Integración y Visualización de Datos

Este proyecto simula un sensor que genera datos, los guarda en una base de datos y los muestra en una interfaz sencilla. 

¿Qué hace este proyecto?
- Simula un sensor que envía datos.
- Guarda la información en una base de datos.
- Muestra los datos en una página web de forma visual y fácil de entender.

Herramientas Utilizadas
- Python: El lenguaje de programación principal.
- Flask: Para crear la página web.
- SQLite: Para almacenar los datos.
- Matplotlib: Para generar gráficos.

Cómo Usarlo en Visual Studio Code (VSC)
Descarga y abre el proyecto
- Descarga el proyecto desde GitHub con este comando:
  git clone https://github.com/tuusuario/IoT_Project.git o descarga desde github
  
- Abre Visual Studio Code y selecciona la carpeta del proyecto.

### 2️ Configura el entorno
- Abre la terminal en VSC (`Ver > Terminal`).
- Escribe los siguientes comandos para preparar el entorno:
  python -m venv venv   # Crea un entorno virtual
  venv\Scripts\activate  # Activa el entorno en Windows
  source venv/bin/activate  # En macOS/Linux
- Instala las herramientas necesarias:
  pip install -r requirements.txt

### 3️ Ejecuta el proyecto
- Ejecutar el programa
  python app.py
- Abre tu navegador y ve a:
  http://127.0.0.1:5000/
### 4️ Cómo detenerlo
- Presiona `Ctrl + C` en la terminal.
- O usa `taskkill /F /IM python.exe` en Windows.

Mejoras Futuras
- Hacer que los datos se actualicen en tiempo real.
- Usar una base de datos más potente como PostgreSQL.
- Crear una versión para fácil instalación con Docker.

Desarrollado por Carlos Enrique Aguilar Maza
