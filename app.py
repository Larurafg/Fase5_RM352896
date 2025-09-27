import streamlit as st
from carregar_cvs import carregar_cv_arquivo
from melhorar_cv import melhorar_cv

# Interface
st.title("Melhorador de Currículo com IA")
st.markdown("Utilizando o modelo **t5-small** para reescrever currículos em português.")

# Upload do JSON
caminho = st.text_input("📂 Caminho para o arquivo applicants.json:", "applicants.json")

if caminho:
    try:
        candidatos = carregar_cv_arquivo(caminho)

        ids = [f"{c['id']} - {c['nome']}" for c in candidatos]
        escolha = st.selectbox("📌 Selecione um candidato:", ids)

        if escolha:
            idx = ids.index(escolha)
            candidato = candidatos[idx]

            st.subheader("Currículo Original")
            st.text_area("CV Original", candidato["cv_original"], height=250)

            if st.button("🔁 Melhorar Currículo"):
                with st.spinner("Reescrevendo com IA..."):
                    novo_cv = melhorar_cv(candidato["cv_original"])

                st.subheader("Currículo Melhorado")
                st.text_area("CV Reescrito", novo_cv, height=250)
    except Exception as e:
        st.error(f"Erro ao carregar arquivo: {e}")
