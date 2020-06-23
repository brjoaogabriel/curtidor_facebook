#..............................Logs.........................................
#   22/06/2020  - Iniciando testes na classe Navegador
#       22:15   - Início de testes
#       22:30   - Prorrogação de testes
#       22:38   - Agora as publicações não ficam mais salvas
#       23:22   - Aplicação finalizada

#.........................Explicação.........................................
#   Classe utilizada para definir tarefas realizadas no webdriver
#   Entre as tarefas, estão:
#   -   Abrir o facebook
#   -   Fazer Login
#   -   Visitar o alvo
#   -   Curtir publicações

#........................Observaçõoes.........................................
#       A classe tem valores constantes, a alteração de dados no site
#       do Facebook acarreterá em bugs de produção por conta dessa classe

#   Importando classes que vão alimentar o navegador com informações
from classes.estatistica                import *
from classes.facebook                   import *
from classes.caminhos                   import *
from classes.usuario                    import *

#   Importando biblioteca responsável pela interação com a web
from selenium                           import webdriver
from selenium.webdriver                 import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by       import By

class Navegador():
    def __init__(self):
        self.__options = Options()
        self.__options.page_load_strategy = "normal"
        self.__driver = Firefox(executable_path=Caminhos().getGecko, options=self.__options)

    def AbreFacebook(self):
        self.__driver.get(Caminhos().getFacebook)

    def FazerLogin(self):
        self.__driver.find_element(By.ID, Facebook().getEmail).send_keys(Email().getEmail)
        self.__driver.find_element(By.ID, Facebook().getSenha).send_keys(Senha().getSenha)
        try:
            self.__driver.find_element(By.ID, Facebook().getLogin).click()
        except:
            self.__driver.find_element(By.ID, Facebook().getLogin2).click()

    def VisitaAlvo(self):
        self.__driver.get(Caminhos().getAlvo)

    def ListaPublicacoes(self):
        return self.__driver.find_elements(By.CLASS_NAME, Facebook().getPubs)

    def CurtePublicacoes(self):
        for publicacao in self.ListaPublicacoes():
            publicacao.find_element(By.CLASS_NAME, Facebook().getCurtir).click()

    def Encerra(self):
        self.__driver.close()
        self.__driver = None