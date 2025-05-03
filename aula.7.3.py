def procurar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        linhas_encontradas = []
        for numero_linha, linha in enumerate(linhas, start=1):
            if palavra in linha:
                linhas_encontradas.append((numero_linha, linha.strip()))

        if linhas_encontradas:
            print(f"A palavra '{palavra}' foi encontrada nas seguintes linhas:")
            for numero_linha, conteudo_linha in linhas_encontradas:
                print(f"Linha {numero_linha}: {conteudo_linha}")
        else:
            print(f"A palavra '{palavra}' não foi encontrada no arquivo.")

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def adicionar_nome_idade():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    with open("Lista_Idades.txt", "a") as ficheiro:
        ficheiro.write(f"{nome}\n")
        ficheiro.write(f"{idade}\n")

def buscar_nome_idade():
    nome_procurado = input("Entre com o nome para busca: ")
    with open("Lista_Idades.txt", "r") as ficheiro:
        linhas = ficheiro.readlines()
        for i in range(0, len(linhas), 2):
            nome = linhas[i].strip()
            idade = linhas[i+1].strip()
            if nome == nome_procurado:
                print(f"Idade: {idade}")
                return
        print("Nome não encontrado.")

def menu():
    while True:
        print("Manipulação de Arquivos")
        print("------------------------")
        print("0 - Sair")
        print("1 - Cadastrar Nome e Idade")
        print("2 - Buscar Nome e Idade")
        print("3 - Procurar Palavra em Arquivo")
        opcao = input("Opção desejada: ")

        if opcao == "0":
            print("Obrigado por utilizar o programa")
            break
        elif opcao == "1":
            adicionar_nome_idade()
        elif opcao == "2":
            buscar_nome_idade()
        elif opcao == "3":
            nome_arquivo = input("Digite o nome do arquivo (com extensão): ")
            palavra = input("Digite a palavra a ser procurada: ")
            procurar_palavra(nome_arquivo, palavra)
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso
menu()
