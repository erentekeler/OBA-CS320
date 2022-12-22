from MySqlConnector import MySqlConnector

class UserRepository:

    def __init__(self):
        self.connector = MySqlConnector()

    def getUser(self, id):
        query = "select * from User where UserId = " + str(id)
        result = self.connector.executeQuery(query)
        return result

    def createUser(self, firstName, lastName, password, identityNumber):
        query =  f'INSERT INTO User (FirstName, LastName, Password, IdentityNumber) VALUES (\'{firstName}\', \'{lastName}\', \'{password}\', \'{identityNumber}\')'
        print(query)
        result = self.connector.executeQuery(query, True)
        print(result)

    def getLoginUser(self, identityNumber, password):
        query = f'select * from User where IdentityNumber = \'{identityNumber}\' AND Password = \'{password}\''
        result = self.connector.executeQuery(query)
        return result

userRepository = UserRepository()
result = userRepository.createUser(firstName= "Selen", lastName= "Selena", identityNumber="1234", password="123")
print(result)