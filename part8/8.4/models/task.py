from dataclasses import dataclass


@dataclass
class Task:
    task_name: str
    is_done: bool
