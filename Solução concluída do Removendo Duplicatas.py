# Removendo Duplicatas
# Este código remove números duplicados de uma lista de números inteiros.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def remover_duplicatas(lista):
    if not lista:
        return []
    numeros_unicos = []
    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)
    return numeros_unicos
numeros_sem_duplicatas = remover_duplicatas(numeros)
print(f"Os números sem duplicatas são: {numeros_sem_duplicatas}")
