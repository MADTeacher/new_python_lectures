from sqlalchemy import delete, select

from database.configuration import Session
from models.employee import Employee
from models.shift import Shift


def add_employee(name: str, position: str) -> int:
    with Session() as session:
        employee = Employee(name=name, position=position)
        session.add(employee)
        session.commit()
        return employee.id


def add_shift(employee_id: int, start_time: str, end_time: str) -> None:
    with Session() as session:
        employee = session.get(Employee, employee_id)
        employee.shift.append(
            Shift(start_time=start_time, end_time=end_time)
        )
        session.commit()


def delete_employee(employee_id: int) -> None:
    with Session() as session:
        smt = delete(Employee).where(Employee.id == employee_id)
        session.execute(smt)
        session.commit()


def delete_shift(employee_id: int) -> None:
    ...


def get_employees() -> list:
    with Session() as session:
        employees = session.execute(
            select(
                Employee.id,
                Employee.name,
                Employee.position
            )
        ).all()
        return employees


def get_employees_with_shifts() -> list:
    with Session() as session:
        employee = session.execute(
            select(
                Employee.id,
                Employee.name,
                Employee.position,
                Shift.start_time,
                Shift.end_time,
            ).join(Shift, Shift.employee_id == Employee.id)
        ).all()
        return employee
