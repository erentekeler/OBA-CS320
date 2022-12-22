import PySimpleGUI as sg 

sg.theme('LightGreen6')   # select theme     
temp_list = ['Currency1','Currency2','Currency3']

# 

layout = [
        [],      
        [sg.Text('Account Name:',font=("Lucida",12,'bold'),size =(12, 1)), sg.InputText(key='accountName', size=(20,1))],      
        [sg.Text('Currency:',font=("Lucida",12,'bold'),size =(12, 1)), sg.Combo(temp_list, size = 40)],
        [sg.Button('CREATE ACCOUNT', size = (10, 2),font=("Lucida",12,'bold'),pad=(200,25))],
        ]


window = sg.Window('Create Account Page - OBA', layout,input, size=(600,200))  

window.read()
