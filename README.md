# 🏠 House Price Prediction

Ce projet est une application web de **prédiction des prix des maisons**. L'utilisateur saisit les caractéristiques d'une maison via une interface web, et l'API Flask prédit le prix de la maison.

## 🚀 Fonctionnalités
- 📦 **API Flask** pour exposer le modèle de machine learning.
- 🐳 **Conteneur Docker** pour l'application.
- ☸️ **Orchestration Kubernetes** (3 réplicas, service exposé via LoadBalancer).
- 📈 **Modèle ML** basé sur **Linear Regression**.
  

## 🛠️ Instructions de déploiement

### 1️⃣ **Exécuter avec Docker**
```bash
docker build -t house-price-api:latest .
docker run -p 5000:5000 house-price-api:latest

### 2️⃣ **Exécuter avec Kubernetes**
minikube start
minikube docker-env | Invoke-Expression
docker build -t house-price-api:latest .
kubectl apply -f k8s/
minikube service house-price-service --url

## 📈 Prédiction des prix
Requête POST : /predict
Exemple de corps de la requête :
{
  "area": 5000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": 1,
  "guestroom": 0,
  "basement": 1,
  "hotwaterheating": 0,
  "airconditioning": 1,
  "parking": 1,
  "prefarea": 1,
  "furnishingstatus_semi-furnished": 0,
  "furnishingstatus_unfurnished": 1
}

