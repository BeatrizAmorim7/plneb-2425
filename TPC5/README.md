# TPC5 - Desenvolvimento de Rotas em Flask

Este trabalho consistiu na implementação de uma nova rota, que permite a visualização específica de cada conceito médico, incluindo a respetiva descrição. Foi também implementada a possibilidade de aceder à página de cada conceito diretamente ao clicar sobre ele, na lista de conceitos criada anteriormente na aula.

## Templates

### Template `conceitos.html`
- Os itens da lista de conceitos (criada na aula) foram transformados em links interativos usando a tag `<a>` e o atributo `href` do HTML, permitindo um acesso direto às páginas individuais de cada conceito.


### Template `um_conceito.html`
- Desenvolvido para exibir detalhes de um conceito específico, incluindo sua designação e descrição.


## Rotas
###  Rota `/conceitos/<designacao>`
- Faz o render do template `um_conceito.html` que exibe a designação e descrição do conceito.
- O valor de designacao é capturado diretamente do URL e usado para procurar a descrição correspondente no dicionário de conceitos.

### Rota `/conceitos`
   - Esta rota exibe a lista de conceitos.
   - Cada conceito é apresentado como um link que permite acessar a página correspondente, através da rota `/conceitos/<designacao>`.




