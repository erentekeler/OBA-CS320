from AccountRepository import AccountRepository
from TransactionRepository import TransactionRepository
from UserRepository import UserRepository

class CreateData:
    
    def __init__(self):
        self.userRepository = UserRepository()
        self.accountRepository = AccountRepository()

    def createUsers(self):
        self.userRepository.createUser("Ceyda", "Sarı", "cs1234", "12345678978")
        self.userRepository.createUser("Cem", "Mavi", "cm1234", "12345678910")
        self.userRepository.createUser("Kermit", "Kurbaga", "kk1234", "11345678910")
        self.userRepository.createUser("Lara", "Croft", "lc1234", "11335678910")
    
    def createAccounts(self):
        userId = self.userRepository.getUserIdFromIdentityNo("11335678910")
        self.accountRepository.createAccount("TL hesabım", "TL", userId)
        self.accountRepository.createAccount("Dolar hesabım", "USD", userId)
        userId = self.userRepository.getUserIdFromIdentityNo("11345678910")
        self.accountRepository.createAccount("TL hesabım", "TL", userId)

