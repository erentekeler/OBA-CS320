import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data import AccountRepository as acc


class ExchangeMoney:

    def __init__(self):
        pass

    def getReceivedTransactions(self, accountId):


    def getSentTransactions(self, accountId):

