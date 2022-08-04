import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        # Leitor e o escritor baseados em dicionários DictReader
        # Vantagem - não precisamos manipular os índices para acessar os dados
        # colunas
        # Desvantagem - o espaço ocupado em memória (que é maior que o comum),
        # devido à estrutura de dados utilizada.
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        # Usando o conceito de desempacotamento
        header, *data = jobs
        return [header, *data]
    pass



