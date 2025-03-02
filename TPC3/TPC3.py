import re

file = open("dicionario_medico.txt", encoding = "utf-8")

texto = file.read()

#limpeza
#tirar os \f que aparecem em algumas linhas
texto = re.sub("\f","",texto)       


#marcar
#queremos marcar os nossos conceitos - colocar marca @ 


#é preciso adicionar isto, porque posteriormente com o processamento realizado, é necessário que acabe com . para apanhar o primeiro conceito
texto = re.sub(r"\bSignificado\b","Significado.",texto) 


#grande parte das descrições acabam em ".", considerando isto, sabemos que a maioria dos conceitos começam depois de um ponto final e de dois \n
texto = re.sub(r"\.\n\n",".\n\n@",texto) 



def limpa_descricao(descricao):
    descricao = descricao.strip() 
    descricao = re.sub(r"\n", " ", descricao) 
    return descricao


conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)

conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
print(conceitos)


def gera_html(conceitos):
    html_header = f"""
        <!DOCTYPE html>
        <head>
        <meta charset = "UTF-8">
        </head>
        <body> 
        <h3>Dicionário de conceitos Médicos </h3>
        <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/
        2025 <p>"""

    html_conceitos = ""

    for designacao, descricao in conceitos:
        html_conceitos += f"""
                    <div>
                    <p><b>{designacao}</b></p> 
                    <p>{descricao}</p> 
                    </div>
                    <hr/>       
            """

    html_footer = """
        </body>
    </html> """

    return html_header + html_conceitos + html_footer

html = gera_html(conceitos)
f_out = open("dicionario_medico.html", "w", encoding = "utf-8")
f_out.write(html)

f_out.close()


