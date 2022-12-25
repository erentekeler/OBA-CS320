import unittest
import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import TransactionRepository as tr


def test_008(self):
        temp = tr.TransactionRepository()
        self.assertTrue(temp.getReceiverAccountTransactions(1)==['1','1000005','1000004','2022-12-25','20', 'TL'])
        self.assertTrue(temp.getSenderAccountTransactions(4)==['2','1000000','1000002','2022-12-25','10', 'TL'])

if __name__ == '__main__':
    unittest.main()
