from src.repositorios import biblioteca_livro_repositorio

def executar_biblioteca_livros():
    # cadastrar_livro()
    # editar_livro()
    apagar_livro()
    # listar_livros()

    # listar_mangas()
    # editar_manga()
    # apagar_manga()
    # cadastrar_manga()


def cadastrar_livro():
    titulo = input("Digite o título do livro que deseja cadastrar: ")

    quantidade_paginas = input("Digite a quantidade de páginas do livro: ")

    autor = input("Digite o nome do autor do livro: ")

    preco = input("Digite o preço do livro: ")

    isbn = input("Digite o ISBN do livro: ")

    descricao = input("Digite a descrição do livro: ")

    biblioteca_livro_repositorio.cadastrar(titulo, quantidade_paginas, autor, preco, isbn, descricao)

    print(f"Livro {titulo} cadastrado com sucesso!")


def editar_livro():
    listar_livros()

    id = input("Digite o id do livro que deseja editar: ")

    titulo = input("Digite o novo título do livro: ")

    quantidade_paginas = input("Digite a nova quantidade de páginas do livro: ")

    autor = input("Digite o autor do livro: ")

    preco = input("Digite o preço do livro: ")

    isbn = input("Digite o ISBN do livro: ")

    descricao = input("Digite uma breve descrição do livro: ")

    linhas_alteradas = biblioteca_livro_repositorio.editar(id, titulo, quantidade_paginas, autor, preco, isbn, descricao)

    if linhas_alteradas == 0:
        print("Ocorreu um erro ao tentar alterar o livro.")
    else:
        print("Livro alterado com sucesso!")


def apagar_livro():
    listar_livros()

    id = input("Digite o ID que deseja apagar: ")

    linhas_apagadas = biblioteca_livro_repositorio.apagar(id)

    if linhas_apagadas == 0:
        print("Ocorreu um erro ao tentar apagar o livro.")
    else:
        print("Livro apagado com sucesso!")


def listar_livros():
    livros = biblioteca_livro_repositorio.obter_todos()

    for livro in livros:
        id = livro["id"]

        titulo = livro["titulo"]

        quantidade_paginas = livro["quantidade_paginas"]

        autor = livro["autor"]

        preco = livro["preco"]

        isbn = livro["isbn"]

        descricao = livro["descricao"]

        print("ID:", id, "\tTITULO:", titulo, "\tPÁGINAS:", quantidade_paginas, "\tAUTOR:", autor, "\tPRECO:", preco, "\tISBN:", isbn, "\tDESCRIÇÂO:", descricao)



