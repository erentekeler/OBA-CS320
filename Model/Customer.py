from Data.UserRepository import UserRepository as users


class Customer:

    def __init__(self):
        pass

    def createUser(self, firstName, lastName, password, identityNumber):
        users.createUser(users(), firstName, lastName, password, identityNumber)

    def loginCheck(self, identityNumber, password) -> bool:
        UserTable = users()
        return users.getUserIdFromIdentityNo(UserTable, identityNumber) is not None \
            and password is users.getUserPassword(UserTable, identityNumber)[3]

    def registerCheck(self, identityNumber):
        UserTable = users()
        return users.getUserIdFromIdentityNo(UserTable, identityNumber) is not None

