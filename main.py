import re
from bot import mybot
import pandas as pd

global planilha
planilha = pd.read_excel('caixnha.xslx')

bot = mybot('DM')

for i, j in planilha.iterrows():
    for coluna in i:
        bot.inicia(coluna)
        bot.saudacao(['Oi! Sou o dm Keller. Use :: para checar sua situação financeira no time!'])
        ultimo_texto = ''
        while True:
            texto = bot.escuta()
            if texto != ultimo_texto and re.match(r'^::', texto):
                ultimo_texto = texto
                texto = texto.replace('::', '')
                texto = texto.lower()
                response = 'Você deve: {0}'.format(planilha[coluna, j + 1])
                bot.responde(texto)
                

