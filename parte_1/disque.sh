#!/bin/bash
 sleep 1
# Récupérer les informations du disque
total_space=$(df / --output=size  | tail -n 1)  # Espace total
used_space=$(df / --output=used  | tail -n 1)   # Espace utilisé
free_space=$(df / --output=avail  | tail -n 1)  # Espace libre
sqlite3 /home/vboxuser/mini-projet/monitoring.db "INSERT INTO disk (total_space, used_space, free_space,date) VALUES ('$total_space', '$used_space', '$free_space', datetime('now'));"
echo "Total espace disque : $total_space"
echo "Espace utilisé : $used_space"
echo "Espace libre : $free_space"
