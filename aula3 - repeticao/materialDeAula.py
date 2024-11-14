"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou')

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)
    
print('acabou')

"""
Operadores de atribuição

= += -= *= /= //= **= %=
"""

contador = 2

# ao inves de contador = contador + 1
contador += 1

"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando o código não tem fim 
"""

contador = 0 

while contador <= 10:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6')
        # pula a execução atual
        continue
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o ',contador)
        continue
    
    print(contador)
    
    if contador == 40:
        # quebra a repetição atual
        break

print('Acabou')

"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando o código não tem fim 
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}{coluna=}')
        coluna += 1
    
    linha += 1

print('Acabou')

""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

texto = 'Python'

# for 
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
    
    
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)