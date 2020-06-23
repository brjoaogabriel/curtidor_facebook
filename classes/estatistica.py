#..............................Logs.........................................
#   22/06/2020  - Iniciando testes na classe Estatistica
#       21:40   - Início de testes
#       22:00   - Finalização de testes
#       22:00   - Classe aprovada
#       22:05   - Classe finalizada

#.........................Explicação.........................................
#   Classe utilizada para contabilizar
#   -   Quantidade de likes dados
#   -   Horario inicial de disparo de likes
#   -   Horario final de disparo de likes
#   -   Auxílio na emição de relatório final

#........................Observaçõoes.........................................
#       A classe já determina o momento em que o disparo começou
#       a partir do momento em que é instanciada, mas a finalização
#       precisa ser informada através do método Encerra()

import datetime as dt

class Estatistica():
    def __init__(self):
        self.__qtde_likes = 0
        self.__horario_inicial = dt.datetime.now()
        self.__horario_final = 0
        self.stats = []

    @property
    def getQtdeLikes(self):
        return self.__qtde_likes

    @property   
    def getHorarioInicial(self):
        return self.__horario_inicial
    
    @property
    def getHorarioFinal(self):
        return self.__horario_final
    
    @property
    def getStats(self):
        return self.stats

    def setStats(self, id, data):
        self.stats.append({'id': 1, 'datetime': data})

    def Encerra(self):
        self.__horario_final = dt.datetime.now()