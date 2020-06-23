#..............................Logs.........................................
#   22/06/2020  - Iniciando testes na classe Navegador
#       22:27   - Início de testes
#       22:28   - Finalização dos testes

#.........................Explicação.........................................
#   Classe utilizada para guardar caminhos de
#   -   Webdriver
#   -   Facebook
#   -   Alvo do facebook

#........................Observaçõoes.........................................
#       A classe tem valores constantes, a alteração de dados no site
#       do Facebook acarreterá em bugs de produção por conta dessa classe

class Caminhos():
    def __init__(self):
        self.__gecko = "geckodriver.exe"
        self.__facebook = "https://www.facebook.com/"
        self.__alvo = ""

    @property
    def getGecko(self):
        return self.__gecko

    @property
    def getFacebook(self):
        return self.__facebook

    @property
    def getAlvo(self):
        self.setAlvo = str(input("\nDigite o link do perfil do alvo:   "))
        print()
        return self.__alvo

    @getAlvo.setter
    def setAlvo(self, alvo):
        self.__alvo = alvo