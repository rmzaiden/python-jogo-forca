import logging

logging.basicConfig(format='%(message)s')
logging.getLogger().setLevel(logging.INFO)

class Forca():
    """
    Class representing Forca game object
    """
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.erro = 0
        self.enforcou = False
        self.acertou = False
        self.letras_acertadas = ["_" for letter in self.palavra_secreta]

    def play(self) -> None:
        """
        """
        while (not self.enforcou and not self.acertou):

            if self.erro == 7:
                self._imprime_mensagem_perdedor(self.palavra_secreta)
                self.enforcou = True
            else:
                chute = input("\nQual letra? ")
                chute = chute.strip().upper()

                self._valida_chute(chute)

                resposta = ''.join(self.letras_acertadas)

                if resposta == self.palavra_secreta:
                    self._imprime_mensagem_vencedor(resposta)
                    self.acertou = True
                else:
                    logging.info("jogando ..")

        logging.info("Fim do jogo")

    def _valida_chute(self, chute: str) -> None:
        """
        Args:
            palavra_secreta (str): Palavra a ser descoberta pelo jogador
            letras_acertadas (list[str]): lista de letras acertadas
            erro (int): Quantidade de erros
            chute (str): letra da tentativa
        """
        if chute.upper() in self.palavra_secreta.upper() and chute not in self.letras_acertadas:
            posicoes_para_alterar = [x for x, v in enumerate(self.palavra_secreta) if v == chute]
            for posicao in posicoes_para_alterar:
                self.letras_acertadas[posicao] = chute
            logging.info(' '.join(self.letras_acertadas))
        elif chute.upper() in self.palavra_secreta.upper():
            logging.info("Palavra %s já informada anteriormente", chute)
        else:
            self.erro += 1
            logging.info("\n|--- ERROU! ---|")
            self.desenha_forca()
            #print("Palavra incompleta ainda: " + ' '.join(self.letras_acertadas))
        logging.info("Quantidade de tentativas erradas %s:", self.erro)

    def desenha_forca(self) -> None:
        logging.info("  _______     ")
        logging.info(" |/      |    ")

        if(self.erro == 1):
            logging.info(" |      (_)   ")
            logging.info(" |            ")
            logging.info(" |            ")
            logging.info(" |            ")

        if(self.erro == 2):
            logging.info(" |      (_)   ")
            logging.info(" |      \     ")
            logging.info(" |            ")
            logging.info(" |            ")

        if(self.erro == 3):
            logging.info(" |      (_)   ")
            logging.info(" |      \|    ")
            logging.info(" |            ")
            logging.info(" |            ")

        if(self.erro == 4):
            logging.info(" |      (_)   ")
            logging.info(" |      \|/   ")
            logging.info(" |            ")
            logging.info(" |            ")

        if(self.erro == 5):
            logging.info(" |      (_)   ")
            logging.info(" |      \|/   ")
            logging.info(" |       |    ")
            logging.info(" |            ")

        if(self.erro == 6):
            logging.info(" |      (_)   ")
            logging.info(" |      \|/   ")
            logging.info(" |       |    ")
            logging.info(" |      /     ")

        if (self.erro == 7):
            logging.info(" |      (_)   ")
            logging.info(" |      \|/   ")
            logging.info(" |       |    ")
            logging.info(" |      / \   ")

        logging.info(" |            ")
        logging.info("_|___         ")

    def _imprime_mensagem_vencedor(self, resposta):
        logging.info("Parabéns, você acertou a resposta, que era a palavra %s",  resposta)
        logging.info("       ___________      ")
        logging.info("      '._==_==_=_.'     ")
        logging.info("      .-\\:      /-.    ")
        logging.info("     | (|:.     |) |    ")
        logging.info("      '-|:.     |-'     ")
        logging.info("        \\::.    /      ")
        logging.info("         '::. .'        ")
        logging.info("           ) (          ")
        logging.info("         _.' '._        ")
        logging.info("        '-------'       ")        

    def _imprime_mensagem_perdedor(self, resposta):
        logging.info("Puxa, você foi enforcado!")
        logging.info("A palavra era %s", resposta)
        logging.info("    _______________         ")
        logging.info("   /               \       ")
        logging.info("  /                 \      ")
        logging.info("//                   \/\  ")
        logging.info("\|   XXXX     XXXX   | /   ")
        logging.info(" |   XXXX     XXXX   |/     ")
        logging.info(" |   XXX       XXX   |      ")
        logging.info(" |                   |      ")
        logging.info(" \__      XXX      __/     ")
        logging.info("   |\     XXX     /|       ")
        logging.info("   | |           | |        ")
        logging.info("   | I I I I I I I |        ")
        logging.info("   |  I I I I I I  |        ")
        logging.info("   \_             _/       ")
        logging.info("     \_         _/         ")
        logging.info("       \_______/           ")