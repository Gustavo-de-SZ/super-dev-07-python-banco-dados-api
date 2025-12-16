from src.banco_dados import conectar_biblioteca
from datetime import date


def obter_todos():
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas"

    cursor.execute(sql)

    registros = cursor.fetchall()

    conexao.close()

    cursor.close()

    revistas = []

    for registro in registros:
        revista = {
            "id": registro[0],
            "titulo": registro[1],
            "edicao": registro[2],
            "data_publicacao": registro[3],
            "editora": registro[4],
        }

        revistas.append(revista)

    return revistas


def obter_por_id(id: int):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas WHERE id = %s"

    dados = (id, )

    cursor.execute(sql, dados)

    registro = cursor.fetchone()

    if not registro:
        return None
    
    return {
        "id": registro[0],
        "titulo": registro[1],
        "edicao": registro[2],
        "data_publicacao": registro[3],
        "editora": registro[4],
    }


def cadastrar(titulo: str, edicao: int, data_publicacao: date, editora: str):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "INSERT INTO revistas (titulo, edicao, data_publicacao, editora) VALUES (%s, %s, %s, %s)"

    dados = (titulo, edicao, data_publicacao, editora)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


def apagar(id: int) -> int:
    conexao = conectar_biblioteca()

    sql = "DELETE FROM revistas WHERE id= %s"

    dados = (id, )

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_apagadas = cursor.rowcount

    cursor.close()

    conexao.close()

    return linhas_apagadas


def editar(id: int,titulo: str, edicao: int, data_publicacao: date, editora: str) -> int:
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    linhas_alteradas = cursor.rowcount

    sql = "UPDATE revistas SET titulo= %s, edicao= %s, data_publicacao= %s, editora= %s WHERE id= %s"

    dados = (titulo, edicao, data_publicacao, editora, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    return linhas_alteradas
