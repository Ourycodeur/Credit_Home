## Créons les entrées de la personne et la sortie
from sqlalchemy import Column, Float

from db.models import PersonalInputs, PersonalOutputs


## Insertions des features d'entrée de l'employé dans la base de données

def create_personal_input(db,data):
    personal = PersonalInputs(
    EXT_SOURCE_1 = data.EXT_SOURCE_1,
    EXT_SOURCE_2 = data.EXT_SOURCE_2,
    EXT_SOURCE_3 = data.EXT_SOURCE_3,

    INSTAL_AMT_PAYMENT_sum = data.INSTAL_AMT_PAYMENT_sum,
    AMT_CREDIT = data.AMT_CREDIT,
    CC_AMT_BALANCE_mean = data.CC_AMT_BALANCE_mean,
    DAYS_BIRTH = data.DAYS_BIRTH,
    AMT_ANNUITY = data.AMT_ANNUITY,
    AMT_GOODS_PRICE = data.AMT_GOODS_PRICE,
    DAYS_EMPLOYED = data.DAYS_EMPLOYED,
    PREV_CNT_PAYMENT_mean = data.PREV_CNT_PAYMENT_mean,
    INSTAL_PAYMENT_DIFF_mean = data.INSTAL_PAYMENT_DIFF_mean,
    DAYS_ID_PUBLISH = data.DAYS_ID_PUBLISH,
    PREV_CNT_PAYMENT_max = data.PREV_CNT_PAYMENT_max,
    INSTAL_AMT_PAYMENT_mean = data.INSTAL_AMT_PAYMENT_mean,
    POS_MONTHS_BALANCE_min = data.POS_MONTHS_BALANCE_min,
    BUREAU_AMT_CREDIT_SUM_DEBT_mean = data.BUREAU_AMT_CREDIT_SUM_DEBT_mean,
    BUREAU_AMT_CREDIT_SUM_mean = data.BUREAU_AMT_CREDIT_SUM_mean,
    BUREAU_DAYS_CREDIT_max = data.BUREAU_DAYS_CREDIT_max,
    POS_SK_DPD_DEF_mean = data.POS_SK_DPD_DEF_mean
    )
    
    db.add(personal)
    db.commit()
    db.refresh(personal)
    
    return personal

## Insertions des résultats de prédiction dans la base de données

def creation_prediction(
    db,
    personal_input_id,
    target,
    probability
):
    prediction = PersonalOutputs(
    personal_id=personal_input_id,
    target=int(target),
    probability=float(probability),
    model_version="1.0"
)
    
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    
    return prediction
    
    
    