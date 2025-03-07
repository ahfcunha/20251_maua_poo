def somar (a,b)
    return a + b

def subtrair(a, b):
    return a - b

def menu()
    while True:
            print("\Escolha uma opção:")
            print("1. Somar")
            print("2. Subtrair")

            opcao = input("Digite a opção desejada: ")

            elif opcao in ['1','2']:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

                if opcao == '1':
                    print(f"O resultado da soma é: {somar(a, b)}")
                elif opcao == '2':
                    print(f"O resultado da subtração é: {subtrair(a, b)}")



            
            

