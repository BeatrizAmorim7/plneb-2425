
# TPC5 - Desenvolvimento de Rotas em Flask

Este trabalho consistiu na implementação de uma nova rota, que permite a visualização específica de cada conceito médico. Foi também implementada a possibilidade de aceder à página de cada conceito diretamente ao clicar sobre ele na lista de conceitos criada anteriormente na aula.

## Templates

### Template `conceitos.html`
- Foi alterado de modo a incluir links para cada conceito permitindo que o utilizador aceda diretamente à página de cada um.

### Template `um_conceito.html`
- Foi criado de modo a ser possível exibir os detalhes de um conceito específico (incluindo a designação e descrição).
- Este template é renderizado pela `rota /conceitos/<designacao>`.


## Rotas
###  Rota `/conceitos/<designacao>`

- Permite visualizar a descrição de um conceito específico.
- Faz o render do template `um_conceito.html` que exibe a designação e descrição do conceito.
- O valor de designacao é capturado diretamente do URL e usado para procurar a descrição correspondente no dicionário de conceitos.

### Rota `/conceitos`
   - Esta rota exibe a lista de conceitos.
   - Cada conceito é apresentado como um link que permite acessar a página correspondente, através da rota `/conceitos/<designacao>`.

