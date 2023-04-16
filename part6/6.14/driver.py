from employee import Employee

class RatioException(Exception): ...

class Driver(Employee):

    def __init__(self, name: str,
                 auto_type: str,
                 id_employee: int,
                 age: int = 20,
                 salary_ratio: float = 0.8) -> None:
        super().__init__(name, id_employee, age)
        self.__auto_type = auto_type
        self.__salary_ratio = salary_ratio

    @property
    def auto_type(self) -> str:
        return self.__auto_type

    @auto_type.setter
    def auto_type(self, new_auto_type: str) -> None:
        self.__auto_type = new_auto_type

    @property
    def salary_ratio(self) -> float:
        return self.__salary_ratio

    @salary_ratio.setter
    def salary_ratio(self, ratio: float) -> None:
        if ratio < 0.5:
            raise RatioException('salary_ratio must be >= 0.5')
        self.__salary_ratio = ratio

    def get_salary(self) -> int:
        salary = ((self.id_employee + self.age) * 
                  self.__salary_ratio)
        return int(salary * 1000)

    def __repr__(self) -> str:
        return_str = f'{self.name} is Driver, ' \
                     f'id: {self.id_employee},'
        return_str += f' age: {self.age}, ' \
                      f'auto: {self.__auto_type}'
        return return_str
