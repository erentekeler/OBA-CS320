import unittest
import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Model import Customer as cs
from Data import AccountRepository as acr
from Data import UserRepository as Ur
class LoginTest(unittest.TestCase):

    def test_001_1(self):
        temp=cs.Customer()
        repo=Ur.UserRepository()
        #ExistingUser '11335678910'
        self.assertTrue(temp.registerCheck('11335678910')==str(8))
        self.assertIsNotNone(repo.getUserIdFromIdentityNoV2('11335678910'))
        

    def test_001_2(self):
        temp=cs.Customer()
        repo=Ur.UserRepository()
        #new id 98979695123
        self.assertTrue(temp.registerCheck('98979695123'))
        self.assertIsNone(repo.getUserIdFromIdentityNoV2('98979695123'))

    def test_002(self):
        temp = cs.Customer()
        repo=Ur.UserRepository() 
        #ExistingUser '11335678910'
        self.assertTrue(temp.loginCheck('11335678910','c1234')== False)
        self.assertTrue(temp.loginCheck('01335678910','lc1234')== False)
        self.assertTrue(temp.loginCheck('11335678910','lc1234')== True)



    def test_003(self):
        temp = acr.AccountRepository()
        self.assertTrue(temp.getAccountNamesOfUser(4)==['TL hesabım','Dolar hesabım'])
        self.assertTrue(temp.getCurrencyFromAccountName('TL hesabım',4)[0]=='TL')
        self.assertTrue(temp.getCurrencyFromAccountName('Dolar hesabım',4)[0]=='USD')
        self.assertTrue(temp.getAccountIdFromAccountName('TL hesabım',4)[0]==1000000)
        self.assertTrue(temp.getAccountIdFromAccountName('Dolar hesabım',4)[0]==1000001)

       


if __name__ == '__main__':
    unittest.main()
