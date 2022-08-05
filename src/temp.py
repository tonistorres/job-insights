# linha para execução via terminal
from jobs import read

path = "jobs.csv"


def get_file_print_max_salries(path):
    dict = read(path)
    arry_values = []
    for dic in dict:
        if dic["max_salary"] != "":
            arry_values.append(int(dic["max_salary"]))
    # https://www.tutorialspoint.com/python/list_max.htm
    return max(arry_values)


result_max_value_list = get_file_print_max_salries(path)
print(result_max_value_list)

# def get_file_unic(path):
#     dict = read(path)
#     for dic in dict:
#         print(dic)


# get_file_unic(path)

# result_unic = get_unique_job_types(path)
# print("-------- Types unic:------")
# print(result_unic)
# print("--------------------------")

# resultado = get_max_salary(path)
# print("--- Max Value Salries: ---")
# print(resultado)
# print("--------------------------")
