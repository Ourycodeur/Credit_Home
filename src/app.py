import streamlit as st 
import joblib
import pandas as pd 

# Chargeons le modèle 
model = joblib.load("../Modèle/lgbm_credit_model.pkl")

def predict(
    EXT_SOURCE_1,
    EXT_SOURCE_2,
    EXT_SOURCE_3,
    INSTAL_AMT_PAYMENT_sum,
    AMT_CREDIT,
    CC_AMT_BALANCE_mean,
    DAYS_BIRTH,
    AMT_ANNUITY,
    AMT_GOODS_PRICE,
    DAYS_EMPLOYED,
    PREV_CNT_PAYMENT_mean,
    INSTAL_PAYMENT_DIFF_mean,
    DAYS_ID_PUBLISH,
    PREV_CNT_PAYMENT_max,
    INSTAL_AMT_PAYMENT_mean,
    POS_MONTHS_BALANCE_min,
    BUREAU_AMT_CREDIT_SUM_DEBT_mean,
    BUREAU_AMT_CREDIT_SUM_mean,
    BUREAU_DAYS_CREDIT_max,
    POS_SK_DPD_DEF_mean
):
    data = pd.DataFrame([{
        "EXT_SOURCE_1":EXT_SOURCE_1,
        "EXT_SOURCE_2":EXT_SOURCE_2,
        "EXT_SOURCE_3":EXT_SOURCE_3,
        "INSTAL_AMT_PAYMENT_sum":INSTAL_AMT_PAYMENT_sum,
        "AMT_CREDIT":AMT_CREDIT,
        "CC_AMT_BALANCE_mean":CC_AMT_BALANCE_mean,
        "DAYS_BIRTH":DAYS_BIRTH,
        "AMT_ANNUITY":AMT_ANNUITY,
        "AMT_GOODS_PRICE":AMT_GOODS_PRICE,
        "DAYS_EMPLOYED":DAYS_EMPLOYED,
        "PREV_CNT_PAYMENT_mean":PREV_CNT_PAYMENT_mean,
        "INSTAL_PAYMENT_DIFF_mean":INSTAL_PAYMENT_DIFF_mean,
        "DAYS_ID_PUBLISH":DAYS_ID_PUBLISH,
        "PREV_CNT_PAYMENT_max":PREV_CNT_PAYMENT_max,
        "INSTAL_AMT_PAYMENT_mean":INSTAL_AMT_PAYMENT_mean,
        "POS_MONTHS_BALANCE_min":POS_MONTHS_BALANCE_min,
        "BUREAU_AMT_CREDIT_SUM_DEBT_mean":BUREAU_AMT_CREDIT_SUM_DEBT_mean,
        "BUREAU_AMT_CREDIT_SUM_mean":BUREAU_AMT_CREDIT_SUM_mean,
        "BUREAU_DAYS_CREDIT_max":BUREAU_DAYS_CREDIT_max,
        "POS_SK_DPD_DEF_mean":POS_SK_DPD_DEF_mean
        
    }])
    
    prediction_proba = model.predict_proba(data)[:, 1][0]
    prediction = int(prediction_proba >= 0.52)  # Seuil de 0.52 pour la classification binaire
    predicted_label = prediction
    
    predicted_label = int(predicted_label)
    probability = float(prediction_proba)

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