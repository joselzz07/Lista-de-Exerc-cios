# Verificando se a Lista está Vazia
# Este código verifica se uma lista está vazia ou não.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def verificar_lista_vazia(lista):
    if not lista:
        return True
    return False
lista_vazia = verificar_lista_vazia(numeros)
if lista_vazia:
    print("A lista está vazia.")
else:
    print("A lista não está vazia.")
