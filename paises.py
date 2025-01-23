import json
import sys

import requests

url_all = 'https://restcountries.com/v2/all'
url_name = 'https://restcountries.com/v2/name'

def requisicao(url):
    try:
        resposta = requests.get(url, verify=False)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição em: ', url)

def parsing(text_da_resposta):
    try:
        return json.loads(text_da_resposta) # PARSING DE JSON PARA PYTHON
    except:
        print("Erro ao fazer parsing")

def contagem_de_paises():
    resposta = requisicao(url_all)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao(f'{url_name}/{nome_do_pais}')
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print(f'{pais['name']}: {pais['population']} habitantes')
    else:
        print("País não encontrado")

def mostrar_moeda(nome_do_pais):
    resposta = requisicao(f'{url_name}/{nome_do_pais}')
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"Moeda do {pais['name']}:")
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f'{moeda['name']} - {moeda['code']}')
    else:
        print("País não encontrado")

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Bem-vindo ao sistema de países ##")
        print("Uso: python paises.py <acao> <nome do país>")
        print('Ações: contagem, moeda, população')
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            num_de_paises = contagem_de_paises()
            print(f'Existem {num_de_paises} países no mundo todo...')
        elif argumento1 == 'moeda':
            mostrar_moeda(ler_nome_do_pais())
        elif argumento1 == 'população':
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Agumento inválido")
            
