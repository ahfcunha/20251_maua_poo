def somar (a,b)
    return a + b

def menu()
    while True:
            print("\Escolha uma opção:")
            print("1. Somar")

            opcao = input("Digite a opção desejada: ")

            elif opcao in ['1']:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
                if opcao == '1':
                    print(f"O resultado da soma é: {somar(a, b)}")

# Chamando a função menu para iniciar o programa
menu()

            
            

