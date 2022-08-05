def count_ocurrences(path, word):
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count


pass

# resultsPython = count_ocurrences('jobs.csv', "Python")
# print('-----Testando a palavra Python passada como argumento-----')
# print(type(resultsPython))
# print(resultsPython)
# print('-----Testando a palavra python passada como argumento-----')
# resultspython = count_ocurrences('jobs.csv', "python")
# print(type(resultspython))
# print(resultspython)
# print('-----Testando a palavra zero passada como argumento-----')
# resultszero = count_ocurrences('jobs.csv', "zero")
# print(type(resultszero))
# print(resultszero)
