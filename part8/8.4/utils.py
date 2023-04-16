import json

from models.student import Student
from models.task import Task


def save(students: list[Student], path: str) -> None:
    with open(f'{path}.json', 'w') as json_file:
        json_file.write(json.dumps(students,
                                   default=lambda x: x.__dict__, indent=4))


def load(path: str) -> list[Student]:
    with open(path) as json_file:
        students: list[Student] = []
        data = json.load(json_file)
        for it in data:
            student = Student(
                it['user_id'],
                it['last_name'],
                it['first_name'],
            )
            for key, value in it['tasks'].items():
                student.tasks[key] = []
                for task in value:
                    student.tasks[key].append(
                        Task(
                            task['task_name'],
                            task['is_done'],
                        )
                    )
            students.append(student)
        return students
