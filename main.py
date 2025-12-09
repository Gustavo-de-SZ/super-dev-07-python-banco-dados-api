from fastapi import FastAPI, HTTPException

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
        return HTTPException(
            status_code=400,
            detail="operacao invalida"
        )
    if operacao == "somar":
        resultado = n1 + n2
        return{
            "n1": n1,
            "N2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return{
            "n1": n1,
            "N2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }
@app.get ("/pessoas/nome-completo")
def concatenar_nome(nome1: str, nome2: str):
    concatenar = nome1 + " " + nome2
    return {"resultado": concatenar}

@app.get ("/pessoas/calcular-ano-nascimento")
def calcular_ano_nascimento(idade: int):
    data_nascimento = 2025 - idade
    return {"ano de nascimento": data_nascimento}

@app.get ("/pessoas/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso/(altura * altura)
    
    if imc < 18.5:
        status = "abaixo"
    elif imc < 25:
        status = "peso normal"
    elif imc < 30:
        status = "sobrepeso"
    elif imc > 30:
        status = "obesidade"
        
    return {"imc": imc,  "status": status}

