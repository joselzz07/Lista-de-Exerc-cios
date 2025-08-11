# Encontrando o Maior Número   
# Este código encontra o maior número em uma lista de números.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def encontrar_maior_numero(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

maior_numero = encontrar_maior_numero(numeros)
print(f"O maior número da lista é: {maior_numero}")
