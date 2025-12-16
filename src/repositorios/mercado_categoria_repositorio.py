from sqlalchemy.orm import Session

from src.database.models import Categoria


def cadastrar(db: Session, nome: str):
    categoria = Categoria(nome=nome)
    db.add(categoria) # INSERT INTO categorias (nome) VALUES (%s)
    db.commit() # Concretização do insert no banco
    db.refresh(categoria) # Atribuir para a categoria o ID que foi gerado no DB
    return categoria


def editar(db: Session, id: int, nome: str):
    # Busaca a categoria pelo id (retorna a primeira categoria encontrada ou None)
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    # Senão encontrou a categoria
    if not categoria:
        return 0 # retornamos 0 indicando que nada foi alterado
    categoria.nome = nome # Atualiza o nome do objeto em memória (SQLAlchemy detecta a mudança)
    db.commit() # Persiste a alteração no banco
    return 1 # Retorna 1 indicando sucesso na edição


def apagar(db: Session, id: int) -> int:
    # Busaca a categoria pelo id (retorna a primeira categoria encontrada ou None)
    categoria = db.query(Categoria).filter(Categoria.id == id).first()

    # Senão encontrou a categoria
    if not categoria:
        return 0 # retornamos 0 indicando que nada foi alterado
    # Marca o registro para remoção de sessão
    db.delete(categoria)
    db.commit() # Confirma a transação e remove a categoria do banco
    return 1 # Retorna 1 indicando sucesso na remoção


def obter_todos(db: Session):
    categorias = db.query(Categoria).all()
    return categorias


def obter_por_id(db: Session, id: int):
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    return categoria
