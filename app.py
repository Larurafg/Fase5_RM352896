# app.py

import streamlit as st
from carregar_cvs import carregar_cv_arquivo
from melhorar_cv import melhorar_cv

# Carrega dados
cvs = carregar_cv_arquivo("applicants.json")

st.title("Melhorador de Currículos com IA Local")

# Seleção
nomes = [f"{cv['nome']} ({cv['id']})" for cv in cvs]
selecionado = st.selectbox("Selecione um candidato:", nomes)

if selecionado:
    idx = nomes.index(selecionado)
    cv = cvs[idx]

    st.subheader("Currículo Original")
    st.text_area("Texto original", cv["cv_original"], height=300)

    if st.button("Melhorar Currículo"):
        with st.spinner("Melhorando currículo..."):
            novo_cv = melhorar_cv(cv["cv_original"])
        st.subheader("Currículo Melhorado")
        st.text_area("Texto melhorado", novo_cv, height=300)
