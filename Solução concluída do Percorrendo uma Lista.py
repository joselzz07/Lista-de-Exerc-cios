# Percorrendo uma Lista
# Este código percorre uma lista de números e imprime cada número.
numero = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def pecorrer_lista(lista):
    if not lista:
        return None
    for numero in lista:
        print(numero)

pecorrer_lista(numero)
