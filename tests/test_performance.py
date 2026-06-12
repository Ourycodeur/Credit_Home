import time 
from fastapi import Path
import pandas as pd
import joblib
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "../Modèle/lgbm_credit_model.pkl"
model = joblib.load(model_path)

# Testons les predictions

def test_prediction_speed():
    data = pd.DataFrame([{
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
    }])
    
    start = time.time()

    model.predict(data)

    end = time.time()

    assert (end - start) < 1
    