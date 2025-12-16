from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime

from classes import AlunoCalcularMedia, AlunoFrequencia, CarroAutonomia, CategoriaCriar, CategoriaEditar, ClienteCriar, ClienteEditar, LivroCriar, LivroEditar, MangaCriar, MangaEditar, PedidoTotal, ProdutoCriar, ProdutoDesconto, ProdutoEditar, RevistaCriar, RevistaEditar
from src.database.conexao import get_db
from src.repositorios import biblioteca_livro_repositorio, biblioteca_manga_repositorio, biblioteca_revista_repositorio, mercado_categoria_repositorio, mercado_cliente_repositorio, mercado_produto_repositorio

from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/greetings", tags=["Saudações"])
def saudacoes():
    return {"mensagem": "Hello World"}


@app.get("/calculadora", tags=["Calculadora"])
def calcular(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}


# (query) vai depois da ? ex.: /calculadora/expert?operacao=somar&n1=100&n2=200
@app.get("/calculadora/expert", tags=["Calculadora"])
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair", "dividir", "multiplicar"]:
        raise HTTPException(
            status_code=400,
            detail="Operação inválida. Opcões disponíveis [somar, subtrair, dividir, multiplicar]"
        )
    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "dividir":
        resultado = n1 / n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "multiplicar":
        resultado = n1 * n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    

@app.get("/pessoa/nome-completo", tags=["Pessoas"])
def concatenar_nome(nome: str, sobrenome: str):
    nome_completo =  nome + " " + sobrenome
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "nomeCompleto": nome_completo
    }


# Criar um endpoint 'pessoa/calcular-ano-nascimento' para calcular o ano de nascimento
#   Query param: idade
#   Calcular o ano de nascimento
#   Retornar {"anoNascimento": 1991}


@app.get("/pessoa/calcular-ano-nascimento", tags=["Pessoas"])
def calcular_ano_nascimento(idade: int):
    data_atual = datetime.now()

    ano_atual = data_atual.year

    ano_nascimento = ano_atual - idade
    return {
        "idade": idade,
        "anoNascimento": ano_nascimento
    }


# Criar um endpoint 'pessoa/imc' para calcular o imc da pessoa
#   Query param: altura, peso
#   Calcular o imc
#   Retornar {"imc": 20.29}
# Alterar o endpoint 'pessoa/imc' para retornar o status do imc
#   Descobrir o status do IMC
#   Retornar {"imc"': 20.29, "Obesidade III"}


@app.get("/pessoa/imc", tags=["Pessoas"])
def calcular_imc(altura: float, peso: float):
    imc = peso / (altura * altura)
    if imc < 18.5:
        status = "Magreza"
    elif imc >= 18.5 and imc <= 24.9:
        status = "Normal"
    elif imc >= 25.0 and imc <= 29.9:
        status = "Sobrepeso"
    elif imc >= 30.0 and imc <= 39.9:
        status = "Obesidade"
    elif imc >= 40.0:
        status = "Obesidade Grave"

    return {
        "imc": f"""{imc:.2f}""",
        "status": status
    }


@app.post("/aluno/calcular-media", tags=["Alunos"])
def calcular_media(alunos_dados: AlunoCalcularMedia):
    nota1 = alunos_dados.nota1

    nota2 = alunos_dados.nota2

    nota3 = alunos_dados.nota3

    media = (nota1 + nota2 + nota3) / 3

    return {
        "media": media,
        "nome_completo": alunos_dados.nome_completo
    }


# Ex.1 Criar um endpoint do tipo POST /aluno/calcular-frequencia
# Criar uma classe AlunoFrequencia
#   nome
#   quantidade_letivos
#   quantidade_presencas
# Payload:
#   nome do aluno
#   quantidade letivos
#   quantidade presencas
#   
#   qtd letivos     100
#   qtd presencas   
#   (qtd presencas * 100) / qtd letivos
@app.post("/aluno/calcular-frequencia", tags=["Alunos"])
def calcular_frequencia(aluno_dados: AlunoFrequencia):
    presenca = aluno_dados.quantidade_presenca

    letivos = aluno_dados.quantidade_letivos

    frequencia = (presenca * 100) / letivos


    return {
        "nome do aluno": aluno_dados.nome,
        "quantidade letivos": aluno_dados.quantidade_letivos,
        "quantidade presenca": aluno_dados.quantidade_presenca,
        "frequncia": frequencia
    }


