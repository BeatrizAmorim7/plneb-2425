from flask import Flask, request, render_template
import json

app = Flask(__name__)
dbFile = open("conceitos_.json", encoding="UTF-8")

db = json.load(dbFile)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/conceitos')
def conceitos_api():
    return db

@app.route('/api/conceitos/<designacao>')
def conceito_api(designacao):
    return {"designacao": designacao, "descricao": db[designacao]}


@app.post("/api/conceitos")
def adicionar_conceito():
    #json
    data = request.get_json()
    #{ "designacao":"vida", "descricao": "a vida é..."}
    db[data["designacao"]] = data["descricao"]

    f_out = open("conceitos_.json", "w", encoding="UTF-8")  
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    return data


#TPC ---------------------------------------------------------------
#Criar a rota /conceitos/<designacao> => fazer render template de um conceito e pôr a lista dos conceitos clicável (vai para a rota criada)

@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")

@app.route('/conceitos/<designacao>')
def conceito_detalhe(designacao):
    descricao = db[designacao]
    return render_template('um_conceito.html', designacao=designacao, descricao=descricao)

app.run (host = "localhost", port=4002, debug = True)

