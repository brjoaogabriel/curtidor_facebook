#..............................Logs.........................................
#   22/06/2020  - Iniciando testes na classe Facebook
#       22:06   - Início de testes
#       22:15   - Classe validada

#.........................Explicação.........................................
#   Classe utilizada para guardar class_names de
#   -   Botão de curtir
#   -   Botão de realizar login
#   -   Inputbox de email
#   -   Inputbox de senha
#   -   Frame da publicação

#........................Observaçõoes.........................................
#       A classe tem valores constantes, a alteração de dados no site
#       do Facebook acarreterá em bugs de produção por conta dessa classe

class Facebook():
    def __init__(self):
        self.__curtir = "_666k"
        self.__email = "email"
        self.__senha = "pass"
        self.__login = "loginbutton"
        self.__login2 = "u_0_b"
        self.__pubs = "_3ccb"

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
    def getLogin2(self):
        return self.__login2

    @property
    def getPubs(self):
        return self.__pubs