from fastapi import FastAPI, HTTPException
from datetime import datetime

from classes import AlunoCalcularMedia, AlunoFrequencia, CarroAutonomia, ProdutoDesconto, CategoriaCriar, CategoriaEditar, ProdutoEditar, ProdutoCriar, LivrosCriar
from src.repositorios import mercado_categoria_repositorio 
from src.repositorios import mercado_produto_repositorio
from src.repositorios import biblioteca_livro_repositorio

app = FastAPI()


@app.get("/greetings")
def saudacoes():
    return {"mensagem": "Hello World"}


@app.get("/calculadora")
def calculadora(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}


@app.get("/calculadora/expert")
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair"]:
        raise HTTPException(status_code=400, detail="operacao invalida")
    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "N2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }


@app.get("/pessoas/nome-completo")
def concatenar_nome(nome1: str, nome2: str):
    concatenar = nome1 + " " + nome2
    return {"resultado": concatenar}


@app.get("/pessoas/calcular-ano-nascimento")
def calcular_ano_nascimento(idade: int):
    # ano_atual = datetime.now().year
    data_nascimento = datetime.now().year - idade
    return {"ano de nascimento": data_nascimento}


@app.get("/pessoas/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso / (altura * altura)

    if imc < 18.5:
        status = "abaixo"
    elif imc < 25:
        status = "peso normal"
    elif imc < 30:
        status = "sobrepeso"
    else:
        status = "obesidade"

    return {"imc": imc, "status": status}


@app.post("/aluno/calcular-media")
def calcular_media(aluno_dados: AlunoCalcularMedia):
    nota1 = aluno_dados.nota1
    nota2 = aluno_dados.nota2
    nota3 = aluno_dados.nota3
    media = (nota1 + nota2 + nota3) / 3
    return {
        "Media": media,
        "nome_completo": aluno_dados.nome_completo
    }
    
    
@app.post ("/aluno/calcular-frequencia")
def calcular_frequencia(aluno_frequencia: AlunoFrequencia):
    quantidade_letivos = aluno_frequencia.quantidade_letivos
    quantidade_presencas = aluno_frequencia.quantidade_presencas
    frequencia = (quantidade_presencas * 100) / quantidade_letivos
    return {
        "nome_completo": aluno_frequencia.nome_completo,
        "frequencia": frequencia
    }    
    

@app.post ("/produto/calcular-desconto")
def calcular_desconto(produto_desconto: ProdutoDesconto):
    preco_original = produto_desconto.preco_original
    percentual_desconto = produto_desconto.percentual_desconto
    valor_desconto = (preco_original * percentual_desconto) / 100
    preco_final = preco_original - valor_desconto
    return {
        "nome": produto_desconto.nome,
        "desconto": valor_desconto,
        "preco_final": preco_final
    }
    
@app.post ("/carro/calcular-autonomia")
def calcular_autonomia(calcular_autonomia: CarroAutonomia):
    consumo_por_litro = calcular_autonomia.consumo_por_litro
    quantidade_combustivel = calcular_autonomia.quantidade_combustivel
    autonomia = consumo_por_litro * quantidade_combustivel
    return {
        "modelo": calcular_autonomia.modelo,
        "autonomia": autonomia
    }


@app.get("/api/v1/categorias")
def listar_categorias():
    categorias = mercado_categoria_repositorio.obter_todos()
    return categorias

@app.post("/api/v1/categorias")
def cadastrar_categorias(categoria: CategoriaCriar):
    mercado_categoria_repositorio.cadastrar(categoria.nome)
    return {
        "status": "ok"
    }

@app.delete("/api/v1/categoria")
def apagar_categoria():
    def apagar_categoria(id: int):
        linhas_afetadas = mercado_categoria_repositorio.apagar(id)
        
        if linhas_afetadas == 1:
            return{
                "status": "ok"
        }
        else: 
            raise HTTPException(status_code=404, detail="categoria não encontrada")
        


@app.put("/api/v1/categorias")
def alterar_categoria(id: int, categoria: CategoriaEditar):
    linhas_afetadas = mercado_categoria_repositorio.editar(id, categoria.nome)
    if linhas_afetadas == 1:
        return{
            "status": "ok"
        }
    else: 
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    

@app.get("/api/v1/categorias/{id}")
def buscar_categoria_por_id(id: int):
    categoria = mercado_categoria_repositorio.obter_por_id(id)
    if categoria is None:
        raise HTTPException(status_code=404, detail=("categoria não encontrada"))
    return categoria


@app.get("/api/v1/produtos")
def listar_todos_produtos():
    produtos = mercado_produto_repositorio.obter_todos()
    return produtos


@app.delete("/api/v1/produtos/{id}")
def apagar_produto(id: int):
    linhas_afetadas = mercado_produto_repositorio.apagar(id)
    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="produto n encontrado")
    return{"status": "ok"}


@app.put("/api/v1/produtos/{id}")
def alterar_produto(id: int, produto: ProdutoEditar):
    linhas_afetadas = mercado_produto_repositorio.editar(id, produto.nome, produto.id_categoria)
    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="produto não encontrado")
    return {"status": "ok"}

@app.post("/api/v1/produtos")
def cadastrar_produto(produto: ProdutoCriar):
    mercado_categoria_repositorio.cadastrar(produto.nome, produto.id_categoria)
    return{"status": "ok"}

@app.get("/api/v1/produtos/{id}")
def obter_produto_por_id(id: int):
    produto = mercado_produto_repositorio.obter_por_id(id)
    if produto is None:
        raise HTTPException(status_code=404, detail="nao encontrado")
    return produto



@app.get("/api/v1/livros")
def listar_livros():
    livros = biblioteca_livro_repositorio.obter_todos()
    return livros


@app.get("api/v1/livros/{id}")
def obter_livro_por_id(id: int):
    livro = biblioteca_livro_repositorio.obter_por_id()
    

@app.delete("/api/v1/livros/{id}")
def apagar_livro():
    linhas_afetadas = biblioteca_livro_repositorio.apagar(id)
    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="n foi encontrado")
    return{"status:" "ok"}

@app.post("/api/v1/livros")
def cadastrar_livro(livros: LivrosCriar):
    biblioteca_livro_repositorio.cadastrar(livros.nome)
    return{"status": "Ok"}

@app.put("/api/v1/livros/{id}")
def alterar_livro():
    linhas_afetadas = biblioteca_livro_repositorio.editar(id)
    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail=("deu bostwal ke"))
    return {"status": "Ok"}