import sqlite3
import pandas as pd
import streamlit as st

# Connexion à la base
conn = sqlite3.connect("Netflixdata.db")

# Exemple : chargement d'une table
df = pd.read_sql_query("SELECT * FROM Movie LIMIT 10", conn)

# Affichage dans Streamlit
st.title("Aperçu de la base Netflix 🎬")
st.dataframe(df)

# Tu peux maintenant créer des visualisations à partir de df
