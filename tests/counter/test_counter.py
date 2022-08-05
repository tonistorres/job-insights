from src.counter import count_ocurrences


def test_counter():
    word_count = count_ocurrences("src/jobs.csv", "Python")
    # verificar se o retorno da função count_ocurrences é um inteiro
    assert type(word_count) == int
    # verificar se inteiro verificar se é o numero de ocorrencias da palavra
    # Python é 1639
    assert word_count == 1639
    word_count = count_ocurrences("src/jobs.csv", "python")
    # verificar se o retorno da função count_ocurrences é um inteiro
    assert type(word_count) == int
    # verificar se inteiro verificar se é o numero de ocorrencias da palavra
    # python é 1639
    assert word_count == 1639
    word_count = count_ocurrences("src/jobs.csv", "zero")
    # verificar se ao passar zero no parametro retorna um número inteiro
    assert type(word_count) == int
    # se for inteiro retorna o numero 14
    assert word_count == 14


pass
