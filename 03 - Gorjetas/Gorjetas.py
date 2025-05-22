def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def menu():
    print("\n====== Calcular Gorjetas ==========")
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
        
        valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        print(f"\nA gorjeta é: R$ {valor_gorjeta:.2f}")
    
    except ValueError:
        print(" ERRO: Entrada inválida. Por favor, digite números.")

menu()
