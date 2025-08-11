# Buscando um Número
# Este código percorre uma lista de números e verifica se um número específico está presente na lista
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def buscando_numero(lista, numero):
    if not lista:
        return False
    for item in lista:
        if item == numero:
            return True
    return False
numero_procurado = 50
encontrado = buscando_numero(numeros, numero_procurado)
if encontrado:
    print(f"O número {numero_procurado} foi encontrado na lista.")
else:
    print(f"O número {numero_procurado} não foi encontrado na lista.")
