class Navegador():
    def __init__(self):
        self.__options = Options()
        self.__options.page_load_strategy = "normal"
        self.__driver = Firefox(executable_path=caminho, options=self.__options)

    def AbreFacebook(self):
        self.__driver.get(Caminhos.getFacebook)

    def FazLogin(self):
        self.__driver.find_element(By.ID, Facebook.getEmail).send_keys(login_email)
        self.__driver.find_element(By.ID, Facebook.getSenha).send_keys(login_senha)
        self.__driver.find_element(By.ID, Facebook.getLogin).click()

    def VisitaAlvo(self):
        self.__driver.get(Caminhos.getAlvo)

    def ListaPublicacoes(self):
        Facebook.setPubs = self.__driver.find_elements(By.CLASS_NAME, Facebook.getPubs)

    def CurteListadas(self):
        for publicacao in Facebook.getPubs:
            publicacao.find_element(By.CLASS_NAME, Facebook.getCurtir)
        publicacao = None

    def Encerra(self):
        self.__driver.close()
        self.__driver = None