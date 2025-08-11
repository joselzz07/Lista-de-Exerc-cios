# Extraindo Nomes de Objetos
# Este código extrai os nomes de objetos de uma lista e os imprime.
nomes_obejtos = ["monitor, teclado, mouse, gabinete, processador, memoria, placa_mae, fonte, cooler, webcam, microfone"]

def extrair_nomes_objetos(lista):
    if not lista:
        return []
    nomes = []
    for objeto in lista:
        nomes.append(objeto)
    return nomes
objetos_extraidos = extrair_nomes_objetos(nomes_obejtos)
print(f"Os nomes dos objetos extraídos são: {objetos_extraidos}")
