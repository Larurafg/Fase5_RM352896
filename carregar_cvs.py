# carregar_cvs.py

import json

def carregar_cv_arquivo(caminho_arquivo):
    with open(caminho_arquivo, encoding='utf-8') as f:
        data = json.load(f)

    cvs = []
    for candidato_id, candidato in data.items():
        nome = candidato.get("infos_basicas", {}).get("nome", "")
        email = candidato.get("infos_basicas", {}).get("email", "")
        cv_pt = candidato.get("cv_pt", "").strip()

        if cv_pt:
            cvs.append({
                "id": candidato_id,
                "nome": nome,
                "email": email,
                "cv_original": cv_pt
            })

    return cvs
