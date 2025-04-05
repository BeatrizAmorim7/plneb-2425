# TPC8
## Web Scrapping: Doenças do "Atlas da Saúde"

Este TPC tem como objetivo principal a **extração estruturada de informação** sobre doenças a partir do site [Atlas da Saúde](https://www.atlasdasaude.pt/doencasAaZ).

O site apresenta uma listagem de doenças organizadas alfabeticamente, onde cada entrada contém:
- Um pequeno resumo da doença
- Um link para uma página com mais informação detalhada, como sintomas, causas, tratamento, artigos relacionados, entre outros.

---
## Objetivos:

1. Aceder à lista de doenças no site, organizadas por letra (de A a Z);
2. Aceder à página de cada doença;
3. Extrair e organizar as principais informações textuais dessas páginas;
4. Guardar toda a informação num ficheiro `JSON` com o nome `tpc8.json`.

---

### Estrutura da Informação Extraída

Para cada doença, o JSON final contém:

- **`url`**: o link completo da página da doença;
- **`Resumo`**: o pequeno parágrafo de resumo presente na listagem inicial;
- **`content`**: um dicionário com a informação detalhada da doença, que pode incluir:
  - **`Data`**: data de publicação da página;
  - **`Descrição`**: parágrafos introdutórios;
  - **Secções com títulos dinâmicos** (ex: "Sintomas", "Causas", "Tratamento", etc.), quando identificados por `h2` no HTML;
  - **Listas** de sintomas ou outros itens (quando encontrados elementos `ul > li`);
  - **Artigos Relacionados**, identificados por `h3` com links;
  - **Nota** final (se existir).


#### O código está dividido em 3 partes principais:

### 1. `get_doenca_info(url_href)`

- Acede à página individual da doença.
- Extrai a data, descrição, sintomas, causas, tratamento, artigos relacionados e notas.
- Constrói um dicionário `info` com esta informação.

### 2. `extrai_letra(letra)`

- Acede à lista de doenças por letra.
- Para cada doença, extrai o nome, link, resumo e chama a função `get_doenca_info`.
- Constrói um dicionário `doenca` com as doenças dessa letra.



## Exemplo de Saída JSON

```json
{
"Aerofagia": {
    "url": "https://www.atlasdasaude.pt/content/aerofagia",
    "content": {
        "Data": "20/02/2013 - 18:57",
        "Descrição": [
            "A aerofagia é uma condição caracterizada pela deglutição involuntária e excessiva de ar que se acumula no estômago, dando origem a sintomas gastrointestinais desconfortáveis. A aerofagia pode ser crónica ou aguda e pode estar relacionada a fatores físicos e psicológicos."
        ],
        "Causas": [
            "A aerofagia pode ser causada por comer demasiado rápido (taquifagia), por comer alimentos que aumentem a produção de gases (feijão, grão, castanhas, espargos, brócolos, cebolas, leite) ou pela presença de bactérias no intestino (neste caso, dando origem a aerocolia).",
            "A aerofagia é bastante frequente nos lactentes, provocando eructações, acompanhadas muitas vezes de alimentos regurgitados, muitas vezes confundido com vómitos."
        ],
        "Sintomas": [
            [
                "distensão abdominal",
                "inchaço",
                "arroto",
                "flatulência"
            ]
        ],
        "Diagnóstico": [
            "Uma vez que a aerofagia apresenta sintomas semelhante aos de outras condições clínicas, como o refluxo gástrico, alergias alimentares ou desequilíbrios intestinais, o médico deve avaliar e descartar essas hipóteses."
        ],
        "Tratamento": [
            "Enquanto a Aerocolia pode ser tratada com recurso a alguns medicamentos, a Aerofagia pressupõe a alteração de alguns hábitos diários:",
            [
                "Comer devagar",
                "Mastigar bem os alimentos",
                "Evitar falar enquanto come",
                "Comer de boca fechada",
                "Não ingerir bebidas gaseificadas",
                "Evitar alimentos que provoquem gases"
            ],
            "Alguns especialistas recomendam ainda terapia da fala para um melhor controlo da respiração enquanto fala, por forma a resolver o problema."
        ],
        "Nota": "As informações e conselhos disponibilizados no Atlas da Saúde de A-Z não substituem o parecer/opinião do seu Médico e/ou Farmacêutico."
    },
    "Resumo": "A aerofagia é uma condição caracterizada pela deglutição involuntária e excessiva de ar que se acumula no estômago, dando origem a sintomas gastrointestinais desconfortáveis. A aerofagia pode ser crónica ou aguda e pode estar relacionada a fatores físicos e psicológicos."
    }
}

```


