import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import SellBuyCurrency


class BuySellCurrencyPageController():
    def __init__(self) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        

    def getView(self, page):
        pass

    def openPage(self):
        view = SellBuyCurrency.createWindow()
        while True:
            
            events, values = view.read()

        view.close()

