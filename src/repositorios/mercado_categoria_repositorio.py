from src.banco_dados import conectar


def cadastrar(nome: str):
        # Abrir a conexão com o banco de dados
    conexao = conectar()
    # Criando um cursor para poder executar comandos no BD
    cursor = conexao.cursor()

    # Definir qual comando será executado
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome,)

    cursor.execute(sql, dados)

    # Confirmar o comando (concretizar o comando de insert)
    conexao.commit()

    # Fechar a conexão com o banco de dados do cursor
    cursor.close()


def editar(id: int, nome: str):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "UPDATE categorias SET nome= %s WHERE id = %s"

    dados = (nome, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


def apagar(id: int) -> int:
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "DELETE FROM categorias WHERE id = %s"

    dados = (id,)

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    
    cursor.close()

    conexao.close()

    return linhas_afetadas


def obter_todos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome FROM categorias")

    registros = cursor.fetchall()

    cursor.close()

    conexao.close()

    categorias = []

    for registro in registros:
        categoria = {
            "id": registro[0],
            "nome": registro[1]
        }

        categorias.append(categoria)
    
    return categorias
    

