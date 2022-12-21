class Transaction:

    def __init__(self, toIBAN, amount):
        self.amount = amount
        self.toIBAN = toIBAN

    def updateDatabase(self):
        print("Transaction.updateDatabase()")


