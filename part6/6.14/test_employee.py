from employee import Employee


def test_create_employee():
    try:
        employee = Employee('Alex', 1, 34)
        raise Exception('Employee is not abstract class')
    except TypeError as er:
        ...
