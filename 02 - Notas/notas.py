#Crie um programa que permita a um professor registrar 
#as notas de uma turma. 
#O programa deve continuar solicitando notas até que o professor digite 'fim'. 
#Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
#No final, deve exibir a média da turma.



notas = [] 

def notas_lancar():
    while True:
        entrada = input("Digite a nota 'sair' para encerrar:")

        if entrada.lower() == 'sair':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                print("Nota adicionada com sucesso!")
            else:
                print("ERROR: Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("ERROR: Entrada inválida. Digite um número ou 'Sair' para voltar ao menu.")
        
def ver_media():
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média total da turma: {media:.2f}")
    else:
        print("Nenhuma nota registrada ainda.")

def listar_notas():
    if notas:
        print("Notas registradas:")
        for i, nota in enumerate(notas, start=1):
            print(f"{i} nota: {nota}")
    else:
        print("Nenhuma nota registrada ainda.")

def menu():
    while True:
        print("\n=== Notas Escola da Nuvem  ===")
        print("1 - Adicionar notas")
        print("2 - Ver média da turma")
        print("3 - Listar todas as notas")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            notas_lancar()
        elif escolha == '2':
            ver_media()
        elif escolha == '3':
            listar_notas()
        elif escolha == '4':
            print("Programa encerrado, até mais!.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()