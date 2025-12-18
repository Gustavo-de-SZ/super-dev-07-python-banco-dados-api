from src.banco_dados import conectar
from sqlalchemy.orm import Session, contains_eager

from src.database.models import Produto

def cadastrar(nome: str, id_categoria: int):
    produto = Produto(nome=nome, id_categoria=id_categoria)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "INSERT INTO produtos (nome, id_categoria) VALUES (%s, %s)"
    # dados = (nome, id_categoria)
    # cursor.execute(sql, dados)
    # conexao.commit()
    # cursor.close()
    # conexao.close()

def editar(db: Session, id: int, nome: str, id_categoria: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return 0
    
    produto.nome = nome
    produto.id_categoria = id_categoria
    
    db.commit()
    db.refresh(produto)
    return 1
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "UPDATE produtos SET nome = %s, id_categoria = %s WHERE id = %s"
    # dados = (nome, id_categoria, id)
    # cursor.execute(sql, dados)
    # conexao.commit()
    # linhas_afetadas = cursor.rowcount
    # cursor.close()
    # conexao.close()
    # return linhas_afetadas


def apagar(db: Session, id: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return 0
    db.delete(produto)
    db.commit()
    return 1
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "DELETE FROM produtos WHERE id = %s"
    # dados = (id,)
    # cursor.execute(sql, dados)
    # conexao.commit()
    # linhas_afetadas = cursor.rowcount
    # cursor.close()
    # conexao.close()
    # return linhas_afetadas


def obter_todos(db: Session):
    produtos = db.query(Produto).options(contains_eager(Produto.categoria)).all()
    return produtos
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = """select
	# produtos.id,
	# produtos.nome,
	# categorias.id,
	# categorias.nome
	# from produtos
	# inner join categorias on (produtos.id_categoria = categorias.id)"""
    # cursor.execute(sql)
    # registros = cursor.fetchall()
    # produtos = []
    # for registro in registros:
    #     produto = {
    #         "id": registro[0],
    #         "nome": registro[1],
    #         "categoria": {
    #             "id": registro[2],
    #             "nome": registro[3]
    #         }
    #     }
    #     produtos.append(produto)
    # return produtos


def obter_por_id(db: Session, id: int):
    produto = db.query(Produto)\
        .options(contains_eager(Produto.categoria))\
        .filter(Produto.id == id)\
        .first()
    
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = """select
    #     produtos.id,
    #     produtos.nome,
    #     categorias.id,
    #     categorias.nome
    # from produtos
    # inner join categorias on (produtos.id_categoria = categorias.id)
    # where produtos.id = %s"""
    # cursor.execute(sql, (id,))
    # registro = cursor.fetchone()
    # cursor.close()
    # conexao.close()

    # if registro is None:
    #     return None

