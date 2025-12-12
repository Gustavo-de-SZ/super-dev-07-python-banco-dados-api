from pydantic import BaseModel


class AlunoCalcularMedia(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nome_completo: str
    

class AlunoFrequencia(BaseModel):
    nome_completo: str
    quantidade_letivos: int
    quantidade_presencas: int
    
class ProdutoDesconto(BaseModel):
    nome: str
    preco_original: float
    percentual_desconto: float
    
class CarroAutonomia(BaseModel):
    modelo: str
    consumo_por_litro: int
    quantidade_combustivel: int
    
class CategoriaCriar(BaseModel):
    nome: str


class CategoriaEditar(BaseModel):
    nome: str


class ProdutoCriar(BaseModel):
    nome: str
    id_categoria: int
    
    
class ProdutoEditar(BaseModel):
    nome: str
    id_categoria: int
    
    
class LivrosCriar(BaseModel):
    nome: str
    