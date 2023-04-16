from models.driver import Driver
from loader.driver_loader import DriverTxtLoader, DriverJsonLoader
from models.employee import Employee
from models.manager import Manager
from loader.manager_loader import ManagerJsonLoader, ManagerTxtLoader
from models.waiter import Waiter
from loader.waiter_loader import WaiterJsonLoader, WaiterTxtLoader


class WorkersLoader:
    def __init__(
            self,
            manager_loader: ManagerJsonLoader | ManagerTxtLoader,
            driver_loader: DriverTxtLoader | DriverJsonLoader,
            waiter_loader: WaiterTxtLoader | WaiterJsonLoader):
        self.__manager_loader = manager_loader
        self.__driver_loader = driver_loader
        self.__waiter_loader = waiter_loader

    def save_employee(self, employee: Employee, path: str) -> None:
        if isinstance(employee, Manager):
            self.__manager_loader.save(employee, path)
        if isinstance(employee, Driver):
            self.__driver_loader.save(employee, path)
        if isinstance(employee, Waiter):
            self.__waiter_loader.save(employee, path)

    def load_manager(self, path: str) -> Manager:
        manager = self.__manager_loader.load(path)
        if isinstance(manager, Manager):
            return manager

    def load_driver(self, path: str) -> Driver:
        return self.__driver_loader.load(path)

    def load_waiter(self, path: str) -> Waiter:
        return self.__waiter_loader.load(path)

    def switch_manager_loader(
            self,
            manager_loader: ManagerJsonLoader |
                            ManagerTxtLoader) -> None:
        self.__manager_loader = manager_loader

    def switch_driver_loader(
            self,
            driver_loader: DriverTxtLoader |
                           DriverJsonLoader) -> None:
        self.__driver_loader = driver_loader

    def switch_waiter_loader(
            self,
            waiter_loader: WaiterTxtLoader |
                           WaiterJsonLoader) -> None:
        self.__waiter_loader = waiter_loader


def create_json_worker_loader() -> WorkersLoader:
    return WorkersLoader(ManagerJsonLoader(),
                         DriverJsonLoader(),
                         WaiterJsonLoader())


def create_txt_worker_loader() -> WorkersLoader:
    return WorkersLoader(ManagerTxtLoader(),
                         DriverTxtLoader(),
                         WaiterTxtLoader())
