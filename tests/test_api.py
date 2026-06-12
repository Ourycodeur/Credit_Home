from fastapi.testclient import TestClient
from api.main import app

## Definissons la variable client

client = TestClient(app)

def test_root():
    reponse = client.get("/")
    
    assert reponse.status_code == 200
    
    assert reponse.json() == {
        "message" :"Bienvenue sur l'API de prédiction d'accord de crédit bancaire!"
    }
    
    
# Testons les endpoints de prediction

def test_prediction ():
    Entré = {
        "EXT_SOURCE_1": 30,
        "EXT_SOURCE_2": 40,
        "EXT_SOURCE_3": 35,
        "INSTAL_AMT_PAYMENT_sum": 45,
        "AMT_CREDIT": 1000,
        "CC_AMT_BALANCE_mean": 36,
        "DAYS_BIRTH": 15,
        "AMT_ANNUITY": 20,
        "AMT_GOODS_PRICE": 1000,
        "DAYS_EMPLOYED": 25,
        "PREV_CNT_PAYMENT_mean": 250,
        "INSTAL_PAYMENT_DIFF_mean": 25, 
        "DAYS_ID_PUBLISH": 35,
        "PREV_CNT_PAYMENT_max": 25,
        "INSTAL_AMT_PAYMENT_mean": 250,
        "POS_MONTHS_BALANCE_min": 25,
        "BUREAU_AMT_CREDIT_SUM_DEBT_mean": 30,
        "BUREAU_AMT_CREDIT_SUM_mean": 40,
        "BUREAU_DAYS_CREDIT_max": 35,
        "POS_SK_DPD_DEF_mean": 22
    }
    
    
    response = client.post(
        "/predict",
        json = Entré
    )
    
    assert response.status_code ==200
    
    data = response.json()
    
    assert "prediction" in data
    assert "probability" in data
    assert isinstance(data["prediction"], int)

    assert isinstance(data["probability"], float)
    

# Testons les cas d'erreur

def test_prediction_invalid_data():
    Entré = {
       "EXT_SOURCE_1": "Mamadou",
        "EXT_SOURCE_2": 40,
        "AMT_CREDIT": -1000 
    }
    
    response = client.post(
        "/predict",
        json=Entré
    )
    
    assert response.status_code ==422
    
# Testons la santé 

def test_health():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "API en bonne santé et tourne"}