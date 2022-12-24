import PySimpleGUI as sg 

def createWindow():
        sg.theme('LightGreen6')   # select theme     
        temp_list = ['TL','USD','EUR']



        layout = [
                [],      
                [sg.Text('Account Name:',font=("Lucida",12,'bold'),size =(12, 1)), sg.InputText(key='accountName', size=(20,1))],      
                [sg.Text('Currency:',font=("Lucida",12,'bold'),size =(12, 1)), sg.Combo(temp_list, key='currency', size = 40)],
                [sg.Button('CREATE ACCOUNT', size = (10, 2),font=("Lucida",12,'bold'),pad=(200,10))],
                [sg.Button('Go Back', size = (10, 1),font=("Arial",12,'bold'), pad=(10,10), button_color='Dark Grey')]
                ]


        window = sg.Window('Create Account Page - OBA', layout,input, size=(600,200))  
        return window
