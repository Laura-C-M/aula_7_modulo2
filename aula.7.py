#def procurar_palavra(nome_arquivo, palavra):
#    try:
#        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
#            conteudo = arquivo.read()
#            if palavra in conteudo:
#                print(f"A palavra '{palavra}' foi encontrada no arquivo.")
#            else:
#                print(f"A palavra '{palavra}' não foi encontrada no arquivo.")
#    except FileNotFoundError:
#        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
#    except Exception as e:
#        print(f"Ocorreu um erro: {e}")

# Solicitar ao usuário o nome do arquivo e a palavra a ser procurada
#nome_arquivo = input("Digite o nome do arquivo (com extensão .txt): ")
#palavra = input("Digite a palavra que deseja procurar: ")

#procurar_palavra(nome_arquivo, palavra)


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


# Exemplo de uso
nome_arquivo = input("Digite o nome do arquivo (com extensão): ")
palavra = input("Digite a palavra a ser procurada: ")
procurar_palavra(nome_arquivo, palavra)


