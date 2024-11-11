"""
DOCTRING SEMPRE UTILIZANDO 3 ASPAS
NÃO É UM COMENTÁRIO
"""

# Permite escrever um comentário

# Imprimir na tela
print('olá mundo')

# sep = separador, o que deseja entre os valores passados no print
# caracteres que representam essa sequencia são \r\n (return e line feed) quebra linha
print(89,00, sep='-', end='##')

"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte 

# Dinamica, ela identifica que tipo de informação está sendo passada 
# 

str -> string -> texto
String são textos que estão dentro das aspas
"""

# Aspas simples
print('Victor Santos Rohod')

# Aspas duplas 
print(1,"Victor Santos 'Rohod'")

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo

print(11) # int
print(-11) # int
print(0) 

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo

print(1.1) # float
print(0.0) # float
print(-1.5) # float

# A função type mostra o tipo que o python
# inferiu ao valor

print( type('Victor') )
print( type(1) )
print( type(1.1), type(-1.1), type(0.0) )

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa
# só existem duas respostas possiveis
# sim (true) ou não (false)
# existem varios operadores para "questionar"
# dentro deles o ==, que é um operador lógico que
# questiona se um valor é igual a outro

print(10 == 10) # sim => True (verdadeiro)
print(10 == 11) # não => False (falso)
print(type(10 == 10)) 
print(type(10 == 11)) 
print(type(True)) 
print(type(False)) 

# conversão de tipos, coerção
# type convertion, typecasting, coersion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str , int , float , bool

print(1 + 1)
print('a' + 'b')
# print('1' + 1) erro
print('1', type('1')) # coerção
print(int('1') , type(int('1')))
print(int('1') + 1) # int
print(float('1') + 1) # float
print(bool('')) # boolean false
print(bool(' ')) # boolean false
print(str(11) + 'b') # str

# Variaveis são usadas para salvar algo na memória do computador
# PEP8 : Inicie variaveis com letras minusculas, pode usar
# numeros e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome ( variavel )
# Uso: nome_variavel = expressão

nome_completo = 'Victor Santos Rohod'
soma_dois_mais_dois = 2 + 2
int_um = int('1')

# f string - concatenação

nome = 'Luiz'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
