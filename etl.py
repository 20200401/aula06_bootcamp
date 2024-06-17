#Dado um arquivo CSV contendo dados de vendas, o desafio consiste em ler os dados, processa-los
#em um dicionario para analise e, por fim, calcular e reportar totais por categoria de produto.

import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    #Funcao que le um arquivo csv e retorna uma lista de dicionario
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo)
print(vendas_itens)