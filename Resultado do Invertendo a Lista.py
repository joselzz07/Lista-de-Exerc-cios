# Invertendo a Lista
# Este código inverte uma lista de números.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def inverter_lista(lista):
    if not lista:
        return []
    lista_invertida = []
    for numero in lista:
        lista_invertida.insert(0, numero)
    return lista_invertida
lista_invertida = inverter_lista(numeros)
print(f"A lista invertida é: {lista_invertida}")
