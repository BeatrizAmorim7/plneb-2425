from flask import Flask, request, render_template
import json
import re 
app = Flask(__name__)
dbFile = open("conceitos_.json", encoding="UTF-8")

db = json.load(dbFile)


@app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def hello_world():
    return render_template("home.html")


@app.route('/api/conceitos')
def conceitos_api():
    return db

@app.route('/api/conceitos/<designacao>')
def conceito_api(designacao):
    return {"designacao": designacao, "descricao": db[designacao]}


@app.post("/api/conceitos")
def adicionar_conceito_api():
    #json
    data = request.get_json()
    #{ "designacao":"vida", "descricao": "a vida é..."}
    db[data["designacao"]] = data["descricao"]

    f_out = open("conceitos_.json", "w", encoding="UTF-8")  
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    return data

@app.post("/conceitos")
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")

    db[designacao] = descricao

    f_out = open("conceitos_.json", "w", encoding="UTF-8")  
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title ="Lista de conceitos")


@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")

@app.route('/conceitos/<designacao>')
def conceito_detalhe(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template('um_conceito.html', designacao=designacao, descricao=descricao)
    else:
        return render_template('um_conceito.html', designacao="Erro", descricao="Descrição não encontrada")


TPC-------------------------------------------------------------------------------------------
#por o botão pesquisar a funcionar - rota para pesquisar, uma nova página para pesquisar (com uma text input e um 
# botão quando clico no botão na mesma página apareça o termo e a descrição aparecerem em baixo com todas as 
# ocorrencias da palavra escrita => e aparecer com bold )
#maior numero possível

@app.route('/pesquisar')
def pesquisar_palavra():
    return render_template('pesquisa.html')

@app.post('/pesquisar')
def pesquisar():
    palavra = request.form.get('palavra').strip().lower()  # Remove espaços extra
    resultados = []

    if palavra:
        for designacao, descricao in db.items():
            # Verifica a correspondência exata na designação 
            if re.search(rf'\b{re.escape(palavra)}\b', designacao, flags=re.IGNORECASE):
                # Destaca a palavra na designação 
                designacao_destacada = re.sub(rf'\b({re.escape(palavra)})\b', r'<b>\1</b>', designacao, flags=re.IGNORECASE)
                match = (designacao, designacao_destacada, descricao)
                resultados.append(match)

            if re.search(rf'\b{re.escape(palavra)}\b', descricao, flags=re.IGNORECASE):
                descricao_destacada = re.sub(rf'\b({re.escape(palavra)})\b', r'<b>\1</b>', descricao, flags=re.IGNORECASE)
                match = (designacao, designacao, descricao_destacada)
                resultados.append(match)

    return render_template('pesquisa.html', resultados=resultados, palavra=palavra)

app.run (host = "localhost", port=4002, debug = True)
