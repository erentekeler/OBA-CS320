import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import TransactionHistory


class TransactionHistoryController():
    def __init__(self,customer) -> None:
        self.view=self.getView(TransactionHistory)
        self.customer=customer
    
    def getActionModel(self):
        pass

    def getView(self, tranpage):
        return tranpage.window
    
    def openPage(self):
        while True:
            events, values = self.view.read()

        self.view.close()