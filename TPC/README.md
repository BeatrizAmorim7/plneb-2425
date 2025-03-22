## TPC6 - Funcionalidade de pesquisa no dicionário médico

Este TPC6 consistiu na implementação de uma funcionalidade de pesquisa para a aplicação desenvolvida nas últimas aulas, referente ao dicionário médico. A funcionalidade permite aos utilizadores a pesquisa de uma palavra específica no dicionário. São devolvidas as ocorrências dessa palavra tanto na designação quanto na descrição dos conceitos.


### Pesquisa
O utilizador digita uma palavra no campo de pesquisa e clica no botão "Pesquisar". É verificado se a palavra pesquisada está presente tanto na designação quanto na descrição, de algum conceito do dicionário médico. Caso haja uma correspondência, é retornada uma lista contendo a designação e a descrição, com a palavra destacada a negrito para facilitar a identificação.

É possível clicar num conceito retornado, sendo redirecionado para a página detalhada desse conceito específico.


## Estrutura do Projeto

### Rotas Adicionadas
- **`/pesquisar` (GET):** Rota para exibir a página de pesquisa.
- **`/pesquisar` (POST):** Rota para processar a pesquisa e mostrar os resultados.

### Templates
- **`pesquisa.html`:** Página de pesquisa e apresentação dos resultados.
- Utilização da tag `<b>` para destacar a palavra pesquisada a negrito.
---

