# README - Expressões Regulares em Python

O ficheiro `Ficha_RE_1.ipynb`, presente nesta pasta, descreve diversas funções usadas para a manipulação de strings utilizando expressões regulares em Python. 

# Funções e exemplos

## Exercício 1

### 1.1 `verifica_hello(linha)`
Determina se a palavra "hello" aparece no início da linha. 

**Exemplos:**
```python
verifica_hello("hello world")  # True.
verifica_hello("goodbye world")  # False.
verifica_hello("hi, hello there")  # False.
```


### 1.2. `encontrar_hello_string(line)`
Verifica se a palavra "hello" aparece em qualquer posição da linha.

**Exemplos:**
```python
encontrar_hello_string("hello world")  # True.
encontrar_hello_string("goodbye world")  # False.
encontrar_hello_string("hi, hello there")  # True.
```

### 1.3. `encontra_hello(line)`
Procura por todas as ocorrências de "hello" dentro da string, independentemente da palavra estar em maiúsculas ou minúsculas.

**Exemplo:**
```python
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"

encontra_hello(line)   # Foram encontradas 4 ocorrências da palavra 'hello'.
```

### 1.4. `substitui_todos_hello(line)`
Substitui todas as ocorrências da palavra "hello" por "*YEP*", desconsiderando se está em maiúsculas ou minúsculas. 

**Exemplo:**
```python
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"

substitui_todos_hello(line)   # "*YEP* there! Uh, hi, *YEP*, it's me... Heyyy, *YEP*? *YEP*!"
```

### 1.5. `separar_frutas(line)`
Divide uma string utilizando a vírgula como delimitador.

**Exemplo:**
```python
line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."

separar_frutas(line)   # ['bananas', ' laranjas', ' maçãs', ' uvas', ' melancias', ' cerejas', ' kiwis', ' etc.']
```


## Exercício 2
### `palavra_magica(frase)`
Verifica se a frase termina com "por favor", seguido de uma pontuação válida, como a vírgula, ponto final ou ponto de exclamação.

**Exemplos:**
```python
palavra_magica("Posso ir à casa de banho, por favor?")  # True
palavra_magica("Preciso de um favor.")  # False
```


## Exercício 3 
### `narcissismo(linha)`
Calcula quantas vezes a palavra "eu" aparece na string, independentemente de estar em maiúsculas ou minúsculas.

**Exemplo:**
```python
line = "Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."

narcissismo(line)   # 6
```


## Exercício 4
### `troca_de_curso(linha, novo_curso)`
Substitui todas as ocorrências de "LEI" pelo nome do curso especificado.

**Exemplo:**
```python
linha = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."

troca_de_curso(linha, "EngBiom")  # "EngBiom é o melhor curso! Adoro EngBiom! Gostar de EngBiom devia ser uma lei."
```


## Exercício 5
### `soma_string(linha)`
Dada uma string contendo números separados por vírgulas, retorna a soma deles.

**Exemplo:**
```python
soma_string("4,-6,2,3,8,-3,0,2,-5,1")  # 6
```


## Exercício 6
### `pronomes(frase)`
Encontra e retorna todos os pronomes pessoais presentes na frase dada.

**Exemplo:**
```python
pronomes("Ela ficou feliz, ele não. Nós ficamos felizes, eles não.")   # ['Ela', 'ele', 'Nós', 'eles']
```


## Exercício 7
### `variavel_valida(string)`
Verifica se uma string é um nome válido para uma variável, começando com uma letra e contendo apenas letras, números ou underscores. 

**Exemplos:**
```python
variavel_valida("a123_bB_2")  # True
variavel_valida("2123_bB_")  # False
variavel_valida("B12?_bB N")  # False
```


## Exercício 8
### `inteiros(frase)`
Identifica e retorna todos os números inteiros presentes na string.

**Exemplos:**
```python
inteiros("Existem 3 casos, 2 de homicídio e 1 de suicídio")  # ['3', '2', '1']
inteiros("O número 14 é positivo e -9 é negativo")  # ['14', '-9']
```


## Exercício 9
### `underscores(string)`
Substitui espaços por underscores, garantindo que múltiplos espaços sejam reduzidos a um único underscore. 

**Exemplos:**
```python
underscores("Substituir string por underscores    . Vários    espaços")  # "Substituir_string_por_underscores_._Vários_espaços"
```


## Exercício 10
### `codigos_postais(lista_numeros)`
Recebe uma lista de códigos postais e divide-os com base no hífen. Retorna uma lista de tuplos.

**Exemplo:**
```python
lista = ["4700-000", "1234-567", "8541-543", "4123-974", "9481-025"]

codigos_postais(lista)  # [('4700', '000'), ('1234', '567'), ('8541', '543'), ('4123', '974'), ('9481', '025')]
```
