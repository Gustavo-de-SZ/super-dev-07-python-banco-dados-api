from mysql.connector import connect
from src.repositorios import biblioteca_revista_repositorio


def executar_biblioteca_revista():
    # listar_revistas()

    # cadastrar_revista()

    # apagar_revista()

    editar_revista()


def listar_revistas():
    revistas = biblioteca_revista_repositorio.obter_todos()

    for revista in revistas:
        id = revista["id"]

        titulo = revista["titulo"]
        
        edicao = revista["edicao"]

        data_publicacao = revista["data_publicacao"]

        editora = revista["editora"]

        print("ID:", id, "\tTÍTULO:", titulo, "\tEDIÇÂO:", edicao, "\tDATA DE PUBLICAÇÂO:", data_publicacao, "\tEDITORA:", editora)


def cadastrar_revista():
    titulo = input("Digite o título da revista: ")

    edicao = input("Digite a edição da revista: ")

    data_publicacao = input("Digite a data de publicação: ")

    editora = input("Digite a editora da revista: ")

    biblioteca_revista_repositorio.cadastrar(titulo, edicao, data_publicacao, editora)

    print("Revista cadastrada com sucesso com sucesso!")


def apagar_revista():
    listar_revistas()

    id = input("Digite o ID da revista que deseja apagar: ")

    linhas_apagadas = biblioteca_revista_repositorio.apagar(id)

    if linhas_apagadas == 0:
        print("Ocorreu um erro ao tentar apagar a revista.")
    else:
        print("Revista apagada com sucesso!")


def editar_revista():
    listar_revistas()
    id = input("Digite o ID da revista que deseja alterar: ")

    titulo = input("Digite o título da revista: ")

    edicao = input("Digite a edição da revista: ")

    data_publicacao = input("Digite a data de publicação: ")

    editora = input("Digite a editora da revista: ")

    linhas_alteradas = biblioteca_revista_repositorio.editar(id, titulo, edicao, data_publicacao, editora)

    if linhas_alteradas == 0:
        print("Ocorreu um erro ao tentar alterar a revista.")
    else:
        print("Revista alterada com sucesso!")

