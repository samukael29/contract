# essa linha importa os recursos
import json, requests
import pandas as pd

def get_ibge():
    name = "Samuel Andrade de Souza"

    # essa linha pega os recursos do link e atribui a variavel
    connection_string = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    print(connection_string)
    response = requests.get(connection_string)

    # realiza a conversão do response para um formato acessível ao python
    json_data = json.loads(response.text)

    # imprime na tela o valor do primeiro ano do censo - demonstração de navegação
    print(json_data)
    # print(json_data[0]['res'][0])

def get_deputados():
    url        = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    parametros = {}
    resposta   = requests.request("GET", url, params=parametros)
    objetos    = json.loads(resposta.text)
    dados      = objetos['dados']
    dataframe = pd.DataFrame(dados)
    dataframe.head()
    i = 1
    for item in dataframe.index:
        print(i,dataframe['nome'][item])
        i=i+1

def get_deputados_paramethers():
    url              = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    parametros       = {'id': 204521}
    resposta         = requests.request("GET", url, params=parametros)
    objetos          = json.loads(resposta.text)
    dados_parametros = objetos['dados']

    dataframe = pd.DataFrame(dados_parametros)
    dataframe.head()
    print(dataframe)
    # for item in dataframe.index:
    #     print(),dataframe['nome'][item])


get_deputados()