def somar (a,b)
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero!"

def menu()
    while True:
            print("\Escolha uma opção:")
            print("1. Somar")
            print("2. Subtrair")
            print("3. Multiplicar")
            print("4. Dividir")

            opcao = input("Digite a opção desejada: ")

            elif opcao in ['1','2','3','4']:
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
                elif opcao == '3':
                    print(f"O resultado da multiplicação é: {multiplicar(a, b)}")
                elif opcao == '4':
                    print(f"O resultado da divisão é: {dividir(a, b)}")



            
            

