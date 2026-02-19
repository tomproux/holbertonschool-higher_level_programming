#!/usr/bin/env python3

# Importation du framework Flask et des fonctions nécessaires
from flask import Flask
from flask import jsonify
from flask import request

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
# (clé = username, valeur = dictionnaire utilisateur)
users = {}

# Route principale de l'API ("/") qui retourne un message de bienvenue


@app.route('/')
def home():
    """Affiche un message de bienvenue à la racine de l'API."""
    return "Welcome to the Flask API!"

# Route "/data" qui retourne la liste des usernames enregistrés


@app.route('/data')
def data():
    """Retourne la liste des noms d'utilisateurs enregistrés."""
    return jsonify(list(users.keys()))

# Route "/status" qui permet de vérifier que l'API fonctionne correctement


@app.route('/status')
def status():
    """Retourne 'OK' pour vérifier que l'API fonctionne."""
    return "OK"

# Route dynamique "/users/<username>" pour accéder aux données d'un
# utilisateur spécifique


@app.route('/users/<username>')
def get_user(username):
    """Retourne les données d'un utilisateur donné, s'il existe."""
    # Vérifie si l'utilisateur existe dans le dictionnaire
    if username in users:
        return jsonify(users[username])
    else:
        # Si l'utilisateur n'existe pas, retourne une erreur
        return jsonify({"error": "User not found"}), 404

# Route "/add_user" pour ajouter un nouvel utilisateur via une requête POST


@app.route('/add_user', methods=['POST'])
def add_user():
    """Ajoute un utilisateur à partir de données JSON envoyées via POST."""
    # Récupère les données JSON envoyées par le client
    data = request.get_json()

    # Vérifie que la clé "username" est bien présente
    if "username" not in data:
        # Si elle est absente, retourne une erreur avec le code HTTP 400
        return jsonify({"error": "Username is required"}), 400

    # Récupère la valeur du champ "username"
    username = data["username"]
    # Ajoute l'utilisateur dans le dictionnaire, la clé étant le username
    users[username] = data
    # Retourne un message de confirmation avec le code HTTP 201 (création)
    return jsonify({"message": "User added", "user": data}), 201


# Lancement du serveur Flask uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    app.run()
