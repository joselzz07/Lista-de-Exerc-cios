# Encontrando o Segundo Maior Número
# Este código encontra o segundo maior número em uma lista de números.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def encontrar_segundo_maior_numero(lista):
    if len(lista) < 2:
        return None
    primeiro_maior = segundo_maior = float('-inf')
    for numero in lista:
        if numero > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = numero
        elif primeiro_maior > numero > segundo_maior:
            segundo_maior = numero
    return segundo_maior

segundo_maior_numero = encontrar_segundo_maior_numero(numeros)
print(f"O segundo maior número da lista é: {segundo_maior_numero}")
