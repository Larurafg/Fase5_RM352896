from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from limpar_cv import limpar_cv

# Carrega modelo
model_name = "unicamp-dl/ptt5-base-paraphraser"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def melhorar_cv(texto_original):
    texto_limpo = limpar_cv(texto_original)
    entrada = f"parafrasear: {texto_limpo}"

    inputs = tokenizer.encode(entrada, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        output = model.generate(
            inputs,
            max_length=512,
            num_beams=4,
            temperature=0.9,
            top_p=0.92,
            top_k=50,
            early_stopping=True
        )

    texto_melhorado = tokenizer.decode(output[0], skip_special_tokens=True)
    return texto_melhorado
