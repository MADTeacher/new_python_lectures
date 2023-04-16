from main import *


def test_sum_list() -> None:
    data = [2, 3, 4]
    assert sum_list(data) == 9


def test_splitter() -> None:
    test_str = f'Python is a dynamic language, ' \
               f'so usually you’ll only see errors ' \
               f'in your code when you attempt to run ' \
               f'it. Mypy is a static checker, so it finds ' \
               f'bugs in your programs without ' \
               f'even running them!'
    assert len(splitter(test_str, '’')) == 2
    assert len(splitter(test_str, 'is')) == 3


def test_create_person() -> None:
    name = 'Alex'
    age = 34
    is_married = False
    person = create_person(name, age, is_married)
    assert person['name'] == name
    assert person['age'] == age
    assert person['is_married'] == is_married

    name, age, is_married = 'Max', 23, True
    person = create_person(name, age, is_married)
    assert person['name'] == name
    assert person['age'] == age
    assert person['is_married'] == is_married


def test_pow_n() -> None:
    my_pow = pow_n(0)
    for it in range (1, 9):
        assert my_pow(it) == 1

    my_pow = pow_n(3)
    assert my_pow(2) == 8
