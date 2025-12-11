from mysql.connector import connect

def conectar():
    # Abrir a conexão com o banco de dados
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="admin",
        database="mercado",
    )
    return conexao


def conectar_biblioteca():
    conexao = connect(
        user="root",
        password="admin",
        database="biblioteca",
        host="127.0.0.1",
        port="3306",
    )
    return conexao