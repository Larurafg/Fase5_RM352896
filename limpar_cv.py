def limpar_cv(texto):
    texto = texto.replace('\n', ' ').replace('\r', ' ')
    texto = ' '.join(texto.split())
    return texto.strip()
