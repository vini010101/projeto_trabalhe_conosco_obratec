from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class FormData(BaseModel):
    nome: str
    idade: int
    endereco: str
    email: str
    escolaridade: str
    concordo: bool
    trabalho: str
    mensagem: str

@app.get("/", response_class=HTMLResponse)
def read_form():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="/static/css/style.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <title>Trabalhe na marketing now</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-sm bg-dark sticky-top" data-bs-theme="dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Marketing now</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link" aria-current="page" href="../">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="#">Formulario</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <main class="container bg-secondary-subtle">
            <h1 class="text-center my-5">Formulário de Cadastro</h1>
            <form action="http://127.0.0.1:8000/submit" method="post">
                <section class="row mb-2">
                    <div class="col-md-12">
                        <label for="nome" class="mb-2">Nome</label>
                        <input type="text" name="nome" id="nome" class="form-control">
                    </div>
                </section>
                <section class="row mb-2">
                    <div class="col-md-6">
                        <label for="idade">Idade</label>
                        <input type="number" name="idade" id="idade" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label for="endereco">Endereço</label>
                        <input type="text" name="endereco" id="endereco" class="form-control">
                    </div>
                </section>
                <section class="row mb-2">
                    <div class="col-md-12">
                        <label for="email" class="mb-2">E-mail</label>
                        <input type="email" name="email" id="email" class="form-control" placeholder="email@email.com">
                    </div>
                </section>
                <section class="row mb-2 ps-3">
                    <label class="col-form-label-lg">Qual o seu nível de escolaridade?</label>
                    <div class="form-check">
                        <input type="radio" name="escolaridade" id="fundamental" value="fundamental" class="form-check-input">
                        <label for="fundamental" class="form-check-label">Fundamental</label>
                    </div>
                    <div class="form-check">
                        <input type="radio" name="escolaridade" id="medio" value="medio" class="form-check-input">
                        <label for="medio" class="form-check-label">Médio</label>
                    </div>
                    <div class="form-check">
                        <input type="radio" name="escolaridade" id="superior" value="superior" class="form-check-input">
                        <label for="superior" class="form-check-label">Superior</label>
                    </div>
                </section>
                <section class="p-5 mt-3" id="contrato">
                    <div class="container-fluid">
                        <h1>Termos do Contrato</h1>
                        <p class="lead altura">
                            <!-- Termos do contrato aqui -->
                       1. OBJETO

1.1 A EMPRESA conduzirá um processo seletivo para vagas de emprego.

1.2 O CANDIDATO concorda em fornecer à EMPRESA informações e dados pessoais necessários para avaliação e consideração no processo seletivo.

2. AUTORIZAÇÃO DE USO DE DADOS

2.1 O CANDIDATO autoriza a EMPRESA a coletar, armazenar e utilizar os dados fornecidos para avaliação de qualificações e consideração no processo seletivo.

2.2 Os dados fornecidos pelo CANDIDATO incluem, mas não se limitam a, nome, endereço, número de telefone, endereço de e-mail, histórico acadêmico, experiência profissional, habilidades e outras informações relevantes para o processo seletivo.

3. CONFIDENCIALIDADE

3.1 A EMPRESA compromete-se a tratar todas as informações fornecidas pelo CANDIDATO de forma confidencial.

3.2 Os dados do CANDIDATO serão acessíveis apenas aos responsáveis pelo processo seletivo e serão utilizados exclusivamente para avaliação e seleção de candidatos.

4. PERÍODO DE RETENÇÃO DE DADOS

4.1 Os dados fornecidos pelo CANDIDATO serão retidos pela EMPRESA durante o período necessário para a conclusão do processo seletivo.

4.2 Caso o CANDIDATO seja contratado, os dados fornecidos serão mantidos de acordo com as políticas internas de gestão de dados da EMPRESA.

5. DIREITOS DO CANDIDATO

5.1 O CANDIDATO tem o direito de solicitar acesso, correção ou exclusão dos seus dados pessoais a qualquer momento, entrando em contato com a EMPRESA.

6. CONSIDERAÇÕES FINAIS

6.1 Este contrato representa o entendimento completo entre as partes e substitui qualquer acordo ou entendimento anterior, oral ou escrito, relacionado ao objeto deste contrato.

6.2 Ao assinar este contrato, o CANDIDATO reconhece que leu e compreendeu as condições aqui estabelecidas, concordando voluntariamente em participar do processo seletivo da EMPRESA.
                         </p>
                        <hr>
                        <div class="form-check">
                            <input type="checkbox" name="concordo" id="concordo" value="concordo" class="form-check-input">
                            <label for="concordo" class="form-check-label">Concordo</label>
                        </div>
                    </div>
                </section>
                <section class="row mb-2">
                    <label class="col-form-label-lg">Em qual setor gostaria de trabalhar?</label>
                    <select name="trabalho" class="form-select">
                        <option value="">Escolha uma opção...</option>
                        <option value="RH">RH</option>
                        <option value="tecnologia">Tecnologia</option>
                        <option value="financeiro">Financeiro</option>
                    </select>
                </section>
                <section class="row mb-2"> 
                    <div class="col-md-12">
                        <label for="mensagem" class="mb-2">Por que você quer trabalhar nesse setor?</label>
                        <textarea name="mensagem" id="mensagem" placeholder="Descreva aqui" class="form-control"></textarea>
                    </div>
                </section>
                <div class="col-md-6 mx-auto my-5">
                    <button type="submit" class="btn btn-primary col-12">Enviar Formulário</button>
                </div>
            </form>
        </main>
        <footer class="container-fluid bg-dark text-white py-3">
            <section class="row d-flex justify-content-between">
                <div class="col-md-6">
                    <p>&copy;2024 Marketing Now</p>
                </div>
            </section>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script src="/static/js/script.js"></script>
    </body>
    </html>
    """

@app.post("/submit")
def submit_form(
    nome: str = Form(...),
    idade: int = Form(...),
    endereco: str = Form(...),
    email: str = Form(...),
    escolaridade: str = Form(...),
    concordo: bool = Form(...),
    trabalho: str = Form(...),
    mensagem: str = Form(...)
):
    return {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "email": email,
        "escolaridade": escolaridade,
        "concordo": concordo,
        "trabalho": trabalho,
        "mensagem": mensagem
    }
