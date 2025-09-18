import pickle
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Charger le pipeline complet
model = pickle.load(open("car__model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("car_price_predictor.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.to_dict()
        
        # Transformer "Première Main" de Oui/Non vers 1/0 comme pendant l'entraînement
        if "Première Main" in data:
            data["Première main"] = 1 if data["Première main"] == "Oui" else 0
        else:
            data["Première main"] = 0  # Par défaut Non = 0
        
        # Si besoin, convertir les cases à cocher en 0/1
        checkbox_cols = [
            "Jantes aluminium", "Airbags", "Climatisation", "Système de navigation/GPS",
            "Toit ouvrant", "Sièges cuir", "Radar de recul", "Caméra de recul",
            "Vitres électriques", "ABS", "ESP", "Régulateur de vitesse",
            "Limiteur de vitesse", "CD/MP3/Bluetooth", "Ordinateur de bord",
            "Verrouillage centralisé à distance"
        ]
        
        for col in checkbox_cols:
            data[col] = 1 if col in data else 0
        
        # Convertir les colonnes numériques si nécessaire
        numeric_cols = ["Année-Modèle", "Kilométrage", "Puissance fiscale", "Nombre de portes"]
        for col in numeric_cols:
            if col in data:
                try:
                    data[col] = float(data[col])
                except (ValueError, TypeError):
                    data[col] = 0
        
        df = pd.DataFrame([data])
        
        # Faire la prédiction
        prediction = model.predict(df)[0]
        
        return render_template("car_price_predictor.html",
                             prediction_text=f"Prix estimé : {prediction:,.0f} MAD")
    
    except Exception as e:
        return render_template("car_price_predictor.html",
                             prediction_text=f"Erreur: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)