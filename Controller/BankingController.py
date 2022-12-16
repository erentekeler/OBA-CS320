import abc

class BnakingController(abc.ABC):
    @abc.abstractclassmethod
    def getActionModel(): #It will return BankingModel
        pass
    def getView(): #This will return BankingModel
        pass 
