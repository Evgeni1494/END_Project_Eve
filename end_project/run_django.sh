#!/bin/bash

echo "Choisissez l'environnement :"
echo "1. Développement (SQLite)"
echo "2. Production (PostgreSQL)"
read -p "Entrez votre choix (1 ou 2): " choix

if [ "$choix" == "1" ]; then
  export DJANGO_PRODUCTION=false
elif [ "$choix" == "2" ]; then
  export DJANGO_PRODUCTION=true
else
  echo "Choix non valide."
  exit 1
fi

python manage.py runserver
