class Transaction:

    def __init__(self, fromIBAN, toIBAN, amount, status):
        self.amount = amount
        self.fromIBAN = fromIBAN
        self.toIBAN = toIBAN
        self.status = status #0 if received, 1 if sent

    def updateDatabase(self):
        print("Transaction.updateDatabase()")