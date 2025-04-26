def adicionar_nome_idade():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    with open("Lista_Idades.txt", "a") as ficheiro:
        ficheiro.write(f"{nome}\n")
        ficheiro.write(f"{idade}\n")

def menu():
    while True:
        print("Manipulação de Arquivos")
        print("------------------------")
        print("0 - Sair")
        print("1 - Cadastrar")
        opcao = input("Opção desejada: ")

        if opcao == "0":
            print("Obrigado por utilizar o programa")
            break
        elif opcao == "1":
            adicionar_nome_idade()
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso
menu()