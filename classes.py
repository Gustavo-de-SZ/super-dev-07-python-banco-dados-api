from datetime import date
from pydantic import BaseModel


class AlunoCalcularMedia(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nome_completo: str


class AlunoFrequencia(BaseModel):
    nome: str
    quantidade_letivos: int
    quantidade_presenca: int


class ProdutoDesconto(BaseModel):
    nome: str
    preco_original: float
    percentual_desconto: float


class CarroAutonomia(BaseModel):
    modelo: str
    consumo_por_litro: float
    quantidade_combustivel: float


class PedidoTotal(BaseModel):
    descricao: str
    quantidade: int
    valor_unitario: float


# ---------------------------------------------------------- Categorias -----------------------------------------------------------------------------------------------


class CategoriaCriar(BaseModel):
    nome: str


class CategoriaEditar(BaseModel):
    nome: str


# ---------------------------------------------------------- Produtos -----------------------------------------------------------------------------------------------


class ProdutoCriar(BaseModel):
    nome: str
    id_categoria: int


class ProdutoEditar(BaseModel):
    nome: str
    id_categoria: int


# ---------------------------------------------------------- Livros -----------------------------------------------------------------------------------------------


class LivroCriar(BaseModel):
    titulo: str
    quantidade_paginas: int
    autor: str
    preco: float
    isbn: str
    descricao: str


class LivroEditar(BaseModel):
    titulo: str
    quantidade_paginas: int
    autor: str
    preco: float
    isbn: str
    descricao: str


# ---------------------------------------------------------- Mangás -----------------------------------------------------------------------------------------------


class MangaCriar(BaseModel):
    nome: str
    volume: int
    autor: str  
    data_lancamento: date


class MangaEditar(BaseModel):
    nome: str
    volume: int
    autor: str  
    data_lancamento: date


# ---------------------------------------------------------- Revistas -----------------------------------------------------------------------------------------------


class RevistaCriar(BaseModel):
    titulo: str
    edicao: int
    data_publicacao: date
    editora: str


class RevistaEditar(BaseModel):
    titulo: str
    edicao: int
    data_publicacao: date
    editora: str

# ---------------------------------------------------------- Clientes -----------------------------------------------------------------------------------------------

class ClienteCriar(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    limite: float


class ClienteEditar(BaseModel):
    data_nascimento: date
    limite: float