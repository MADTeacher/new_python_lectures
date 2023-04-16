from dataclasses import dataclass, field

from models.task import Task


@dataclass
class Student:
    user_id: int
    last_name: str
    first_name: str
    tasks: dict[str, list[Task]] = field(default_factory=dict)

