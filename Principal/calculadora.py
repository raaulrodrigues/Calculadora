from Operacoes.soma import soma
from Operacoes.sub import sub
from Operacoes.multi import multi
from Operacoes.div import div
from Principal.numeros import adicionar_valores

def main():
    print("||Calculadora em Py||")

    escolha = int(input("[1]Soma\n"
      "[2]Subtração\n"
      "[3]Multiplicação\n"
      "[4]Divisão\n"
      "Qual operação deseja usar: "))

    numeros = adicionar_valores()

    if escolha == 1:
            print("\nResultado: ", soma(numeros))
    elif escolha == 2:
        print("\nResultado: ", sub(numeros))
    elif escolha == 3:
        print("\nResultado: ", multi(numeros))
    elif escolha == 4:
        print("\nResultado: ", div(numeros))
    else:
        print("\nErro.")

if __name__ == "__main__":
    main()