class Facebook():
    def __init__(self):
        self.__curtir = "_666k"
        self.__email = "email"
        self.__senha = "pass"
        self.__login = "loginbutton"
        self.__pubs = "_3ccb"
        self.__publicacoes = []

    @property
    def getCurtir(self):
        return self.__curtir

    @property
    def getEmail(self):
        return self.__email
    
    @property
    def getSenha(self):
        return self.__senha

    @property
    def getLogin(self):
        return self.__login

    @property
    def getPubs(self):
        return self.__pubs

    @property
    def getPubs(self):
        return self.__publicacoes

    @getPubs.setter
    def setPubs(self, webelem):
        self.__publicacoes = webelem