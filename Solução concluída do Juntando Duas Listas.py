# Juntando Duas Listas
# Este código junta duas listas: uma com palavras relacionadas à natureza e outra com palavras relacionadas à tecnologia.
# A lista resultante contém todos os elementos das duas listas originais.
natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def juntar_listas(lista1, lista2):
    return lista1 + lista2
juntas = juntar_listas(natureza, tecnologia)
print(f"As listas juntadas são: {juntas}")
