import time
import pandas as pd
import joblib

model = joblib.load(
    "C:\\Users\\El. OURY BALDE\\Documents\\P8\\Modèle\\lgbm_credit_model.pkl"
)

sample = pd.DataFrame([{
    "EXT_SOURCE_1":0.4,
    "EXT_SOURCE_2":0.3,
    "EXT_SOURCE_3": 35,
    "INSTAL_AMT_PAYMENT_sum" : 45,
    "AMT_CREDIT" : 1000,
    "CC_AMT_BALANCE_mean" :36,
    "DAYS_BIRTH" :15,
    "AMT_ANNUITY" :20,
    "AMT_GOODS_PRICE" :1000,
    "DAYS_EMPLOYED" :25,
    "PREV_CNT_PAYMENT_mean" :250,
    "INSTAL_PAYMENT_DIFF_mean" : 25,
    "DAYS_ID_PUBLISH" :35,
    "PREV_CNT_PAYMENT_max":25,
    "INSTAL_AMT_PAYMENT_mean":250,
    "POS_MONTHS_BALANCE_min":25,
    "BUREAU_AMT_CREDIT_SUM_DEBT_mean" :30,
    "BUREAU_AMT_CREDIT_SUM_mean" :40,
    "BUREAU_DAYS_CREDIT_max" :35,
    "POS_SK_DPD_DEF_mean" :22

    
}])

times = []

for _ in range(100):

    start = time.time()

    model.predict(sample)

    end = time.time()

    times.append(end-start)

print("Temps moyen :", sum(times)/len(times))
print("Temps max :", max(times))
print("Temps min :", min(times))