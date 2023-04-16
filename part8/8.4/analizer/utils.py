from models.student import Student


def get_total_progress(students: list[Student]) -> dict[str, int]:
    total_progress = {}
    for it in students:
        total_progress[it.last_name] = 0
        for key, value in it.tasks.items():
            for task in value:
                if task.is_done:
                    total_progress[it.last_name] += 1
    return total_progress


def get_amount_tasks(students: list[Student]) -> int:
    amount_task = 0
    for key, value in students[0].tasks.items():
        amount_task += len(value)
    return amount_task
