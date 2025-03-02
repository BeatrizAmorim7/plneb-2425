# TPC3 - Dicionário de conceitos médicos

O ficheiro `TPC3.py` processa um documento de texto (`dicionario_medico.txt`) que contém conceitos médicos e as suas respetivas descrições, e cria um ficheiro HTML formatado com essa informação.


## Como Funciona

O script realiza as seguintes etapas:

### 1. Leitura do ficheiro e limpeza dos dados
- O ficheiro `dicionario_medico.txt` é lido e armazenado na variável `texto`.
- São removidos caracteres `\f`, que representam quebras de página.

```python
texto = re.sub("\f", "", texto)  # Remove quebras de página
```

### 2. Marcação dos conceitos com "@"
- Para facilitar a extração, os conceitos são marcados com "@" antes do nome.
- Como a maioria das descrições termina com um ponto final (`.`), podemos assumir que um novo conceito começa após o ponto final, seguidos de dois `\n`.
- Com esta lógica, surgiu um problema: a palavra "Significado", no início do texto, não termina com um ponto final, o que interfere na identificação do primeiro conceito. Para resolver isso, garantiu-se que a palavra "Significado" termine com um ponto final, permitindo que o primeiro conceito seja identificado corretamente.


```python
texto = re.sub(r"\bSignificado\b", "Significado.", texto)  # Garante o ponto final
texto = re.sub(r"\.\n\n", ".\n\n@", texto)  # Marca o início dos conceitos
```

### 3. Extração de conceitos e descrições
- Os conceitos são extraídos utilizando uma expressão regular que encontra:
  1. Um conceito após "@".
  2. A sua descrição, que continua até ao próximo conceito.
  
- A função `limpa_descricao()` remove quebras de linha dentro da descrição e garante que ela fique formatada corretamente.

```python
conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
```

### 4. Gerar o ficheiro HTML
- O ficheiro HTML é criado e guardado no ficheiro `dicionario_medico.html`.


## Possíveis melhorias

O código atual funciona bem para a maioria dos casos, mas há algumas melhorias que poderiam ser implementadas para torná-lo mais robusto e abrangente. Uma das principais melhorias seria tratar casos em que as descrições não terminam com um ponto final. O processamento executado pelo código exposto, assume que todas as descrições terminam com um ponto final. No entanto, há casos em que as descrições terminam com outros caracteres ou até mesmo sem pontuação. Para garantir que todos os conceitos sejam corretamente extraídos, seria necessário implementar uma lógica que identifique o final das descrições mesmo quando não há um ponto final. 
