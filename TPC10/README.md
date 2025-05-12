# Web Scraping: Revista Portuguesa de Medicina Interna

O objetivo deste TPC, foi extrair dados de artigos da *Revista Portuguesa de Medicina Interna*, disponível em [https://revista.spmi.pt](https://revista.spmi.pt). Assim, o *script* desenvolvido, recolhe, através de *Web Scrapping*: o título, URL, autores, edição, resumo, palavras-chave, data da publicação e link do PDF. Estas informações são então guardadas num ficheiro JSON  (`revista.json`).


## Resultado
O ficheiro JSON, contém uma lista de dicionários, cada um representando um artigo encontrado. Cada entrada do artigo inclui:

- **title**: O título do artigo, preferencialmente em português quando disponível. 
- **url**: O URL da página do artigo.
- **authors**: Uma lista dos nomes dos autores.
- **archives**: O título da edição (como "Janeiro / Março").
- **abstract**: O resumo pode vir em dois formatos: como um dicionário estruturado (com secções como 'Introdução', 'Métodos', etc.) quando se encontram organizados por tópicos, ou como uma string simples quando apresentado em texto contínuo sem divisões.
- **keywords**: Uma lista de palavras-chave.
- **doi**: O link do DOI ou uma string vazia se indisponível.
- **publish_date**: A data de publicação ou uma string vazia se não houver data disponível.
- **pdf_link**: O URL do PDF ou uma string vazia se não existir.

## Script 
O *script* em Python utiliza a biblioteca `requests` para obter conteúdo HTML e `BeautifulSoup` (de bs4) para o analisar. O *script* conta com três funções principais:

1. `get_issue_urls`: Obtém os URLs das edições recentes da revista.
2. `extract_article_info`: Extrai os dados da página de um artigo.
3. `scrape_articles`: Realiza o processo de extração e compilação dos dados. 

## Exemplo de output
```json
[  
  {
    "title": "Estudo Populacional das Prioridades Verde e Azul num Serviço de Urgência",
    "url": "https://revista.spmi.pt/index.php/rpmi/article/view/188-92",
    "authors": [
      "David Prescott",
      "Ana Isabel Brochado",
      "Vasco Evangelista",
      "Andreia  Carlos",
      "Ana Sofia Corredoura"
    ],
    "archives": "Outubro/Dezembro",
    "abstract": {
      "Introdução": "A gestão do Serviço de Urgência Geral (SUG) é complexa e multifatorial, com um influxo crescente de utentes, levando a sobrelotação hospitalar, com maiores tempos de espera, desgaste profissional e menor qualidade de cuidados. Cerca de 43% dos casos em Portugal são classificados como admissões não urgentes e pouco urgentes.",
      "Métodos": "Este estudo observacional retrospetivo foi realizado no SUG de um hospital distrital de Portugal, de outubro de 2018 a maio de 2019. Foram incluídos adultos com prioridade verde e azul na triagem. O destino na alta e o número de admissões à urgência foram analisados, com associações examinadas em relação à idade, modo de proveniência, ativação de via azul e acesso a cuidados de saúde primários.",
      "Resultados": "Incluímos 41 066 episódios, a maioria deles com prioridade verde (99,9%). A maioria dos doentes, 98,8%, teve alta para cuidados ambulatórios. Os frequent flyers (≥ 4 admissões) constituíam 3,3% dos doentes e os high users (≥ 10admissões) 0,3%. A análise mostrou associações significativas entre o destino à data de alta com a idade, com a proveniência e com a ativação da via azul (p<0,001). Houve ainda uma associação estatisticamente muito significativa entre o número de admissões e a idade (p<0,001) e o número de admissões e a capacidade de acesso aos CSP (p<0,001).",
      "Conclusão": "O estudo destaca a importância de vários fatores no destino dos doentes, mostrando uma forte associação entre a idade e a probabilidade de internamento. Além disso, a forma de chegada ao SUG e a ativação da via azul também se associam com o destino do doente. No entanto, são necessários mais estudos para entender os problemas sistémicos do SUG."
    },
    "keywords": [
      "Admissão de Doentes",
      "Alta do Doente",
      "Mau Uso de Serviços de Saúde",
      "Serviço de Urgência Hospitalar",
      "Triagem"
    ],
    "doi": "https://doi.org/10.24950/rspmi.2512",
    "publish_date": "2024-12-19",
    "pdf_link": "https://revista.spmi.pt/index.php/rpmi/article/view/188-92/1896"
  },
  ...
]
```

