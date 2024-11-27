# Palavra secreta
palavra_secreta = "python"
letras_palavra = set(palavra_secreta)  # Conjunto com as letras únicas da palavra
letras_digitadas = set()  # Conjunto para rastrear letras digitadas
tentativas = 6  # Número máximo de erros

print("Bem-vindo ao Jogo da Forca!")

while tentativas > 0 and letras_palavra:
    # Exibe o estado atual da palavra
    palavra_exibida = []
    for letra in palavra_secreta:
        if letra in letras_digitadas:
            palavra_exibida.append(letra)
        else:
            palavra_exibida.append("_")
    print("Palavra:", " ".join(palavra_exibida))

    # Pede ao usuário uma letra
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi usada
    if letra in letras_digitadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    # Adiciona a letra ao conjunto de tentativas
    letras_digitadas.add(letra)

    # Verifica se a letra está na palavra
    if letra in letras_palavra:
        print(f"Boa! A letra '{letra}' está na palavra.")
        letras_palavra.remove(letra)
    else:
        print(f"Ops! A letra '{letra}' não está na palavra.")
        tentativas -= 1

    print(f"Tentativas restantes: {tentativas}")

# Verifica se o jogador ganhou ou perdeu
if not letras_palavra:
    print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
else:
    print(f"Game over! A palavra era: {palavra_secreta}")