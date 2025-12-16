from sqlalchemy import Column, Date, Double, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

# Temos uma classe chamada Categoria que herda as propriedades e métodos da Base
class Categoria(Base):
    __tablename__ = "categorias"

    # Coluna da PK id do tipo inteiro auto incrementável
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Coluna do nome que n permite nulo
    nome = Column(String(255), nullable=False)


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(14), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    limite = Column(Double, nullable=True)

    # nullable=False campo é obrigatório
    # nullable=True campo não é obrigatório