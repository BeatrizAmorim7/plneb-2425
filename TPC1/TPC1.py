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
