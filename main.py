from fastapi import FastAPI, HTTPException
from datetime import datetime

from classes import AlunoCalcularMedia, AlunoFrequencia, CarroAutonomia, ProdutoDesconto, CategoriaCriar, CategoriaEditar
from src.repositorios import mercado_categoria_repositorio 

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
    pass