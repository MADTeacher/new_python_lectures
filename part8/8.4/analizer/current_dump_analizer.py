import numpy as np
from matplotlib import pyplot as plt

from analizer.analyzer import Analyzer
from analizer.utils import get_total_progress, get_amount_tasks
from models.student import Student


def create_dump_analyzer(students: list[Student]) -> Analyzer:
    return _CurrentDumpAnalyzer(students)


class _CurrentDumpAnalyzer(Analyzer):

    def __init__(self, students: list[Student]):
        self.students = students

    def run(self) -> None:
        total_progress = get_total_progress(self.students)
        self._total_done_tasks(total_progress)
        self._tasks_left(total_progress)

    def _total_done_tasks(self, total_progress: dict[str, int]) -> None:
        f = plt.figure()
        f.set_figwidth(15)
        f.set_figheight(5)

        plt.bar(*zip(*total_progress.items()))
        plt.savefig('TotalDone.png')
        plt.show()
        plt.close()


    def _tasks_left(self, total_progress: dict[str, int]) -> None:
        amount_tasks = get_amount_tasks(self.students)
        names = total_progress.keys()

        values = np.array(list(total_progress.values()))
        values = values / amount_tasks

        f = plt.figure()
        f.set_figwidth(15)
        f.set_figheight(5)
        plt.bar(names, values)
        plt.savefig('TasksLeft.png')
        plt.show()