import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import AccountList
from Data import AccountRepository


class AccountsPageController():
    def __init__(self,customer) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.view = self.getView(AccountList)
        self.customer=customer

    def getView(self, loginPage):
        return loginPage.window

    def openPage(self):
        while True:
            events, values = self.view.read()


        self.view.close()



a = AccountsPageController()
a.openPage()