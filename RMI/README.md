# Projet RMI en Java

## Description
Ce projet montre comment communiquer entre un client et un serveur avec **Java RMI**. Le client appelle une méthode distante qui renvoie un message de bienvenue.

## Structure du projet
- `Hello.java` : définit l'interface distante.
- `HelloImpl.java` : implémente la méthode `sayHello()`.
- `Server.java` : démarre le registre RMI et enregistre l'objet distant.
- `Client.java` : recherche l'objet distant et appelle sa méthode.

## Éléments importants
- `Remote` : indique que l'interface peut être utilisée à distance.
- `UnicastRemoteObject` : permet d'exposer un objet distant.
- `RemoteException` : gère les erreurs de communication.
- `Naming.lookup()` : récupère l'objet distant.
- `Naming.rebind()` : enregistre l'objet dans le registre RMI.

Ce projet n'utilise pas d'annotations Java spécifiques.

## Exécution
Depuis le dossier parent de `RMI` :

```bash
javac RMI/*.java
```

Terminal 1 — démarrer le serveur :

```bash
java RMI.Server
```

Terminal 2 — lancer le client :

```bash
java RMI.Client
```

**Résultat attendu :**

```text
Salut Emna ! Bienvenue dans mon serveur RMI.
```