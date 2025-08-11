# Somando os Valores da Lista
# Este código percorre uma lista de números e soma todos os valores.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def somar_valores(lista):
    if not lista:
        return 0
    soma = 0
    for numero in lista:
        soma += numero
    return soma
soma_total = somar_valores(numeros)
print(f"A soma dos valores da lista é: {soma_total}")
