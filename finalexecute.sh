#!/bin/bash

# Chemin du projet
PROJECT_DIR="/home/vboxuser/mini-projet"

echo "===== Début de l'exécution du projet MonitoringSystem ====="

# Partie 1 : Collecte des données
echo "-> Exécution de collect.py"
python3 $PROJECT_DIR/parte_1/collect.py

echo "-> Exécution de collect.sh"
bash $PROJECT_DIR/parte_1/collect.sh

echo "-> Exécution de disque.sh"
bash $PROJECT_DIR/parte_1/disque.sh

# Partie 3 : Génération des graphiques
echo "-> Exécution de graph.py"
python3 $PROJECT_DIR/graph.py

# Partie 2 : Alertes et nettoyage
echo "-> Exécution de alert.py (alertes CERT-FR)"
python3 $PROJECT_DIR/parte_2/alert.py

echo "-> Exécution de netoyage.py (nettoyage base de données)"
python3 $PROJECT_DIR/parte_2/netoyage.py

echo "===== Fin de l'exécution du projet ====="
