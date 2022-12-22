import PySimpleGUI as sg 

sg.theme('LightGreen6')   # select theme     

layout = [
        [sg.Button('Create New Account', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Button('List Accounts', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Button('Transfer Money', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Button('Transaction History', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Button('Buy/Sell Currency', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Button('Logout', size = (10, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')]

        ]
                       

window = sg.Window('Main Page - OBA', layout,input, size=(500,500),element_justification='c')    

