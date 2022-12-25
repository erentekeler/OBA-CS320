import unittest
import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Model import Customer as cs
from Data import UserRepository as Ur
class LoginTest(unittest.TestCase):

    def test_001_1(self):
        temp=cs.Customer()
        repo=Ur.UserRepository()
        #ExistingUser '11335678910'
        self.assertTrue(temp.registerCheck('11335678910')==str(8))
        self.assertIsNotNone(repo.getUserIdFromIdentityNoV2('11335678910'))
        

    def test_001_2(self):
        pass

    def test_002(self):
        pass

    def test_003(self):
        pass


if __name__ == '__main__':
    unittest.main()
