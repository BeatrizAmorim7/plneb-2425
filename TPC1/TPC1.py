'''Create a function that:
1. given a string “s”, reverse it.
2. given a string “s”, returns how many “a” and “A” characters are present in it.
3. given a string “s”, returns the number of vowels there are present in it.
4. given a string “s”, convert it into lowercase.
5. given a string “s”, convert it into uppercase.
6. Verifica se uma string é capicua
7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão
balanceadas se todos os caracteres de s1 estão presentes em s2.)
8. Calcula o número de ocorrências de s1 em s2
9. Verifica se s1 é anagrama de s2.
○ "listen" e "silent": Deve imprimir True
○ "hello", "world": Deve imprimir False
10. Dado um dicionário, calcular a tabela das classes de anagramas. '''


#1
def reverse(s):
    return s[::-1]

#2
def how_many(s):
    count = 0
    for letter in s:
        if letter == 'a' or letter=='A':
            count = count + 1
    return count

#3
def vowels(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count = count + 1
    return count

#4     
def lower(s):
    return s.lower()

#5
def upper(s):
    return s.upper()

#6
def capicua(s):
    return s == s[::-1]

#7
def balanceada(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    return True

#8 Calcula o número de ocorrências de s1 em s2
def count(s1,s2):
    return s2.count(s1)

#9 Verifica se s1 é anagrama de s2.
#○ "listen" e "silent": Deve imprimir True
#○ "hello", "world": Deve imprimir False
def anagrama(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False 
    
# 10. Dado um dicionário, calcular a tabela das classes de anagramas. 

def criar_dicionario_anagramas(palavras):
    dicionario = {}

    for palavra in palavras:
        chave = "".join(sorted(palavra))  

        if chave in dicionario:
            dicionario[chave].append(palavra)
        else:
            dicionario[chave] = [palavra]

    return dicionario


def tabela_anagrama(dicionario):
    print(f"{'Sequência de letras ordenadas':<35}{'Palavras anagramas'}")
    print("-" * 50)

    for chave, anagramas in dicionario.items():
        print(f"{chave:<35}{', '.join(anagramas)}")

def exemplos_automaticos():
    print("\n--- Exemplos Automáticos ---\n")

    # 1. Reverter string
    s = "abcdef"
    print(f"reverse('{s}') → '{reverse(s)}'")

    # 2. Contar 'a' e 'A'
    s = "Ananas e Abacaxi"
    print(f"how_many('{s}') → {how_many(s)}")

    # 3. Contar vogais
    s = "Exemplo de teste"
    print(f"vowels('{s}') → {vowels(s)}")

    # 4. Converter para minúsculas
    s = "MaIúsculA"
    print(f"lower('{s}') → '{lower(s)}'")

    # 5. Converter para maiúsculas
    s = "minúscula"
    print(f"upper('{s}') → '{upper(s)}'")

    # 6. Verificar capicua
    s1 = "radar"
    s2 = "python"
    print(f"capicua('{s1}') → {capicua(s1)}")
    print(f"capicua('{s2}') → {capicua(s2)}")

    # 7. Strings balanceadas
    s1, s2 = "abc", "bacxyz"
    print(f"balanceada('{s1}', '{s2}') → {balanceada(s1, s2)}")
    s1, s2 = "xyz", "abc"
    print(f"balanceada('{s1}', '{s2}') → {balanceada(s1, s2)}")

    # 8. Contar ocorrências
    s1, s2 = "ab", "abcabcab"
    print(f"count('{s1}', '{s2}') → {count(s1, s2)}")

    # 9. Verificar anagramas
    s1, s2 = "listen", "silent"
    print(f"anagrama('{s1}', '{s2}') → {anagrama(s1, s2)}")
    s1, s2 = "hello", "world"
    print(f"anagrama('{s1}', '{s2}') → {anagrama(s1, s2)}")

    # 10. Dicionário de anagramas
    palavras = ["amor", "mora", "ramo", "roma", "galo", "algo", "estudo", "duetos"]
    dicionario = criar_dicionario_anagramas(palavras)
    print("\nTabela de classes de anagramas:")
    tabela_anagrama(dicionario)






def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Reverter a string")
        print("2. Contar quantos 'a' ou 'A' há na string")
        print("3. Contar o número de vogais na string")
        print("4. Converter para minúsculas")
        print("5. Converter para maiúsculas")
        print("6. Verificar se a string é capicua")
        print("7. Verificar se duas strings estão balanceadas")
        print("8. Contar o número de ocorrências de s1 em s2")
        print("9. Verificar se duas strings são anagramas")
        print("10. Calcular a tabela de classes de anagramas")
        print("11. Executar exemplos automáticos")

        print("0. Sair")
        
        escolha = input("Escolha a opção: ")
        
        if escolha == "1":
            s = input("Digite a string: ")
            print("String reversa:", reverse(s))
        
        elif escolha == "2":
            s = input("Digite a string: ")
            print("Número de 'a' ou 'A' presentes:", how_many(s))
        
        elif escolha == "3":
            s = input("Digite a string: ")
            print("Número de vogais presentes:", vowels(s))
        
        elif escolha == "4":
            s = input("Digite a string: ")
            print("String em minúsculas:", lower(s))
        
        elif escolha == "5":
            s = input("Digite a string: ")
            print("String em maíusculas:", upper(s))
        
        elif escolha == "6":
            s = input("Digite a string: ")
            print("É capicua?", capicua(s))
        
        elif escolha == "7":
            s1 = input("Digite a primeira string: ")
            s2 = input("Digite a segunda string: ")
            print("Balanceadas? :", balanceada(s1, s2))
        
        elif escolha == "8":
            s1 = input("Digite a string 1 (substring): ")
            s2 = input("Digite a string 2: ")
            print("Número de ocorrências:", count(s1, s2))
        
        elif escolha == "9":
            s1 = input("Digite a primeira string: ")
            s2 = input("Digite a segunda string: ")
            print("As strings são anagramas?", anagrama(s1, s2))
        
        elif escolha == "10":
            print("Digite as palavras separadas por vírgulas.\nExemplo: amor, mora, ramo")

            entrada = input("Digite as palavras:")
            palavras = [palavra.strip() for palavra in entrada.split(",")]            
            dicionario = criar_dicionario_anagramas(palavras)
            tabela_anagrama(dicionario)
        
        elif escolha == "11":
            exemplos_automaticos()

            
        elif escolha == "0":
            print("A sair do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione Enter para voltar ao menu...")

menu()

