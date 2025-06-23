import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV-Datei laden
df = pd.read_csv("data/cem_SVM_breastcancer_kappa_0-0.5.csv")

st.title("CEM-Ergebnisse: Gegenfaktorenanalyse")

# Dropdown für kappa
kappa_val = st.selectbox("Wähle kappa-Wert", sorted(df["kappa"].unique()))

# Daten filtern
filtered = df[df["kappa"] == kappa_val]

# Erfolgsrate anzeigen
success_rate = filtered["success"].mean()
st.metric("Erfolgsrate", f"{success_rate:.2%}")

# Diagramm: Original vs. CF-Probs
st.subheader("Wahrscheinlichkeiten: Original vs. Gegenfaktum")
sns.scatterplot(x=filtered["original_prob"], y=filtered["cf_prob"])
plt.xlabel("Original-Proba")
plt.ylabel("CF-Proba")
st.pyplot(plt)
