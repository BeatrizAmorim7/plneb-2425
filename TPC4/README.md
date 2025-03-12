# Descrição do Projeto

Foi criada uma página HTML que exibe alguns filmes e séries, e as suas respetivas informações. A página inclui várias secções, como uma introdução, uma seção com uma grelha de filmes e séries, e uma seção informativa sobre onde visualizar o conteúdo e onde obter mais informações.

## Estrutura do Projeto

### 1. **CSS Global**
- Todos os elementos foram definidos com `margin: 0`, `padding: 0` e `box-sizing: border-box` para garantir consistência entre navegadores. A fonte padrão é a **Roboto** (sem serifa), com fontes adicionais para títulos (Pacifico, Lobster) e corpo (Quicksand).

### 2. **Secções**
#### a) **Secção de Introdução**
- Neste campo, é apresentado um título e uma breve introdução à página.

#### b) **Grelha de Filmes e Séries**
- Aqui é exibido uma lista de filmes e séries em formato de grelha com 5 itens por linha.
- As imagens dos itens são responsivas, e ao passar o cursor sobre elas, a imagem expande-se e o conteúdo do item fica levemente translúcido.
- A imagem ocupa a área toda do item, com bordas arredondadas.
- Ao passar o cursor sobre os itens, um overlay escuro com informações adicionais (como a sinopse) sobre o filme/série é exibido.

#### c) **Seção Informativa**
- Exibe duas categorias de conteúdo: uma com informações adicionais sobre os filmes e séries, e outra com detalhes sobre as plataformas onde é possível assisti-los.
- Cada categoria contém uma lista de links que mudam de fundo e oferecem um efeito visual de destaque quando o utilizador passa com o cursor.
  
### 3. **Outros Estilos**
- **Grelha de Imagens**: Usando o`grid-template-columns`, a grelha é dividida em 5 colunas, com espaçamento entre os itens (`gap: 20px`).
- **Overlay de Detalhes**: Um efeito de sobreposição que aparece quando o usuário passa o cursor sobre um item na grelha, oferecendo mais informações.
  
## Funcionalidades

- Exibição dinâmica de filmes e séries.
- Efeitos interativos ao passar o cursor sobre os itens.
- Informações extras mostradas ao interagir com os itens da grelha.

## Tecnologias Utilizadas

- **HTML**: Para a estrutura da página.
- **CSS**: Para o estilo visual, incluindo layout de grelha e efeitos de transição.


