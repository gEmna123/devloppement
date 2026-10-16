
from flask import Flask, jsonify, request

# Créer l'application Flask
app = Flask(__name__)

# Une liste d'étudiants
students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
]

# Racine de l'API pour tester si le serveur fonctionne
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

# Lancer le serveur sur toutes les interfaces réseau
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
