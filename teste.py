#   Importando webdriver e firefox
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

path_gecko = "geckodriver.exe"
path_facebook = "https://www.facebook.com/"
path_alvo = "https://www.facebook.com/fernanda.thf"
login_email = "contato_joaogabriel@outlook.com"
login_senha = "32333529Itau"

#   Definindo estratégia de carregamento
options = Options()
options.page_load_strategy = "normal"

#   Instanciando driver
driver = Firefox(executable_path=path_gecko, options=options)

#   Indo até a página do facebook
driver.get(path_facebook)

#   Realizando login
driver.find_element(By.ID, "email").send_keys(login_email)
driver.find_element(By.ID, "pass").send_keys(login_senha)
driver.find_element(By.ID, "loginbutton").click()

#   Indo até o perfil alvo
driver.get(path_alvo)

#   Criando dicionário que vai suportar os dados extraídos do perfil
dados = {   'autor': [],
            'tempo': [],
            'curtidores': []}

#   Carrega dados da publicação
class_autor = "_5pb8 n_19fygwlcg6 _8o _8s lfloat _ohe"
class_tempo = "_5ptz timestamp livetimestamp"
class_curtidores = "_81hb"
class_curtir = "_666k"

input("Aperte ENTER...")