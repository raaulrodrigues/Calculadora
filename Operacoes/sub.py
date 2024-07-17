def sub(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado