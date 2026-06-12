# Mettons en place un environnement de travail pour notre projet de déploiement d'un modèle de machine learning avec FastAPI et Docker.

# Image de base 
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installation des dépendance nécessaire pour faire tourne LGM
RUN apt-get update && apt-get install -y \
   gcc \
    g++ \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copier les dependances
COPY requirements.txt .

# Installer les dependances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]