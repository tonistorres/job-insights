# linha para execução via terminal
from jobs import read

path = "jobs.csv"


def industries(path):
    dict = read(path)
    industries = []
    for job in dict:
        if job["industry"] != '':
            industries.append(job["industry"])
    return [*set(industries)]


def industries_list_test(path):
    dict = read(path)
    results = set()
    for element in dict:
        if element["industry"] != '':
            results.add(element["industry"])
    return [*results]


arr_results = industries_list_test(path)
print(arr_results)
