import socket
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS

# Servidor UDP
def servidor_udp():
    # Configuración del servidor 
    DIRECCION_IP = "0.0.0.0"
    PUERTO_UDP = 5000

    # Crear socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Permitir reutilización de dirección/puerto (evita errores al reiniciar)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        udp_socket.bind((DIRECCION_IP, PUERTO_UDP))
    except OSError as e:
        print(f"Error al enlazar el socket: {e}")
        return

    print("Servidor esperando llamados...")

    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)
            print(f"Llamado recibido desde {addr}: {data.decode().strip()}")
        except Exception as e:
            print(f"Error al recibir datos: {e}")

# Servidor Flask (HTTP)
app = Flask(__name__)
CORS(app)  # Permite solicitudes desde la página web

@app.route("/orden", methods=["POST"])  # Endpoint y tipo de método POST (el cliente envía información al servidor)
def recibir_orden(): # Función que se ejecuta cuando el cliente se conecta con el endpoint
    datos = request.json
    mesa = datos.get("mesa")
    comida = datos.get("comida")

    if not mesa or not comida:
        return jsonify({"error": "Datos inválidos"}), 400

    print(f"Orden recibida: Mesa {mesa}, Pedido: {comida}")
    return jsonify({"mensaje": "Orden recibida", "mesa": mesa, "comida": comida})

# Ejecutar servidores
if __name__ == "__main__":
    # Iniciar el servidor UDP en un hilo separado
    hilo_udp = threading.Thread(target=servidor_udp, daemon=True)
    hilo_udp.start()

    # Iniciar el servidor Flask (HTTP) en el hilo principal
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
