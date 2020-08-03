import pandas as pd
import os

path = os.getcwd()
print(path)
listaAtletas = []
somaCobrancas = []
df = pd.read_excel(r"C:\Users\sophi\Documents\Planilha.xlsx", index_col=0)
df.dropna()
nomes = list(df.index)
nomes = nomes[3::]
nomes = [x for x in nomes if x != 'nan']

for nome in nomes:
    listaAtletas.append(nomes)
    if pd.isnull(nome) == False:
        nomePessoa = "{0}".format(nome)
        for cobranca in df.loc[nomePessoa]:
            if isinstance(cobranca, int):
                print(cobranca)
                # somaCobrancas += cobranca
            else:
                break
            # somaCobrancas += cobranca
    print('pessoa: {0} deve {1}'.format(nomePessoa, cobranca))


class Pessoa:
    def __init__(self, nome, divida):
        self.nome = nome
        self.divida = divida


class Time:
    def __init__(self, pessoas):
        self.pessoas = pessoas


def createDictFromName(name, divida):
    dict = {
        "nome": nome,
        "divida": divida
    }
    return dict
