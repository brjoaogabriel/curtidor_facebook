#..............................Logs.........................................
#   22/06/2020  - Iniciando testes na classe Erros
#       23:32   - Iniciando testes
#       23:40   - Finalização de testes

#.........................Explicação.........................................
#   Classe utilizada para guardar os tipos de mensagem de erro

#........................Observaçõoes.........................................
#       A classe tem valores constantes

#............TIPOS DE ERROS CONHECIDOS E TRATADOS.............................
#       E1......Erro ao instanciar Navegador
#       E2......Erro ao abrir Facebook
#       E3......Erro ao realizar Login
#       E4......Erro ao Visitar Alvo
#       E5......Erro ao Curtir Publicações
#       E6......Erro ao encerrar webdriver

class Erros():
    def __init__(self):
        self.__E1 = "Erro ao instanciar Navegador"
        self.__E2 = "Erro ao abrir Facebook"
        self.__E3 = "Erro ao realizar Login"
        self.__E4 = "Erro ao Visitar Alvo"
        self.__E5 = "Erro ao Curtir Publicações"
        self.__E6 = "Erro ao encerrar webdriver"

    @property
    def E1(self):
        return self.__E1

    @property
    def E2(self):
        return self.__E2

    @property
    def E3(self):
        return self.__E3

    @property
    def E4(self):
        return self.__E4

    @property
    def E5(self):
        return self.__E5

    @property
    def E6(self):
        return self.__E6