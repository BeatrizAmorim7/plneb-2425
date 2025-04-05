from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.atlasdasaude.pt/doencasAaZ")

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


def get_doenca_info(url_href):
    url_doenca = "https://www.atlasdasaude.pt" + url_href  
    response = requests.get(url_doenca)  
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    div_content = soup.find("div", class_ = "node-doencas")

    info = {}
    div_data = div_content.find('div', class_ ='field-name-post-date')
    if div_data:
        info['Data'] = div_data.div.div.text

    data_info = div_content.find('div', class_='field-name-body')  

    if data_info:
        titulo = "Descrição"
        info[titulo] = []

        elem = data_info.find('div', class_='field-item even')

        for item in elem:
            if item.name == 'p' or item.name == 'div':
                info[titulo].append(item.text.strip())
            
            #titulos
            elif item.name == 'h2':
                titulo = item.text.replace(" ", "").strip().title()
                info[titulo] = []
   
            #lista de sintomas
            elif item.name == 'ul':
                lista = []
                for li in item.find_all('li'):
                    lista.append(li.text.strip())
                info[titulo].append(lista)

            #secção dos artigos relacionados
            elif item.name == 'h3':
                if len(info[titulo]) == 0:
                    info[titulo].append({item.text.replace(" ", ""): item.a["href"]})
                else:
                    info[titulo][0] = info[titulo][0] | {item.text.replace(" ", ""): item.a["href"]}

    
    # nota
    div_nota = div_content.find('div', class_="field-name-field-nota")
    if div_nota:
        nota = div_nota.find("div", class_= "field-item even").text
        info["Nota"] = nota


    return {"url": url_doenca, "content": info}



def extrai_letra(letra):
    response = requests.get("https://www.atlasdasaude.pt/doencasAaZ/" + letra)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doenca = {}

    for elem in soup.find_all("div", class_="views-row"):
        designacao = elem.div.h3.a.text.strip()
        doenca_url = elem.div.h3.a["href"]
        doenca_info = get_doenca_info(doenca_url)
        desc_div = elem.find("div", class_="views-field-body")
        desc = desc_div.div.text
        doenca_info["Resumo"] = desc.strip().replace(" "," ")
        doenca[designacao] = doenca_info

    return doenca
    

res = {}
for a in range(ord('a'), ord('z') +1 ):   # o ord dá-me o numero de ascii da letra 
    letra = chr(a)  # chr do numero de asci dá-me a letra
    #print(letra)
    #print(extrai_letra(letra))
    
    res = res | extrai_letra(letra)

f_out = open("tpc8.json", "w", encoding="utf-8")
json.dump(res,f_out, indent=4, ensure_ascii=False )
