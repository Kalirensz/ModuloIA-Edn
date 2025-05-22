def calculadora():
    print("Calculadora simples Escola da Nuvem :D")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        operacao = input("Escolha a operação (1/2/3/4) ou 'sair': ")

        if operacao.lower() == 'sair':
            print("Até mais!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("ERRO: Essa operação inválida. Tente novamente.\n")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("ERRO: Por favor, digite apenas números válidos.\n")
            continue

        if operacao == '1':
            resultado = num1 + num2
            simbolo = '+'
        elif operacao == '2':
            resultado = num1 - num2
            simbolo = '-'
        elif operacao == '3':
            resultado = num1 * num2
            simbolo = '*'
        elif operacao == '4':
            if num2 == 0:
                print("ERRO: A divisão por zero não é permitida.\n")
                continue
            resultado = num1 / num2
            simbolo = '/'

        print(f"Resultado: {num1} {simbolo} {num2} = {resultado}\n")



calculadora()