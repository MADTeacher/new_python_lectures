import pytest

from driver import Driver, RatioException
from employee import Employee


@pytest.fixture
def driver() -> Driver:
    return Driver(
        name='Alex',
        age=27,
        id_employee=2,
        salary_ratio=0.6,
        auto_type='Lada'
    )


def test_create_driver(driver):
    assert isinstance(driver, Employee)
    assert driver.name == 'Alex'
    assert driver.age == 27
    assert driver.id_employee == 2
    assert driver.salary_ratio == 0.6
    assert driver.auto_type == 'Lada'


def test_change_age(driver):
    try:
        driver.age = 45
        assert False, "can't change age"
    except AttributeError as ex:
        ...
    driver.increment_age()
    assert driver.age == 28


def test_change_name(driver):
    try:
        driver.name = 'Max'
        assert False, "can't change name"
    except AttributeError as ex:
        ...


def test_change_id(driver):
    try:
        driver.id_employee = 40
        assert False, "can't change id_employee"
    except AttributeError as ex:
        ...


def test_change_auto_type(driver):
    driver.auto_type = 'Oka'
    assert driver.auto_type == 'Oka'


def test_change_salary_ratio(driver):
    driver.salary_ratio = 0.75
    assert driver.salary_ratio == 0.75
    try:
        driver.salary_ratio = 0.4
    except RatioException:
        ...


def test_salary(driver):
    assert driver.get_salary() == 17400

    driver.salary_ratio = 0.75
    assert driver.get_salary() == 21750
