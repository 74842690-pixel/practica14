from flask import Flask, jsonify, request
from procesador import contar_palabras, frecuencia_palabras, resumen

app = Flask(__name__)


@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Envía un objeto JSON válido"}), 400

    texto = data.get("texto")

    if not isinstance(texto, str) or not texto.strip():
        return jsonify({"error": "El campo 'texto' es obligatorio y no debe estar vacío"}), 400

    return jsonify({
        "palabras": contar_palabras(texto),
        "frecuencia": frecuencia_palabras(texto),
        "resumen": resumen(texto)
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
