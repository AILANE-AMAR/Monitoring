# Monitoring
MonitoringSystem
Ce projet est un système de surveillance des ressources système développé en Python, Bash, SQLite et Flask.
Il permet de surveiller le CPU, la RAM, l’espace disque et les utilisateurs actifs.

Objectif :

Collecter et stocker les informations système.

Détecter les dépassements de seuil et envoyer une alerte email.

Récupérer les alertes de sécurité depuis le site CERT-FR.

Fournir une interface web Flask avec des graphiques.

Fonctionnalités principales :

Collecte des données système avec scripts Python et Bash.

Base de données SQLite pour l’historique.

Nettoyage automatique des anciennes données.

Scraping du site cert.ssi.gouv.fr pour récupérer les alertes.

Génération de graphiques SVG avec Pygal.

Interface web Flask pour visualiser les données et gérer les seuils.

Automatisation avec scripts Bash et crontab.

Installation :

Cloner le dépôt avec : git clone git@github.com
:AILANE-AMAR/Monitoring.git

Créer un environnement virtuel et installer les dépendances :
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Lancer l’application Flask avec : python3 parte_4/app.py

Ouvrir http://localhost:5000
 dans un navigateur.

Organisation du projet :

parte_1 : scripts de collecte (CPU, RAM, disque, utilisateurs)

parte_2 : nettoyage, sauvegarde et récupération alertes CERT-FR

parte_3 : génération des graphiques et alertes email

parte_4 : application Flask (interface web)

Automatisation :
Un script finalexecute.sh permet de lancer tout le projet.
Vous pouvez l’exécuter automatiquement avec crontab.
Exemple : 0 * * * * /home/vboxuser/mini-projet/finalexecute.sh

Bibliothèques utilisées :

Flask

Pygal

Requests, BeautifulSoup

SQLite3

smtplib, email.mime

Auteur :
AILANE AMAR (GitHub : https://github.com/AILANE-AMAR
)
