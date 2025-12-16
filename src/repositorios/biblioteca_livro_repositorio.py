from src.banco_dados import conectar_biblioteca


def apagar(id: int) -> int:
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"

    dados = (id,)

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_apagadas = cursor.rowcount

    conexao.close()

    cursor.close()

    return linhas_apagadas


def cadastrar(titulo: str, quantidade_paginas: int, autor: str, preco: float, isbn: str, descricao: str):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo, quantidade_paginas, autor, preco, isbn, descricao) VALUE (%s, %s, %s, %s, %s, %s)"

    dados = (titulo, quantidade_paginas, autor, preco, isbn, descricao)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


def editar(id: int, titulo: str, quantidade_paginas: int, autor: str, preco: float, isbn: str, descricao: str) -> int:
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo= %s, quantidade_paginas= %s, autor= %s, preco= %s, isbn= %s, descricao= %s WHERE id = %s"

    dados = (titulo, quantidade_paginas, autor, preco, isbn, descricao, id)

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_alteradas = cursor.rowcount

    cursor.close()

    conexao.close()

    return linhas_alteradas


def obter_todos():
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, quantidade_paginas, autor, preco, isbn, descricao FROM livros"

    cursor.execute(sql)

    registros = cursor.fetchall()

    cursor.close()

    conexao.close()

    livros = []

    for registro in registros:
        livro = {
            "id": registro[0],
            "titulo": registro[1],
            "quantidade_paginas": registro[2],
            "autor": registro[3],
            "preco": registro[4],
            "isbn": registro[5],
            "descricao": registro[6],
        }

        livros.append(livro)
    
    return livros


def obter_por_id(id: int):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, quantidade_paginas, autor, preco, isbn, descricao FROM livros WHERE id= %s"

    dados = (id, )

    cursor.execute(sql, dados)

    registro = cursor.fetchone()

    if not registro:
        return None
    
    return {
        "id": registro[0],
        "titulo": registro[1],
        "quantidade_paginas": registro[2],
        "autor": registro[3],
        "preco": registro[4],
        "isbn": registro[5],
        "descricao": registro[6]
    }