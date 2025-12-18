from sqlalchemy import Column, Date, Double, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Categoria(Base):
    __tablename__ = "categorias"


    id = Column(Integer, primary_key=True, autoincrement=True)

    nome = Column(String(255), nullable=False)
    
    produtos = relationship("Produto", back_populates="categoria")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(14), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    limite = Column(Double, nullable=True)

    
class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    
    categoria = relationship("Categoria", back_populates ="produtos")


class Livro(Base):
    __tablename__ = "livros"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo =Column(String(100), nullable=False)
    numero_paginas = Column(int, nullable=False)
    autor = Column(String(100), nullable=False)
    preco = Column(Double, nullable=False)
    isbn = Column(String(100), nullable=False)
    descricao = Column(String(100,), nullable=True)

class Manga(Base):
    __tablename__ = "mangas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome =Column(String(100), nullable=False)
    volume = Column(int, nullable=False)
    autor = Column(String(100), nullable=False)
    data_lancamento = Column(Date, nullable=False)
    
class Revista(Base):
    __tablename__ = "revistas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo =Column(String(100), nullable=False)
    numero_paginas = Column(int, nullable=False)
    edicao = Column(int, nullable=False)
    data_publicacao = Column(Date, nullable=False)
    editora = Column(String(100), nullable=False)
    
  
    