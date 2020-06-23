class Caminhos():
    def __init__(self):
        self.__gecko = "geckodriver.exe"
        self.__facebook = "https://www.facebook.com/"
        #self.__alvo = str(input("\nDigite o link do perfil do alvo:   "))# 
        self.__alvo = "https://www.facebook.com/fernanda.thf"

    @property
    def getGecko(self):
        return self.__gecko

    @property
    def getFacebook(self):
        return self.__facebook

    @property
    def getAlvo(self):
        return self.__alvo