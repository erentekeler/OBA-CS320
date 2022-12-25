import unittest
import sys
import os

os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Model import Account as acc
from Model import Transaction as tr
from Data import AccountRepository as AR


class LoginTest(unittest.TestCase):

    def test_004_1(self):
        user_ID = "1"
        acc.Account.createAccount(acc.Account(), "Test_Account", "TL", user_ID)
        repo = AR.AccountRepository()
        self.assertIn("Test_Account", repo.getAccountNamesOfUser(user_ID))

    def test_005(self):
        account = acc.Account
        self.assertEqual(account.getCorrespondingAmount(account(), "TRY", "TRY"), 1)
        self.assertEqual(account.getCorrespondingAmount(account(), "USD", "USD"), 1)
        self.assertEqual(account.getCorrespondingAmount(account(), "EUR", "EUR"), 1)
        self.assertAlmostEqual(account.getCurrencyData(account(), "TRY")["USD"],
                               1 / (account.getCurrencyData(account(), "USD")["TRY"]), places=6)

    def test_006(self):
        user_ID1 = "1"
        user_ID2 = "2"
        account_name1 = "Test_Account1"
        account_name2 = "Test_Account2"
        acc.Account.createAccount(acc.Account(), account_name1, "TL", user_ID1)
        acc.Account.createAccount(acc.Account(), account_name2, "TL", user_ID2)
        repo = AR.AccountRepository()
        account_ID1 = repo.getAccountIdFromAccountName(account_name1, user_ID1)[0]
        account_ID2 = repo.getAccountIdFromAccountName(account_name2, user_ID2)[0]
        repo.updateBalance(100, account_ID1)
        repo.updateBalance(200, account_ID2)
        tr.Transaction.makeTransaction(tr.Transaction(), account_name2, user_ID2, account_ID1, "20")
        self.assertEqual(repo.getAccountBalanceAccountId(account_ID1)[0], 120.0)
        self.assertEqual(repo.getAccountBalanceAccountId(account_ID2)[0], 180.0)

    def test_007(self):
        user_ID = "1"
        account_name1 = "Test_Account_Dollar"
        account_name2 = "Test_Account_Euro"
        acc.Account.createAccount(acc.Account(), account_name1, "USD", user_ID)
        acc.Account.createAccount(acc.Account(), account_name2, "EUR", user_ID)
        repo = AR.AccountRepository()
        account_ID1 = repo.getAccountIdFromAccountName(account_name1, user_ID)[0]
        account_ID2 = repo.getAccountIdFromAccountName(account_name2, user_ID)[0]
        repo.updateBalance(100, account_ID1)
        repo.updateBalance(100, account_ID2)
        acc.Account.exchangeCurrency(acc.Account(), user_ID, "USD", account_name1, "EUR", account_name2, 10)
        self.assertLess(repo.getAccountBalanceAccountId(account_ID1)[0], 100)
        self.assertGreater(repo.getAccountBalanceAccountId(account_ID2)[0], 100)


if __name__ == '__main__':
    unittest.main()
