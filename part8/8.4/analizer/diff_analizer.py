from matplotlib import pyplot as plt

from analizer.analyzer import Analyzer
from analizer.utils import get_total_progress, get_amount_tasks
from models.student import Student


def create_diff_analyzer(old_data: list[Student],
                         new_data: list[Student]) -> Analyzer:
    return _DiffAnalyzer(old_data, new_data)


class _DiffAnalyzer(Analyzer):

    def __init__(self, old_data: list[Student],
                 new_data: list[Student]):
        self.old_data = old_data
        self.new_data = new_data

    def run(self) -> None:
        old_progress = get_total_progress(self.old_data)
        new_progress = get_total_progress(self.new_data)
        self._diff_progress(old_progress, new_progress)

    def _diff_progress(self, old_progress: dict[str, int],
                       new_progress: dict[str, int]) -> None:
        diff_progress: dict[str, int] = {}
        for key, value in new_progress.items():
            diff_progress[key] = value - old_progress.get(key, 0)

        f = plt.figure()
        f.set_figwidth(15)
        f.set_figheight(5)

        plt.bar(*zip(*diff_progress.items()))
        plt.savefig('DiffProgress.png')
        plt.show()
        plt.close()
