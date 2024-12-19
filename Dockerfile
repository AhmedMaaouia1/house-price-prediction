# Utiliser l'image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'application
EXPOSE 5000

# Démarrer l'application
CMD ["python", "src/app.py"]
