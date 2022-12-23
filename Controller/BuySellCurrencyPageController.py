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
        self.view = self.getView(SellBuyCurrency)

    def getView(self, page):
        return page.window

    def openPage(self):
        while True:
            events, values = self.view.read()

        self.view.close()



a = BuySellCurrencyPageController()
a.openPage()