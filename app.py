import os
from flask import Flask, jsonify

app = Flask(__name__)

TICKETS = [
    {"id": 1, "titre": "Imprimante en panne", "statut": "ouvert"},
    {"id": 2, "titre": "Mot de passe oublié", "statut": "en cours"},
    {"id": 3, "titre": "Installation de Docker", "statut": "résolu"},
]


@app.get("/health")
def health():
    return jsonify(status="ko"), 500


@app.get("/version")
def version():
    return jsonify(version=os.getenv("APP_VERSION", "dev"))


@app.get("/tickets")
def tickets():
    return jsonify(TICKETS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)