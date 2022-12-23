import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import AccountRepository as ac
from GUI import transferMoneyPage


class TransferMoneyPageController():
    def __init__(self) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.view = self.getView(transferMoneyPage)
        self.ab = ac.AccountRepository()




    def getView(self, page):
        return page.window

    def openPage(self):

        while True:
            events, values = self.view.read()
            if(events=="Refresh Accounts List"):
                #self.view['AccNames'].update(value=[1], values=[2])
        self.view.close()



a = TransferMoneyPageController()
a.openPage()
