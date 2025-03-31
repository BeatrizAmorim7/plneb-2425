# TPC7

O objetivo deste trabalho foi melhorar a tabela de conceitos, tornando-a mais atraente visualmente. Foi também ativada a pesquisa por **expressões regulares (regex)** e adicionada uma opção de navegação para a tabela na **navbar** do layout. 

---

## Implementação

### 1. **Tabela de Conceitos**

A tabela foi melhorada com o uso do plugin **DataTables** do jQuery. Foram aplicadas as seguintes classes CSS:

- **`display`**: Aplica o estilo padrão do DataTables, permitindo funcionalidades como a paginação, ordenação e pesquisa.
- **`stripe`**: Adiciona uma alternância de cores nas linhas da tabela.
- **`hover`**: Destaca as linhas quando o cursor do mouse passa sobre elas.
- **`cell-border`**: Adiciona bordas visíveis nas células.

Exemplo do código de tabela em HTML:

```html
<table id="tabela_conceitos" class="display stripe hover cell-border">
    <thead class="table-dark">
        <tr>
            <th>Designação</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        {% for designacao, descricao in db.items() %}
            <tr>
                <td><a href="/conceitos/{{ designacao }}" class="text-dark text-decoration-dotted">{{ designacao }}</a></td>
                <td><a href="/conceitos/{{ designacao }}" class="text-dark text-decoration-dotted">{{ descricao }}</a></td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```




A pesquisa com regex foi ativada no ficheiro `conceitos.js`, com a inserção da seguinte linha: 


```javascript
search: {
    regex: true
}
```


Uma nova opção foi adicionada à `navbar` do `layout` para permitir que o utilizador navegue facilmente até a página da tabela dos conceitos.

```html
<ul class="navbar-nav">
    <li class="nav-item">
        <a class="nav-link" href="/conceitos">Tabela de Conceitos</a>
    </li>
</ul>
