#..............................Logs.........................................
#   22/06/2020  - Iniciando testes nas classes Email e Senha
#       22:30   - Início dos testes
#       22:55   - Alteração de classe Usuario para classe Email e Senha
#       22:56   - Finalização de testes

#.........................Explicação.........................................
#   Classe utilizada para solicitar dados do usuário, como:
#   -   Email
#   -   Senha

#........................Observaçõoes.........................................
#       O módulo não é responsável por validar se o usuário
#           acertou ou não a senha

class Email():
    def __init__(self):
        self.__email = str(input("\nDigite seu email:     "))

    @property
    def getEmail(self):
        return self.__email

class Senha():
    def __init__(self):
        self.__senha = str(input(  "Digite sua senha:     "))
    
    @property
    def getSenha(self):
        return self.__senha