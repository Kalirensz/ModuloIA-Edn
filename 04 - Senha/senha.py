def validar_senha(senha):

    if len(senha) < 8:
        return False

    if not any(char.isdigit() for char in senha):
        return False

    if not any(char.isalpha() for char in senha):
        return False
    return True

while True:
    senha = input("Digite uma senha ou 'sair' para encerrar: ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    if validar_senha(senha):
        print("Senha válida e forte!")
        break
    else:
        print("Senha fraca! A senha deve ter pelo menos 8 caracteres, conter pelo menos um número e uma letra.")