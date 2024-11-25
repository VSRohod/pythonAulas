"""
1. Encontrar alunos que cursam apenas uma disciplina
Problema:
Dado dois conjuntos:

matematica com os nomes dos alunos que fazem Matemática
fisica com os nomes dos alunos que fazem Física

Encontre os alunos que fazem apenas uma das disciplinas.
"""

matematica = {"Ana", "Pedro", "João", "Clara"}
fisica = {"João", "Clara", "Lucas", "Mariana"}
apenas_uma = matematica.symmetric_difference(fisica)
print(f"Alunos que fazem apenas uma disciplina: {apenas_uma}")

"""
2. Combinar inventários de lojas
Problema:
Duas lojas possuem estoques diferentes de produtos. Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.
"""

loja1 = {"TV", "Geladeira", "Fogão", "Celular"}
loja2 = {"Celular", "Notebook", "Fogão", "Câmera"}

comum = loja1.intersection(loja2)
exclusivo_loja1 = loja1.difference(loja2)
exclusivo_loja2 = loja2.difference(loja1)

print(f"Produtos em ambas as lojas: {comum}")
print(f"Exclusivos da loja 1: {exclusivo_loja1}")
print(f"Exclusivos da loja 2: {exclusivo_loja2}")

"""
4. Eliminar palavras repetidas em um texto
Problema:
Dado um texto como uma lista de palavras, elimine as palavras repetidas e exiba as palavras únicas em ordem alfabética.
"""

texto = ["o", "gato", "correu", "para", "o", "telhado", "o", "gato", "miou"]
palavras_unicas = set(texto)
palavras_ordenadas = sorted(palavras_unicas)
print(f"Palavras únicas em ordem alfabética: {palavras_ordenadas}")

