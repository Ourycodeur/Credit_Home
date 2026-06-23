import time
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "Modèle" / "lgbm_credit_model.pkl"

model = joblib.load(model_path)
model.set_params(n_jobs=1)

sample = pd.DataFrame([{
    "EXT_SOURCE_1": 0.4,
    "EXT_SOURCE_2": 0.3,
    "EXT_SOURCE_3": 10.3,
    "INSTAL_AMT_PAYMENT_sum": 10.4,
    "AMT_CREDIT": 0.5,
    "CC_AMT_BALANCE_mean": 0.9,
    "DAYS_BIRTH": 0.9,
    "AMT_ANNUITY": 0.4,
    "AMT_GOODS_PRICE": 0.5,
    "DAYS_EMPLOYED": 0.6,
    "PREV_CNT_PAYMENT_mean": 0.8,
    "INSTAL_PAYMENT_DIFF_mean": 0.7,
    "DAYS_ID_PUBLISH": 0.6,
    "PREV_CNT_PAYMENT_max": 0.3,
    "INSTAL_AMT_PAYMENT_mean": 0.4,
    "POS_MONTHS_BALANCE_min": 0.7,
    "BUREAU_AMT_CREDIT_SUM_DEBT_mean": 0.5,
    "BUREAU_AMT_CREDIT_SUM_mean": 0.8,
    "BUREAU_DAYS_CREDIT_max": 0.9,
    "POS_SK_DPD_DEF_mean": 0.9
}])


def test_inference_time():

    start = time.perf_counter()

    model.predict(sample)

    end = time.perf_counter()

    inference_time = end - start

    assert inference_time < 1