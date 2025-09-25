# melhorar_cv.py

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Carrega modelo uma vez (evita recarregar em cada uso)
model_name = "t5-small"  # ou "unicamp-dl/ptt5-base-portuguese-vocab"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def melhorar_cv(texto_cv):
    prompt = f"Reescreva este currículo de forma mais clara e atrativa: {texto_cv}"

    # Tokenizar
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)

    # Gerar resposta
    output_ids = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)

    # Decodificar
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text
