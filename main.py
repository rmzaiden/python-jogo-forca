import random
from Forca import Forca

def _load_secret_word():
    palavras = []

    with open("palavras.txt", encoding='utf-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    numero = random.randrange(0, len(palavras))

    return palavras[numero].upper()

if __name__ == '__main__':

    palavra_secreta = _load_secret_word()

    jogo_forca = Forca(palavra_secreta)
    jogo_forca.play()