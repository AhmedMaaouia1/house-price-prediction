# 🏠 House Price Prediction

Ce projet est une application web de **prédiction des prix des maisons**. L'utilisateur saisit les caractéristiques d'une maison via une interface web, et l'API Flask prédit le prix de la maison.

---

## 🚀 Fonctionnalités
- 📦 **API Flask** : Expose un modèle de machine learning pour effectuer des prédictions.
- 🐳 **Conteneur Docker** : Simplifie le déploiement de l'application.
- ☸️ **Orchestration Kubernetes** : Déploiement en cluster avec 3 réplicas et service exposé via LoadBalancer.
- 📈 **Modèle ML** : Basé sur une **régression linéaire** pour prédire les prix.

---

## 🛠️ Instructions de déploiement

### 1️⃣ Exécuter avec Docker
docker build -t house-price-api:latest .
docker run -p 5000:5000 house-price-api:latest

### 2️⃣ Exécuter avec Kubernetes
minikube start
minikube docker-env | Invoke-Expression
docker build -t house-price-api:latest .
kubectl apply -f k8s/
minikube service house-price-service --url

---

## 📈 Prédiction des prix

### Endpoint API : `/predict`
**Méthode :** POST

### Exemple de corps de la requête :
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

### Exemple de réponse :
{
  "predicted_price": 6664180.12
}

![image](https://github.com/user-attachments/assets/76efc704-2673-428f-952a-b50932b048fc)

---

## 📁 Structure du projet
house-price-prediction/
\n├ ── src/                  # Code source de l'application Flask
│   ├ ── app.py            # API Flask
│   ├ ── model.py          # Chargement du modèle
│   └ ── utils.py          # Fonctions utilitaires
\n├ ── k8s/                  # Fichiers de configuration Kubernetes
│   ├ ── Deployment.yaml
│   ├ ── Service.yaml
│   └ ── Ingress.yaml      # (Optionnel)
├ ── models/               # Modèle ML sauvegardé (fichier .pkl)
├ ── data/                 # Données d'entraînement (optionnel)
├ ── Dockerfile            # Dockerfile pour construire l'image
├ ── requirements.txt      # Liste des dépendances Python
├ ── README.md             # Documentation du projet
└ ── .gitignore            # Fichiers et dossiers ignorés par Git

---

## 📜 Auteur
- **MAAOUIA Ahmed**  
  Data Engineer et passionné par le Machine Learning et Kubernetes.

---

## 🌟 Améliorations futures
- Intégrer un modèle de machine learning plus complexe (par ex. Random Forest, XGBoost).
- Ajouter des tests automatisés pour valider l'API (Pytest).
- Configurer un pipeline CI/CD avec GitHub Actions pour automatiser le déploiement.

