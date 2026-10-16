# API REST de gestion des étudiants

## Description
Cette application utilise **Flask (Python)** pour démarrer un serveur web et préparer une API de gestion des étudiants.

## Fonctionnalités
- Afficher un message de bienvenue à la racine `/`.
- Stocker une liste d'étudiants avec leur identifiant, leur nom et leur âge.
- Écouter sur toutes les interfaces réseau avec le port `5001`.

## Installation

Créer et activer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```

Installer Flask :

```bash
python -m pip install flask
```

## Exécution

```bash
python3 app.py
```

## Test

Ouvrir dans un navigateur :

http://127.0.0.1:5001/

Le message suivant s'affiche :

`Bienvenue dans l'API de gestion des étudiants !`

## Technologies
- Python 3
- Flask
- JSON
