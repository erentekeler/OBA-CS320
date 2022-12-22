from abc import ABCMeta,abstractmethod

class BankingController(metaclass=ABCMeta):
    @abstractmethod
    def getActionModel(): #It will return BankingModel
        pass
    @abstractmethod
    def getView(): #This will return BankingModel
        pass 
