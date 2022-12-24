import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import TransactionHistory


class TransactionHistoryController():
    def __init__(self,customer) -> None:
        self.customer=customer
    
    def openPage(self):
        view= TransactionHistory.createWindow()
        while True:
            
            events, values = view.read()

        view.close()