# Ex.2 Criar um endpoint do tipo POST /produto/calcular-desconto
# Criar uma classe ProdutoDesconto
#   nome
#   preco_original
#   percentual_desconto
# Payload:
#   nome do produto
#   preço original
#   percentual de desconto (0 a 100)
# Fórmulas:
#   valor_desconto = (preco_original * percentual_desconto) / 100
#   preco_final = preco_original - valor_desconto
@app.post("/produto/calcular-desconto", tags=["Atividades"])
def calcular_desconto(produto_dados: ProdutoDesconto):
    preco_original = produto_dados.preco_original

    percentual_desconto = produto_dados.percentual_desconto

    valor_desconto = (preco_original * percentual_desconto) / 100
    
    preco_final = preco_original - valor_desconto

    return {
        "nome do produto": produto_dados.nome,
        "preco original": preco_original,
        "percentual de desconto(0 a 100)": percentual_desconto,
        "valor do desconto": valor_desconto,
        "preco final": preco_final
    }


# Ex.3 Criar um endpoint do tipo POST /carro/calcular-autonomia
# Criar uma classe CarroAutonomia
#   modelo
#   consumo_por_litro
#   quantidade_combustivel
# Payload:
#   modelo do carro
#   consumo por litro (km/l)
#   quantidade de combustível no tanque (litros)
#
# Fórmula:
#   autonomia = consumo_por_litro * quantidade_combustivel
@app.post("/carro/calcular-autonomia", tags=["Atividades"])
def calcular_autonomia(carro_dados: CarroAutonomia):
    consumo_litro = carro_dados.consumo_por_litro

    quantidade_combustivel = carro_dados.quantidade_combustivel

    autonomia = consumo_litro * quantidade_combustivel

    return {
        "modelo": carro_dados.modelo,
        "consumo por litro(KM/l)": consumo_litro,
        "quantidade de combustivel no tanque (litros)": quantidade_combustivel,
        "autonomia do carro": autonomia
    }


# Ex.4 Criar um endpoint do tipo POST /pedido/calcular-total
# Criar uma classe PedidoTotal
#   descricao
#   quantidade
#   valor_unitario
# Payload:
#   descrição do pedido
#   quantidade de itens
#   valor unitário
#
# Fórmulas:
#   subtotal = quantidade * valor_unitario
#   taxa = subtotal * 0.05  (5% de taxa de serviço)
#   total = subtotal + taxa


@app.post("/pedido/calcular-total", tags=["Atividades"])
def calcular_pedido(pedido_dados: PedidoTotal):
    quantidade = pedido_dados.quantidade

    valor_unitario = pedido_dados.valor_unitario

    subtotal = quantidade * valor_unitario

    taxa = subtotal * 0.05

    total = subtotal +  taxa

    return {
        "descrição do pedido": pedido_dados.descricao,
        "quantidade de itens": quantidade,
        "valor unitário": valor_unitario,
        "subtotal": subtotal,
        "taxa adicional": taxa,
        "total final": total
    }


@app.get("/api/v1/categorias", tags=["Categorias"])
def listar_categorias(db: Session = Depends(get_db)):
    categorias = mercado_categoria_repositorio.obter_todos(db)
    return categorias


@app.post("/api/v1/categorias", tags=["Categorias"])
def cadastrar_categoria(categoria: CategoriaCriar, db: Session = Depends(get_db)):
    mercado_categoria_repositorio.cadastrar(db, categoria.nome)
    return {
        "status": "OK"
    }


