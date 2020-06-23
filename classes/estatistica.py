class Estatistica():
    def __init__(self):
        self.__qtde_likes = 0
        self.__horario_inicial = dt.datetime.now()
        self.__horario_final = 0
        self.__stats = {  'id': [],
                        'datetime': []}

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
    def Stats(self):
        return self.__stats

    @Stats.setter
    def Stats(self, id, datetime):
        self.__stats['id'].append(id)
        self.__stats['datetime'].append(datetime)