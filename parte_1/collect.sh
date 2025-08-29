#! /bin/bash
USERS=$(who | wc -l)
sqlite3 /home/vboxuser/mini-projet/monitoring.db "INSERT INTO users (NBR) VALUES ('$USERS');"
echo "Le nombre de USER est : $USERS"

