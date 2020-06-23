class Usuario():
    def __init__(self):
        #self.__email = str(input("Digite seu email:     "))
        #self.__senha = str(input("Digite sua senha:     "))
        self.__email = "contato_joaogabriel@outlook.com"
        self.__senha = "32333529Itau"
    
    @property
    def getEmail(self):
        return self.__email
    
    @property
    def getSenha(self):
        return self.__senha