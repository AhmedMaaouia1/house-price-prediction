from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger le modèle pré-entraîné
model = joblib.load('models/house_price_model.pkl')

# Les colonnes numériques qui doivent être standardisées
numeric_columns = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

# Les colonnes utilisées pendant l'entraînement (dans le bon ordre)
all_columns = [
    'area', 'bedrooms', 'bathrooms', 'stories', 
    'mainroad', 'guestroom', 'basement', 
    'hotwaterheating', 'airconditioning', 
    'parking', 'prefarea', 
    'furnishingstatus_semi-furnished', 
    'furnishingstatus_unfurnished'
]

# Les moyennes et écarts-types utilisés pour la normalisation (à personnaliser)
mean_values = {'area': 5150.54, 'bedrooms': 2.97, 'bathrooms': 1.29, 'stories': 1.81, 'parking': 0.69}
std_values = {'area': 2170.14, 'bedrooms': 0.74, 'bathrooms': 0.50, 'stories': 0.87, 'parking': 0.86}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1️⃣ Récupération des données de la requête
        data = request.get_json()
        
        # 2️⃣ Assurer la conversion des données en float
        features = {key: float(value) for key, value in data.items()}
        
        # 3️⃣ Réorganiser les colonnes dans le bon ordre
        feature_values = [features[column] for column in all_columns]
        
        # 4️⃣ Normaliser les colonnes numériques
        for i, col in enumerate(all_columns):
            if col in numeric_columns:
                # Applique la normalisation
                feature_values[i] = (feature_values[i] - mean_values[col]) / std_values[col]
        
        # 5️⃣ Transformer en tableau numpy
        feature_array = np.array([feature_values])
        
        # 6️⃣ Prédire le prix de la maison
        prediction = model.predict(feature_array)
        
        # 7️⃣ Retourner la prédiction au format JSON
        return jsonify({'predicted_price': round(prediction[0], 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
