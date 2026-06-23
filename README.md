# 🚀 Projet 8 - Déployez un modèle dans le cloud et mettez en place une démarche MLOps

## 📌 Contexte

Ce projet a pour objectif de mettre en production un modèle de Machine Learning capable de prédire l'accord ou le refus d'un crédit bancaire à partir des données du projet Home Credit.

L'ensemble du cycle de vie du modèle a été implémenté selon une démarche MLOps complète :

- Développement du modèle
- Création d'une API REST
- Containerisation avec Docker
- Intégration Continue (CI)
- Déploiement Continu (CD)
- Monitoring des prédictions
- Détection de Data Drift
- Optimisation post-déploiement

## 🎯 Objectifs du projet

- Déployer un modèle de Machine Learning en production.
- Exposer le modèle via une API REST.
- Automatiser les tests et les déploiements.
- Mettre en place un système de monitoring.
- Détecter les dérives des données.
- Optimiser les performances après déploiement.
- Mettre en œuvre une démarche MLOps de bout en bout.

## 🏗️ Architecture

- API FastAPI
- PostgreSQL
- Docker
- GitHub Actions (CI/CD)
- Hugging Face Spaces
- Streamlit
- Evidently AI
- LightGBM

## 🌐 API

Endpoints :
- GET /
- POST /predict
- GET /health

## 🐳 Docker

Construction :

```bash
docker build -t p8-api:latest .
```

## ⚙️ CI/CD

- Branche develop : Intégration Continue
- Branche main : Déploiement Continu

## 📊 Monitoring

Logs JSON contenant :
- Inputs
- Outputs
- Probabilités
- Temps d'exécution
- Statut des requêtes

## 🔍 Data Drift

Détection réalisée avec Evidently AI à partir :
- Des données de référence
- Des données de production

## ⚡ Optimisation

Analyse avec cProfile.

Optimisation appliquée :

```python
model.set_params(n_jobs=1)
```

## 🧪 Tests

- test_api.py
- test_model.py
- test_performance.py
- test_optimisation.py

Lancement :

```bash
pytest -v
```

## 🛠️ Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- LightGBM
- Docker
- GitHub Actions
- Streamlit
- Evidently AI
- Hugging Face

## 👨‍💻 Auteur

Mamadou Oury Baldé
