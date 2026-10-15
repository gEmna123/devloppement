# Projet SOAP en Python — Backend

## Description
Ce projet met en place un service web **SOAP** en Python avec la bibliothèque Spyne. Il permet de récupérer la liste des étudiants à travers une requête SOAP.

## Structure du projet
- `serviceListeEtudiants.py` : définit et démarre le serveur SOAP.
- `client.py` : envoie une requête SOAP au serveur et affiche la réponse XML.
- `venv/` : contient l'environnement virtuel Python et les bibliothèques installées.

## Éléments importants
- `ServiceBase` : définit le service SOAP.
- `ComplexModel` : définit la structure d'un étudiant (`id`, `name`, `age`).
- `@rpc` : déclare une méthode accessible via SOAP.
- `Iterable(Student)` : indique que la méthode renvoie plusieurs étudiants.
- `Application` : configure le service SOAP.
- `WsgiApplication` : rend l'application accessible via un serveur WSGI.

## Exécution
Activer l'environnement virtuel :

```bash
source venv/bin/activate
```

Démarrer le serveur :

```bash
python serviceListeEtudiants.py
```

Dans un deuxième terminal, lancer le client :

```bash
source venv/bin/activate
python client.py
```

Le service peut être consulté à l'adresse `http://localhost:8000/?wsdl`.

## Résultat
Le client reçoit une réponse XML contenant les étudiants enregistrés dans le serveur.