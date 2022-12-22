from abc import ABC, abstractmethod

class AccountingSystem(metaclass=ABCMeta):

    @abstractmethod
    def updateDatabase(self):
        pass