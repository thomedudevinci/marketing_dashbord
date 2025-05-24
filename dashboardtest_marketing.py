import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

st.set_page_config(page_title="Dashboard Marketing", layout="wide")

st.title("📊 Dashboard Analyse Marketing - MarketyWeb")

# --- Données simulées ---
donnees = """
mois,canal,visites,conversions,taux_conversion,revenu
Janvier,Instagram,1200,80,6.7,3200
Janvier,Google Ads,1500,90,6.0,4000
Janvier,Emailing,800,70,8.75,3500
Février,Instagram,1300,95,7.3,3600
Février,Google Ads,1400,85,6.1,3900
Février,Emailing,850,65,7.6,3100
Mars,Instagram,1500,110,7.3,4100
Mars,Google Ads,1700,120,7.1,4700
Mars,Emailing,950,75,7.9,3600
"""

df = pd.read_csv(StringIO(donnees))

# --- Filtres dynamiques ---
mois = st.sidebar.multiselect("📅 Filtrer par mois :", options=df["mois"].unique(), default=df["mois"].unique())
canaux = st.sidebar.multiselect("📣 Filtrer par canal :", options=df["canal"].unique(), default=df["canal"].unique())

df_filtré = df[df["mois"].isin(mois) & df["canal"].isin(canaux)]

st.markdown("### 🔍 Analyse des performances par canal marketing")

# --- Graphique 1 : Visites par canal ---
fig1 = px.bar(df_filtré, x="canal", y="visites", color="mois", barmode="group", title="Nombre de visites par canal")
st.plotly_chart(fig1, use_container_width=True)

# --- Graphique 2 : Taux de conversion ---
fig2 = px.line(df_filtré, x="mois", y="taux_conversion", color="canal", markers=True, title="Évolution du taux de conversion")
st.plotly_chart(fig2, use_container_width=True)

# --- Graphique 3 : Répartition des revenus ---
fig3 = px.pie(df_filtré, names="canal", values="revenu", title="Répartition des revenus par canal")
st.plotly_chart(fig3, use_container_width=True)

# --- Recommandations stratégiques ---
st.markdown("## 💡 Recommandations stratégiques")

st.markdown("""
- **📌 Instagram** : Taux de conversion stable et élevé. Recommandé d’augmenter l’investissement publicitaire.
- **📌 Google Ads** : Bon volume de visites mais un taux de conversion à surveiller. Tester de nouveaux mots-clés.
- **📌 Emailing** : Très bon taux de conversion, mais volume faible. Optimiser l’acquisition d’emails.

Les décisions peuvent être affinées selon les objectifs : notoriété, conversion ou fidélisation.
""")

st.success("📈 Ce tableau de bord est un exemple concret de l’approche data-driven de MarketyWeb pour optimiser vos actions marketing.")
