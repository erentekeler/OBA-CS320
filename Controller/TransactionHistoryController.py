import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import TransactionHistory
from Model import Transaction


class TransactionHistoryController():
    def __init__(self,customer) -> None:
        self.customer=customer
        self.ab=Transaction.Transaction()
    
    def openPage(self):
        view= TransactionHistory.createWindow()
        while True:
            
            events, values = view.read()
            keylist1=['ac','cur','amount','date']
            empytlist=[[''],[''],[''],['']]
            recievedTransaction=self.ab.filterTransactions(self.customer, 1)
            sentTransaction=self.ab.filterTransactions(self.customer,2)
            for i in range(0,5):
                recievedTransaction.append(empytlist)
                sentTransaction.append(empytlist)
            if(events=='Recieved'):
                for i in range(1,6):
                    view[keylist1[0]+str(i)].update(recievedTransaction[i-1][0])
                    view[keylist1[1]+str(i)].update(recievedTransaction[i-1][1])
                    view[keylist1[2]+str(i)].update(recievedTransaction[i-1][2])
                    view[keylist1[3]+str(i)].update(recievedTransaction[i-1][3])
                continue
            elif(events=='Sent'):
                for i in range(1,6):
                    view[keylist1[0]+str(i)].update(str(sentTransaction[i-1][0]))
                    view[keylist1[1]+str(i)].update(str(sentTransaction[i-1][1]))
                    view[keylist1[2]+str(i)].update(str(sentTransaction[i-1][2]))
                    view[keylist1[3]+str(i)].update(str(sentTransaction[i-1][3]))
                continue
            elif(events=='Go Back'):
                break
        view.close()