# operadores logicos
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplição', multiplicacao)

divisao = 10 / 2.2
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2
print('Módulo', modulo)

# prioridade
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** (5 + 5)
conta_3 = (1 + (0.5 * 0.5)) ** (5 + 5)

print(conta_1)
print(conta_2)
print(conta_3)

# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair')     

print('FORA DOS BLOCOS')

"""
Operadores de comparação (relacionais)
OP ---- Significado ------- Exemplo (True)
> ----- maior ------------- Exemplo (True)
>= ---- maior ou igual ---- Exemplo (True)
< ----- menor ------------- Exemplo (True)
<= ---- menor ou igual ---- Exemplo (True)
== ---- igual ------------- Exemplo (True)
!= ---- diferente --------- Exemplo (True)
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que o {segundo_valor}')
else:
    print(f'{segundo_valor} é maior que o {primeiro_valor}')


# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam 
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falso ( que você já viu )
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
# Avaliação de curso circuito
print(True and False and True)
print(True and 0 and True)