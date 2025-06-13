
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("Monitor de Produção Industrial")

volume = st.number_input("Volume Produzido", min_value=0)
tempo_ciclo = st.number_input("Tempo de Ciclo (segundos)", min_value=0.0)
refugo = st.number_input("Porcentagem de Refugo", min_value=0.0)

if st.button("Verificar Status"):
    model = joblib.load('modelo/modelo.pkl')
    entrada = np.array([[volume, tempo_ciclo, refugo]])
    pred = model.predict(entrada)
    resultado = 'Anomalia Detectada ❌' if pred[0] == -1 else 'Processo Normal ✅'
    st.success(resultado)