@app.delete("/api/v1/categorias/{id}", tags=["Categorias"])
def apagar_categoria(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = mercado_categoria_repositorio.apagar(db, id)

    if linhas_afetadas == 1:
        return {
            "status": "OK"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    

@app.put("/api/v1/categorias/{id}", tags=["Categorias"])
def alterar_categoria(id: int, categoria: CategoriaEditar, db: Session = Depends(get_db)):
    linhas_afetadas = mercado_categoria_repositorio.editar(db, id, categoria.nome)
    if linhas_afetadas == 1:
        return {
            "status": "OK"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    

@app.get("/api/v1/categorias/{id}", tags=["Categorias"])
def buscar_categoria_por_id(id: int, db : Session = Depends(get_db)):
    categoria = mercado_categoria_repositorio.obter_por_id(db, id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    return categoria


# ---------------------------------------------------------- Produtos -----------------------------------------------------------------------------------------------


@app.get("/api/v1/produtos", tags=["Produtos"])
def listar_todos_produtos():
    produtos = mercado_produto_repositorio.obter_todos()
    return produtos


@app.post("/api/v1/produtos", tags=["Produtos"])
def cadastrar_produto(produto: ProdutoCriar):
    mercado_produto_repositorio.cadastrar(produto.nome, produto.id_categoria)
    return {
        "status": "OK"
    }


@app.put("/api/v1/produtos/{id}", tags=["Produtos"])
def alterar_produto(id: int, produto: ProdutoEditar):
    linhas_afetadas = mercado_produto_repositorio.editar(id, produto.nome, produto.id_categoria)

    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return {
        "status": "OK"
    }


@app.delete("/api/v1/produtos/{id}", tags=["Produtos"])
def apagar_produto(id: int):
    linhas_afetadas = mercado_produto_repositorio.apagar(id)

    if linhas_afetadas != 1:
        raise HTTPException(status_code= 404, detail="Produto não encontrado")
    
    return {
        "status": "OK"
    }


@app.get("/api/v1/produtos/{id}", tags=["Produtos"])
def obter_produto_por_id(id: int):
    produto = mercado_produto_repositorio.obter_por_id(id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto


# ---------------------------------------------------------- Livros -----------------------------------------------------------------------------------------------


@app.get("/api/v1/livros", tags=["Livros"])
def listar_livros():
    livros = biblioteca_livro_repositorio.obter_todos()
    return livros


@app.get("/api/v1/livros/{id}", tags=["Livros"])
def obter_livro_por_id(id: int):
    livro = biblioteca_livro_repositorio.obter_por_id(id)

    if livro is None:
        raise HTTPException(status_code= 404, detail="Livro não encontrado")
    
    return livro


@app.post("/api/v1/livros", tags=["Livros"])
def cadastrar_livro(livro: LivroCriar):
    biblioteca_livro_repositorio.cadastrar(livro.titulo, livro.quantidade_paginas, livro.autor, livro.preco, livro.isbn, livro.descricao)

    return {
        "status": "OK"
    }


@app.put("/api/v1/livros/{id}", tags=["Livros"])
def alterar_livro(id: int, livro: LivroEditar):
    linhas_alteradas = biblioteca_livro_repositorio.editar(id, livro.titulo, livro.quantidade_paginas, livro.autor, livro.preco, livro.isbn, livro.descricao)

    if linhas_alteradas != 1:
        raise HTTPException(status_code= 404, detail="Livro não encontrado")
    

    return {
        "status": "OK"
    }


@app.delete("/api/v1/livros/{id}", tags=["Livros"])
def apagar_livro(id: int):
    linhas_apagadas = biblioteca_livro_repositorio.apagar(id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code= 404, detail="Livro não encontrado")
    

    return {
        "status": "OK"
    }


# ---------------------------------------------------------- Mangás -----------------------------------------------------------------------------------------------


@app.get("/api/v1/mangas", tags=["Mangás"])
def listar_mangas():
    mangas = biblioteca_manga_repositorio.obter_todos()

    return mangas


@app.get("/api/v1/mangas/{id}", tags=["Mangás"])
def obter_manga_por_id(id: int):
    manga = biblioteca_manga_repositorio.obter_por_id(id)

    if manga is None:
        raise HTTPException(status_code= 404, detail="Mangá não encontrado")
    

    return manga


@app.post("/api/v1/mangas", tags=["Mangás"])
def cadastrar_manga(manga: MangaCriar):
    biblioteca_manga_repositorio.cadastrar(manga.nome, manga.volume, manga.autor, manga.data_lancamento)

    return {
        "status": "OK"
    }


@app.put("/api/v1/mangas/{id}", tags=["Mangás"])
def editar_manga(id: int, manga: MangaEditar):
    linhas_alteradas = biblioteca_manga_repositorio.editar(id, manga.nome, manga.volume, manga.autor, manga.data_lancamento)

    if linhas_alteradas != 1:
        raise HTTPException(status_code= 404, detail="Mangá não encontrado")
    
    return {
        "status": "OK"
    }


url_manga_com_id = "/api/v1/mangas/{id}"
@app.delete(url_manga_com_id, tags=["Mangás"])
def apagar_manga(id: int):
    linhas_apagadas = biblioteca_manga_repositorio.apagar(id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code= 404, detail="Mangá não encontrado")
    
    return {
        "status": "OK"
    }


# ---------------------------------------------------------- Revistas -----------------------------------------------------------------------------------------------

url_revista = "/api/v1/revistas"


url_revista_com_id = "/api/v1/revistas/{id}"


@app.get(url_revista, tags=["Revistas"])
def listar_revistas():
    revistas = biblioteca_revista_repositorio.obter_todos()

    return revistas


@app.get(url_revista_com_id, tags=["Revistas"])
def obter_revista_por_id(id: int):
    revista = biblioteca_revista_repositorio.obter_por_id(id)

    if revista is None:
        raise HTTPException(status_code= 404, detail="Revista não encontrada")
    
    return revista


@app.post(url_revista, tags=["Revistas"])
def cadastrar_revista(revista: RevistaCriar):
    biblioteca_revista_repositorio.cadastrar(revista.titulo, revista.edicao, revista.data_publicacao, revista.editora)

    return {
        "status": "OK"
    }


@app.put(url_revista_com_id, tags=["Revistas"])
def editar_revista(id: int, revista: RevistaEditar):
    linhas_alteradas = biblioteca_revista_repositorio.editar(id, revista.titulo, revista.edicao, revista.data_publicacao, revista.editora)

    if linhas_alteradas != 1:
        raise HTTPException(status_code= 404, detail="Revista não encontrada")
    

    return {
        "status": "OK"
    }


@app.delete(url_revista_com_id, tags=["Revistas"])
def apagar_revista(id: int):
    linhas_apagadas = biblioteca_revista_repositorio.apagar(id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code= 404, detail="Revista não encontrada")
    

    return {
        "status": "OK"
    }


# ---------------------------------------------------------- Clientes -----------------------------------------------------------------------------------------------


@app.post("/api/v1/clientes", tags=["Clientes"])
def cadastrar_clientes(cliente: ClienteCriar, db: Session = Depends(get_db)):
    cliente = mercado_cliente_repositorio.cadastrar(
        db,
        cliente.nome,
        cliente.cpf,
        cliente.data_nascimento,
        cliente.limite,
        )
    return cliente


@app.get("/api/v1/clientes", tags=["Clientes"])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = mercado_cliente_repositorio.obter_todos(db)
    return clientes


@app.delete("/api/v1/clientes/{id}", tags=["Clientes"])
def apagar_cliente(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = mercado_cliente_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    return {
        "status": "OK"
    }


@app.get("/api/v1/clientes/{id}", tags=["Clientes"])
def obter_cliente(id: int, db: Session = Depends(get_db)):
    cliente = mercado_cliente_repositorio.obter_por_id(db, id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    return cliente


@app.put("/api/v1/clientes/{id}", tags=["Clientes"])
def editar_cliente(id: int, cliente: ClienteEditar, db: Session = Depends(get_db)):
    linhas_afetadas = mercado_cliente_repositorio.editar(db, id, cliente.data_nascimento, cliente.limite)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    return {
        "status": "OK"
    }



# fastapi dev main.pys///
# 127.0.0.1/greetings///