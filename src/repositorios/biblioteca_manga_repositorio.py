from src.banco_dados import conectar_biblioteca
from datetime import date

def apagar(id: int) -> int:
    conexao = conectar_biblioteca()

    sql = "DELETE FROM mangas WHERE id = %s"

    dados = (id, )

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_apagadas = cursor.rowcount

    cursor.close()

    conexao.close()

    return linhas_apagadas


def cadastrar(nome: str, volume: int, autor: str, data_lancamento: date):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "INSERT INTO mangas (nome, volume, autor, data_lancamento) VALUES (%s, %s, %s, %s)"

    dados = (nome, volume, autor, data_lancamento)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


def editar(id: int, nome: str, volume: int, autor: str, data_lancamento: date) -> int:
    conexao = conectar_biblioteca()

    dados = (nome, volume, autor, data_lancamento, id)

    sql = "UPDATE mangas SET nome=%s, volume= %s, autor= %s, data_lancamento= %s WHERE id= %s"

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_modificadas = cursor.rowcount

    cursor.close()

    conexao.close()

    return linhas_modificadas


def obter_todos():
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, nome, volume, autor, data_lancamento FROM mangas"
    
    cursor.execute(sql)

    registros = cursor.fetchall()

    conexao.close()

    cursor.close()

    mangas = []
    for registro in registros:
        manga = {
            "id": registro[0],
            "nome": registro[1],
            "volume": registro[2],
            "autor": registro[3],
            "data_lancamento": registro[4],
        }

        mangas.append(manga)

    return mangas


def obter_por_id(id: int):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, nome, volume, autor, data_lancamento FROM mangas WHERE id = %s"

    dados = (id, )

    cursor.execute(sql, dados)

    registro = cursor.fetchone()

    if not registro:
        return None
    
    return {
        "id": registro[0],
        "nome": registro[1],
        "volume": registro[2],
        "autor": registro[3],
        "data_lancamento": registro[4],
    }

