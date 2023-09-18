def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

limite_superior = 100 
print("Números primos en el rango del 1 al", limite_superior, ":")
print([num for num in range(2, limite_superior + 1) if es_primo(num)])
