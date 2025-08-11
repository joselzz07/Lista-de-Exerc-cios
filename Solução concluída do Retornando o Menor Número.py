# Retornando o Menor Número
# Este código encontra o menor número em uma lista de números.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]


def retornar_menor_numero(lista):
    if not lista:
        return None
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor
menor_numero = retornar_menor_numero(numeros)
print(f"O menor número da lista é: {menor_numero}")
