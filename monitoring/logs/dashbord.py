import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Monitoring Home Credit")



production = pd.read_json(
    "monitoring/logs/prediction_logs.jsonl",
    lines=True
)

st.metric(
    "Nombre de prédictions",
    len(production)
)

st.metric(
    "Latence moyenne",
    round(
        production["execution_time"].mean(),
        3
    )
)

st.subheader("Distribution des prédictions")

st.bar_chart(
    production["predicted_label"].value_counts()
)

st.subheader("Probabilités")

st.line_chart(
    production["probability"]
)

st.subheader("Temps d'exécution")

st.line_chart(
    production["execution_time"]
)

st.subheader("Données brutes")

st.dataframe(production)