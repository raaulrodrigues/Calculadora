def div(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]: # Percorrer a lista e ir atualizando o resultado e dps dividindo pelo prox
            resultado /= num
    except ZeroDivisionError:
        return "Não divida por 0."
    return resultado
