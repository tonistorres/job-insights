# linha para execução via terminal
from jobs import read

path = "jobs.csv"


def industries(path):
    dict = read(path)
    industries = []
    for job in dict:
        if job["industry"] != "":
            industries.append(job["industry"])
    return [*set(industries)]


def filter_by_industry(jobs, industry):
    resul_filter = []
    for element in jobs:
        if element["industry"] == industry:
            resul_filter.append(element)
    return resul_filter


data = industries(path)
print(data)

arr_results = filter_by_industry(data, 'Oil')
print(arr_results)


# def industries_list_test(path):
#     dict = read(path)
#     results = set()
#     for element in dict:
#         if element["industry"] != '':
#             results.add(element["industry"])
#     return [*results]
