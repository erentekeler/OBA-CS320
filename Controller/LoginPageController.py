import BankingController
import MainPage
import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
print(os.getcwd())
sys.path.insert(1,os.getcwd())
from GUI import loginPage


window=loginPage.window

while True:
    events, values = window.read()   

    user_id = values['ID']
    user_password = values['Password']

    if(events == 'LOGIN'&user_id=="nfa26"&user_password=="1234"):
        MainPage
        break
    elif(events == 'REGISTER'):    
        #registerpage()
        break
window.close()