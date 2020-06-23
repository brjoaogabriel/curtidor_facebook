#   Importa classe que executa o bot
from classes.navegador import *
from errors.text       import *

#   Instanciando o bot
try:
    Bot = Navegador()

    #   Abrindo o facebook
    try:
        Bot.AbreFacebook()
    else:
        print(Erros().E2)
        exit()

    #   Fazendo login no facebook
    try:
        Bot.FazerLogin()
    else:
        print(Erros().E3)
        exit()

    #   Visitando o alvo
    try:
        Bot.VisitaAlvo()
    else:
        print(Erros().E4)
        exit()

    #   Curte Publicações
    try:
        Bot.CurtePublicacoes()
    else:
        print(Erros().E5)
        exit()

    #   Encerra execução
    try:
        Bot.Encerra()
    else:
        print(Erros().E6)
        exit()
else:
    print(Erros().E1)
    exit()