from src.banco_dados import conectar_biblioteca
from datetime import date
from sqlalchemy.orm import Session
from src.database.models import Revista


def obter_todos(db: Session):
    revistas = db.query(Revista).all()
    return revistas


def obter_por_id(db: Session, id: int):
    revista = db.query(Revista).filter(Revista.id == id).first()
    return revista


def cadastrar(db: Session, titulo: str, edicao: int, data_publicacao: date, editora: str):
    revista = Revista(
        titulo=titulo,
        edicao=edicao,
        data_publicacao=data_publicacao,
        editora=editora
    )

    db.add(revista)
    db.commit()
    db.refresh(revista)
    return revista

def apagar(db: Session, id: int) -> int:
    revista = db.query(Revista).filter(Revista.id == id).first()
    if not revista:
        return 0
    
    db.delete(revista)
    db.commit()
    return 1


def editar(db: Session, id: int,titulo: str, edicao: int, data_publicacao: date, editora: str) -> int:
    revista = db.query(Revista).filter(Revista.id == id).first()
    if not revista:
        return 0
    titulo=titulo,
    edicao=edicao,
    data_publicacao=data_publicacao,
    editora=editora
    db.commit()
    return revista
# from src.banco_dados import conectar_biblioteca
# from datetime import date


# def obter_todos():
#     conexao = conectar_biblioteca()

#     cursor = conexao.cursor()

#     sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas"

#     cursor.execute(sql)

#     registros = cursor.fetchall()

#     conexao.close()

#     cursor.close()

#     revistas = []

#     for registro in registros:
#         revista = {
#             "id": registro[0],
#             "titulo": registro[1],
#             "edicao": registro[2],
#             "data_publicacao": registro[3],
#             "editora": registro[4],
#         }

#         revistas.append(revista)

#     return revistas


# def obter_por_id(id: int):
#     conexao = conectar_biblioteca()

#     cursor = conexao.cursor()

#     sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas WHERE id = %s"

#     dados = (id, )

#     cursor.execute(sql, dados)

#     registro = cursor.fetchone()

#     if not registro:
#         return None
    
#     return {
#         "id": registro[0],
#         "titulo": registro[1],
#         "edicao": registro[2],
#         "data_publicacao": registro[3],
#         "editora": registro[4],
#     }


# def cadastrar(titulo: str, edicao: int, data_publicacao: date, editora: str):
#     conexao = conectar_biblioteca()

#     cursor = conexao.cursor()

#     sql = "INSERT INTO revistas (titulo, edicao, data_publicacao, editora) VALUES (%s, %s, %s, %s)"

#     dados = (titulo, edicao, data_publicacao, editora)

#     cursor.execute(sql, dados)

#     conexao.commit()

#     cursor.close()

#     conexao.close()


# def apagar(id: int) -> int:
#     conexao = conectar_biblioteca()

#     sql = "DELETE FROM revistas WHERE id= %s"

#     dados = (id, )

#     cursor = conexao.cursor()

#     cursor.execute(sql, dados)

#     conexao.commit()

#     linhas_apagadas = cursor.rowcount

#     cursor.close()

#     conexao.close()

#     return linhas_apagadas


# def editar(id: int,titulo: str, edicao: int, data_publicacao: date, editora: str) -> int:
#     conexao = conectar_biblioteca()

#     cursor = conexao.cursor()

#     linhas_alteradas = cursor.rowcount

#     sql = "UPDATE revistas SET titulo= %s, edicao= %s, data_publicacao= %s, editora= %s WHERE id= %s"

#     dados = (titulo, edicao, data_publicacao, editora, id)

#     cursor.execute(sql, dados)

#     conexao.commit()

#     cursor.close()

#     conexao.close()

#     return linhas_alteradas
