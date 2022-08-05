# linha para execução via terminal
from jobs import read

path = "jobs.csv"


def industries(path):
    dict = read(path)
    industries = []
    for element in dict:
        if element["industry"] != "":
            industries.append(element["industry"])
    return [*set(industries)]


def filter_by_industry(jobs, industry):
    resul_filter = []
    for element in jobs:
        if element["industry"] == industry:
            resul_filter.append(element)
    return resul_filter


pass
