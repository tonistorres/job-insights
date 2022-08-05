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
        if element["industry"] != '':
            results.add(element["industry"])
    return [*results]


def filter_by_industry(jobs, industry):
    resul_filter = []
    for element in jobs:
        if element["industry"] == industry:
            resul_filter.append(element)
    return resul_filter


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
