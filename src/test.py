import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Scoring de Crédit", page_icon="🛡️", layout="wide")

# --- Chargement du modèle ---
@st.cache_resource
def load_model():
    return joblib.load("../Modèle/lgbm_credit_model.pkl")

model = load_model()

# --- Fonction de prédiction ---
def predict(features: dict) -> dict:
    data = pd.DataFrame([features])
    prediction_proba = model.predict_proba(data)[:, 1][0]
    prediction = int(prediction_proba >= 0.52)
    message = (
        "⚠️ La personne risque de ne pas rembourser le crédit."
        if prediction == 1
        else "✅ Nous pouvons accorder le crédit à la personne."
    )
    return {
        "message": message,
        "prediction": prediction,
        "probability": float(prediction_proba),
    }

# --- Interface ---
st.title("🛡️ Scoring de crédit — Prédiction")
st.caption("Renseignez les variables du client pour obtenir une recommandation.")

st.divider()

FEATURE_GROUPS = {
    "Sources externes": [
        ("EXT_SOURCE_1", 0.51, 0.0, 1.0, 0.01),
        ("EXT_SOURCE_2", 0.45, 0.0, 1.0, 0.01),
        ("EXT_SOURCE_3", 0.62, 0.0, 1.0, 0.01),
    ],
    "Montants du crédit": [
        ("AMT_CREDIT", 270000.0, 0.0, 5_000_000.0, 1000.0),
        ("AMT_ANNUITY", 13500.0, 0.0, 500_000.0, 500.0),
        ("AMT_GOODS_PRICE", 225000.0, 0.0, 5_000_000.0, 1000.0),
        ("CC_AMT_BALANCE_mean", 4200.0, -100_000.0, 500_000.0, 100.0),
    ],
    "Informations temporelles": [
        ("DAYS_BIRTH", -14513, -25000, -6000, 1),
        ("DAYS_EMPLOYED", -2421, -20000, 0, 1),
        ("DAYS_ID_PUBLISH", -3012, -8000, 0, 1),
    ],
    "Historique des paiements (installations)": [
        ("INSTAL_AMT_PAYMENT_sum", 584320.0, 0.0, 10_000_000.0, 1000.0),
        ("INSTAL_AMT_PAYMENT_mean", 9870.0, 0.0, 500_000.0, 100.0),
        ("INSTAL_PAYMENT_DIFF_mean", -120.0, -50_000.0, 50_000.0, 100.0),
    ],
    "Crédits précédents": [
        ("PREV_CNT_PAYMENT_mean", 18.0, 0.0, 60.0, 0.5),
        ("PREV_CNT_PAYMENT_max", 24.0, 0.0, 120.0, 1.0),
    ],
    "Données POS & Bureau": [
        ("POS_MONTHS_BALANCE_min", -48.0, -120.0, 0.0, 1.0),
        ("POS_SK_DPD_DEF_mean", 0.0, 0.0, 90.0, 0.01),
        ("BUREAU_AMT_CREDIT_SUM_DEBT_mean", 15000.0, -500_000.0, 2_000_000.0, 1000.0),
        ("BUREAU_AMT_CREDIT_SUM_mean", 32000.0, 0.0, 5_000_000.0, 1000.0),
        ("BUREAU_DAYS_CREDIT_max", -180.0, -3000.0, 0.0, 1.0),
    ],
}

features = {}
for group_name, fields in FEATURE_GROUPS.items():
    with st.expander(group_name, expanded=True):
        cols = st.columns(3)
        for i, (name, default, min_val, max_val, step) in enumerate(fields):
            with cols[i % 3]:
                features[name] = st.number_input(
                    label=name,
                    value=default,
                    min_value=float(min_val),
                    max_value=float(max_val),
                    step=float(step),
                    format="%.2f" if step < 1 else "%.0f",
                )

st.divider()

if st.button("🔍 Lancer la prédiction", use_container_width=True, type="primary"):
    with st.spinner("Calcul en cours..."):
        result = predict(features)

    pred = result["prediction"]
    proba = result["probability"]
    message = result["message"]

    # Couleur selon le résultat
    if pred == 1:
        color = "red"
        icon = "🔴"
        badge_label = "Risque élevé"
    else:
        color = "green"
        icon = "🟢"
        badge_label = "Faible risque"

    st.markdown(f"### {icon} Résultat")

    col1, col2, col3 = st.columns(3)
    col1.metric("Prédiction", pred, help="0 = crédit accordé, 1 = crédit refusé")
    col2.metric("Probabilité de défaut", f"{proba:.2%}")
    col3.metric("Seuil appliqué", "52%")

    st.markdown(f"**{message}**")

    # Barre de probabilité
    st.markdown("##### Probabilité de défaut")
    st.progress(proba)

    threshold_pct = int(0.52 * 100)
    current_pct = int(proba * 100)
    st.caption(
        f"Probabilité actuelle : **{current_pct}%** — seuil de classification : **{threshold_pct}%**"
    )

    if pred == 1:
        st.error(f"🚨 {badge_label} — Le score dépasse le seuil de 52%.")
    else:
        st.success(f"✅ {badge_label} — Le score est en dessous du seuil de 52%.")