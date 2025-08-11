# Contando Ocorrências
# Este código conta quantas vezes cada número apareceu na lista. 
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def contar_ocorrencias(lista):
    if not lista:
        return {}
    ocorrencias = {}
    for numero in lista:
        if numero in ocorrencias:
            ocorrencias[numero] += 1
        else:
            ocorrencias[numero] = 1
    return ocorrencias
ocorrencias = contar_ocorrencias(numeros)
print(f"As ocorrências dos números na lista são: {ocorrencias}")
