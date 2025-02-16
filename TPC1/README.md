# TPC1: Funções de manipulação de strings

O ficheiro `TPC1.py` contém um conjunto de funções para realizar operações de manipulação de strings, além de um menu interativo para facilitar a execução das mesmas.

## Funções Implementadas

1. **Reverter a string**:
   - Função `reverse(s)`: Inverte a string dada.
   - Exemplo: reverse ('hello') → 'olleh'

2. **Contar quantos 'a' ou 'A' há na string**:
   - Função `how_many(s)`: Conta quantas ocorrências das letras 'a' ou 'A' existem na string fornecida.
   - Exemplo: how_many ('Abacaxi e Ananás') → 5


3. **Contar o número de vogais na string**:
   - Função `vowels(s)`: Conta o número de vogais, tanto maiúsculas quanto minúsculas, presentes na string dada.
   - Exemplo: vowels ('Exemplo de teste') → 6

4. **Converter para minúsculas**:
   - Função `lower(s)`: Converte os caracteres da string para minúsculas.
   - Exemplo: lower ('MaIúsculA') → 'maiúscula'

5. **Converter para maiúsculas**:
   - Função `upper(s)`: Converte os caracteres da string para maiúsculas.
   - Exemplo: upper ('minúscula') → 'MINÚSCULA'

6. **Verificar se uma string é capicua**:
   - Função `capicua(s)`: Verifica se a string fornecida é capicua, ou seja, se é igual à sua versão invertida.
   - Exemplo: capicua ('radar') → True

7. **Verificar se duas strings estão balanceadas**:
   - Função `balanceada(s1, s2)`: Verifica se todos os caracteres da string `s1` estão presentes na string `s2`.
   - Exemplo:
      - balanceada ('aabbcc', 'abcabc') → True
      - balanceada ('abc', 'abcc') → False

8. **Calcular o nº de ocorrências de s1 em s2**:
   - Função `count(s1, s2)`: Conta o nº de vezes que a substring `s1` aparece na string `s2`.
   - Exemplo: count ('lo', 'hello hello') → 2

9. **Verificar se duas strings são anagramas**:
   - Função `anagrama(s1, s2)`: Determina se as strings `s1` e `s2` são anagramas, isto é, se contêm os mesmos carateres (com a mesma frequência), independentemente da ordem em que aparecem.
   - Exemplo: anagrama ('listen', 'silent') → True, anagrama ('hello', 'world') → False

10. **Calcular a tabela de classes de anagramas**:
    - Para esta questão, foram criadas duas funções. A primeira, `criar_dicionario_anagramas`, recebe uma lista de palavras e cria um dicionário em que as chaves são as letras ordenadas alfabeticamente de cada palavra. Assim, palavras que são anagramas entre si são agrupadas sob a mesma chave. A segunda função, `tabela_anagrama`, percorre o dicionário criado pela primeira função e exibe, de forma formatada, a tabela das classes de anagramas. Cada linha da tabela mostra a sequência de letras ordenadas (a chave) e as palavras associadas a essa chave.
    - Exemplo: 
      Tabela de classes de anagramas:
      
      | Sequência de letras ordenadas        | Palavras anagramas| 
      | ------------- |:-------------:| 
      | amor          | amor, mora, ramo, roma  |
      | aglo          | galo, algo      | 
      | deostu        | estudo, duetos |

## Menu Interativo

O menu interativo permite ao utilizador escolher entre as diferentes funções implementadas. Além disto, o programa também oferece exemplos automáticos para facilitar o entendimento e a utilização das funções. Estes exemplos são executados automaticamente ao selecionar a opção correspondente, sem a necessidade de inserir dados manualmente.
