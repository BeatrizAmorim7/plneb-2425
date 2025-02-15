# TPC1: Funções de Manipulação de Strings

O ficheiro TPC1.py contém um conjunto de funções para realizar operações de manipulação de strings, além de um menu interativo para facilitar a execução das funções.

## Funções Implementadas

1. **Reverter a string**:
   - Função `reverse(s)`: Inverte a string dada como entrada.

2. **Contar quantos 'a' ou 'A' há na string**:
   - Função `how_many(s)`: Conta quantas ocorrências das letras 'a' ou 'A' existem na string fornecida.

3. **Contar o número de vogais na string**:
   - Função `vowels(s)`: Conta o número de vogais, tanto maiúsculas quanto minúsculas, presentes na string dada.

4. **Converter para minúsculas**:
   - Função `lower(s)`: Converte os caracteres da string para minúsculas.

5. **Converter para maiúsculas**:
   - Função `upper(s)`: Converte os caracteres da string para maiúsculas.

6. **Verificar se uma string é capicua**:
   - Função `capicua(s)`: Verifica se a string fornecida é capicua, ou seja, se é igual à sua versão invertida.

7. **Verificar se duas strings estão balanceadas**:
   - Função `balanceada(s1, s2)`: Verifica se todos os caracteres da string `s1` estão presentes na string `s2`.

8. **Calcular o nº de ocorrências de s1 em s2**:
   - Função `count(s1, s2)`: Conta o nº de vezes que a substring `s1` aparece na string `s2`.

9. **Verificar se duas strings são anagramas**:
   - Função `anagrama(s1, s2)`: Determina se as strings `s1` e `s2` são anagramas, isto é, se contêm os mesmos carateres (com a mesma frequência), independentemente da sequência em que aparecem.

10. **Calcular a tabela de classes de anagramas**:
    - Função que recebe um dicionário de palavras separadas por vírgulas e calcula as classes de anagramas, agrupando as palavras que possuem as mesmas letras (em qualquer ordem).


## Menu Interativo

O menu interativo permite ao usuário escolher entre as diferentes funções implementadas. Após a execução de cada operação, o menu é exibido novamente, permitindo a escolha de outra função ou a saída do programa.

As opções do menu são:
- 1: Reverter a string
- 2: Contar quantos 'a' ou 'A' há na string
- 3: Contar o número de vogais na string
- 4: Converter para minúsculas
- 5: Converter para maiúsculas
- 6: Verificar se a string é capicua
- 7: Verificar se duas strings estão balanceadas
- 8: Contar o número de ocorrências de uma substring em outra string
- 9: Verificar se duas strings são anagramas
- 10: Calcular a tabela de classes de anagramas
- 0: Sair
