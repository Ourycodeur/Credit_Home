## C'est dans cette section que nous mettrons en place l'api
# Importation des librairies nécessaires
import joblib
import pandas as pd
import numpy as np
import uvicorn
from fastapi import Depends, FastAPI
from api.database import SessionLocal, engine
from api.crud import create_personal_input, creation_prediction
from api.schemas import CreditRequest
from sqlalchemy.orm import Session
from db.models import Base
from pathlib import Path
import json
import time


# Création de la base de données
Base.metadata.create_all(bind=engine)


# Chargement du modèle pré-entraîné
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "../Modèle/lgbm_credit_model.pkl"
model = joblib.load(model_path)

# Initialisation de l'application FastAPI
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Endpoint pour faire un affichage de bienvenue
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction d'accord de crédit bancaire!"}

# Endpoint pour faire une prédiction
@app.post("/predict/")

def predict(personal_input: CreditRequest, db: Session = Depends(get_db)):
    # Enregistrement des données d'entrée dans la base de données
    #personal_input_db = create_personal_input(db, personal_input)
    
    start_time = time.time()
    # Préparation des données pour la prédiction
    input_dict = personal_input.model_dump()
    input_data = pd.DataFrame([input_dict])
    
    # Prédiction avec le modèle pré-entraîné
    prediction_proba = model.predict_proba(input_data)[:, 1][0]
    prediction = int(prediction_proba >= 0.52)  # Seuil de 0.52 pour la classification binaire
    predicted_label = prediction  # 0 ou 1 selon la prédiction
    # Conversion
    
    predicted_label = int(predicted_label)
    probability = float(prediction_proba)
    
    # Enregistrement de la prédiction dans la base de données
    personal_input = create_personal_input(
        db=db,
        data=personal_input)
    
    # Insertion et prediction
    
    creation_prediction(
        db=db,
        personal_input_id=personal_input.id,
        target=prediction,
        probability=prediction_proba
    )
    
    # Calcul du temps d'exécution
    execution_time = time.time() - start_time
    
    # Structure du log
    log_data = {
        "input_data": input_dict,
        "predicted_label": prediction,
        "probability": probability,
        "execution_time": execution_time,
        "status": "success",
        #"features": input_dict.dict(),
    }
    # Enregistrement du log dans un fichier JSON
    
    log_file_path = BASE_DIR / "../monitoring/logs/prediction_logs.jsonl"
    with open(log_file_path, "a") as log_file:
        json.dump(log_data, log_file)
        log_file.write("\n")
   
    
    
    
    # Message de retour avec la prédiction et la probabilité
    message = (
        "La Personne risque de ne pas payer le crédit"
        if predicted_label ==1
        else "Nous pouvons accorder le crédit à la personne "
    )
    
    # Retour de la prédiction et de la probabilité
    return {
        "message": message,
        "prediction": predicted_label,
        "probability": probability
    }


    
    if __name__ =="__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
        
@app.get("/health")
def health():
    return {"status": "API en bonne santé et tourne"}