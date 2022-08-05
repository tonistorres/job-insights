from src.jobs import read


def get_unique_job_types(path):
    dict = read(path)
    types = []
    for job in dict:
        types.append(job["job_type"])
    return [*set(types)]


def filter_by_job_type(jobs, job_type):
    type = []
    for job in jobs:
        if job["job_type"] == job_type:
            type.append(job)
    return type


def get_unique_industries(path):
    dict = read(path)
    results = set()
    for element in dict:
        if element["industry"] != "":
            results.add(element["industry"])
    return [*results]


def filter_by_industry(jobs, industry):
    resul_filter = []
    for element in jobs:
        if element["industry"] == industry:
            resul_filter.append(element)
    return resul_filter


pass


def get_max_salary(path):
    dict = read(path)
    arry_values = []
    for dic in dict:
        # https://www.w3schools.com/python/ref_string_isdigit.asp
        if dic["max_salary"].isdigit():
            arry_values.append(int(dic["max_salary"]))
    # https://www.tutorialspoint.com/python/list_max.htm
    return max(arry_values)


pass


def get_min_salary(path):
    dict = read(path)
    arry_values = []
    for dic in dict:
        # https://www.w3schools.com/python/ref_string_isdigit.asp
        if dic["min_salary"].isdigit():
            arry_values.append(int(dic["min_salary"]))
    # https://www.tutorialspoint.com/python/list_max.htm
    return min(arry_values)


pass


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("'max_salary' or 'min_salary' is undefined")

    elif (
        type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
    ):
        raise ValueError("'max_salary' or 'min_salary' is not an integer")

    elif type(salary) is not int:
        raise ValueError("'salary' is not an integer")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("'min_salary' is higher than 'max_salary'")

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    return salary in range(min_salary, max_salary)


pass


def filter_by_salary_range(jobs, salary):
    arr = []
    for element in jobs:
        try:
            if matches_salary_range(element, salary):
                arr.append(element)
        except ValueError:
            print("ValueError")
    return arr


pass
