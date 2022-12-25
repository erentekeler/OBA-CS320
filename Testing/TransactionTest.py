import unittest
import sys
import os
import datetime
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Model import Transaction as tr

class TransactionTest(unittest.TestCase):

        def test_008(self):
                temp = tr.Transaction()
                self.assertTrue(temp.filterTransactions(3,1)==[('TL hesabım',10.0,'TL',datetime.date(2022,12,25))])
                self.assertTrue(temp.filterTransactions(4,2)==[('TL hesabım',10.0,'TL',datetime.date(2022,12,25))])

if __name__ == '__main__':
    unittest.main()
