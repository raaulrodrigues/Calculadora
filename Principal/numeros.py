def adicionar_valores():
    numeros = []
    while True:
        num = input("Digite o número que deseja utilizar ou utilize X para parar: ")
        if num.lower() == "x":
            break
        try:
            numeros.append(float(num))
        except ValueError:
            print("Utilize apenas números, por favor.")
    return numeros