# 1. Utiliser une image Python légère

FROM python:3.11-slim

 

# 2. Définir le répertoire de travail dans le conteneur

WORKDIR /app

 

# 3. Empêcher Python de générer des fichiers .pyc et forcer l'affichage des logs

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

 

# 4. Installer les dépendances système nécessaires

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

 

# 5. Copier le fichier des dépendances et les installer

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

 

# 6. Copier tout le reste du code du projet

COPY . .

 

# 7. Exposer le port utilisé par Django

EXPOSE 8000

 

# 8. Commande de lancement (Serveur de développement pour ce TP)

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]