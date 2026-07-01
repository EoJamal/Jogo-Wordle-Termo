import random  # Biblioteca para escolher uma palavra aleatória
import sys     # Biblioteca para encerrar o programa

# Verifica se a palavra digitada possui 5 letras e tem somente letras
def valida_palavra(palavra_atual):

    if len(palavra_atual) != 5: 
        print("A palavra não possui 5 letras. O programa será encerrado!")
        sys.exit()

    for letra in palavra_atual:
        if letra < 'A' or letra > 'Z':
            print("A palavra deve conter apenas letras. O programa será encerrado!")
            sys.exit()

# Compara a palavra digitada com a palavra secreta
def testa_palavra(palavra_secreta):
    for i, letra in enumerate(palavra_atual):

        # Letra correta na posição correta
        if letra == palavra_secreta[i]:
            resultado.append(f"{verde}{letra}{reset}")
            resultado.append(" ")
            verificador.append(letra)

        # Letra existe na palavra, mas está em posição errada
        elif letra in palavra_secreta:
            resultado.append(f"{amarelo}{letra}{reset}")
            resultado.append(" ")
            verificador.append(letra)

        # Letra não existe na palavra secreta
        else:
            resultado.append(f"{vermelho}{letra}{reset}")
            resultado.append(" ")
            verificador.append(letra)

# Lista de palavras possíveis
palavras = ["amigo", "banho", "caixa", "dente", "esqui", "festa", "gosto",
            "hotel", "idade", "jogar", "lindo", "massa", "nuvem", "olhar",
            "praia", "queda", "risco", "saber", "tempo", "uniao", "verde",
            "vinho", "zebra", "bolsa", "carta", "doido", "folha", "aviao",
            "grito", "humor", "impar", "livro", "metro", "noite", "dados",
            "ossos", "poder", "quase", "roupa", "sonho", "terra", "urgir",
            "velha", "vento", "vigor"]

# Escolhe uma palavra aleatória e converte para maiúsculas
palavra_secreta = list(random.choice(palavras).upper())

# Número máximo de tentativas
tentativas = 6

# Listas auxiliares
resultado = []
verificador = []

# Códigos ANSI para cores no terminal
amarelo = "\033[1;43m"
verde = "\033[1;42m"
vermelho = "\033[1;41m"
reset = "\033[m"

print("Jogo do Termo / A palavra deve ter 5 letras")

# Loop principal do jogo
while tentativas != 0:

    # Recebe a palavra digitada pelo usuário
    palavra_atual = list(input("Digite uma palavra: ").upper())

    # Valida o tamanho da palavra
    valida_palavra(palavra_atual)

    # Testa a palavra digitada
    testa_palavra(palavra_secreta)

    # Exibe o resultado colorido
    print("".join(resultado))

    # Verifica se o usuário acertou a palavra
    if verificador == palavra_secreta:
        print("Parábens, você acertou a palavra secreta!!")
        sys.exit()

    # Limpa as listas para a próxima tentativa
    resultado.clear()
    verificador.clear()

    # Diminui uma tentativa
    tentativas -= 1

# Executado quando as tentativas acabam
print("Você perdeu, a palavra era " + "".join(palavra_secreta))