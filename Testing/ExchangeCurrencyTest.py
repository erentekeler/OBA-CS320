import unittest
import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Model import Account as Ac
from Data import AccountRepository as rep
class ExchangeCurrencyTest(unittest.TestCase):

    def test_007(self):
        account=Ac.Account()
        accou
        account.exchangeCurrency(4,'TL','TL hesabım','USD','Dolar hesabım',1)