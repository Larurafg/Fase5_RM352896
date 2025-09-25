# Melhorador de Currículo com IA Local

Este projeto é um MVP (Produto Mínimo Viável) que utiliza um modelo de linguagem pré-treinado para **melhorar automaticamente o texto de currículos**, rodando 100% **localmente**, sem dependência de APIs externas como OpenAI.

---

## Objetivo

Facilitar o trabalho de consultores de RH e recrutadores, automatizando a **reescrita de currículos** em uma linguagem mais clara, formal e profissional.

---

## Tecnologias Utilizadas

- Python 3.10+
- Hugging Face Transformers (`T5`)
- SentencePiece (necessário para o tokenizer do T5)
- Streamlit (interface simples para uso)
- JSON (para carregar currículos reais)

---

## Como Funciona

- O sistema carrega os currículos do arquivo `applicants.json`;
- Extrai o texto dos CVs (`cv_pt`);
- Usa o modelo **T5-base** (pré-treinado) para gerar uma versão melhorada;
- Exibe os resultados na interface Streamlit para revisão.