# linha por causa do teste
from curses.ascii import isdigit
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
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return []


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


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
