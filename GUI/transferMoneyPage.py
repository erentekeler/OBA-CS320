import PySimpleGUI as sg 

sg.theme('DarkGreen')   # select theme     
temp_list = ['a','b','c']
temp_list2 = ['d','e','f']

layout = [
        [sg.Text('Select the Account to Send Money: ',size = (30, 1), font=('Arial',12,'bold')), sg.Combo(temp_list, size = 40)],
        [sg.Text('Select the Account to Send Money to: ',size = (30, 1), font=('Arial',12,'bold')), sg.Combo(temp_list2, size = 40)],
        [sg.Text('Amount to be Sent: ',size = (30, 1), font=('Arial',12,'bold')), sg.InputText(key='amount', size=(20,1))],
        [sg.Button('TRANSFER', size = (10, 1),font=("Arial",20,'bold'), pad=(25,25), button_color='Dark Green')],
        [sg.Button('Logout', size = (10, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')]
       
        ]
                       

window = sg.Window('Transfer Money Page - OBA', layout,input, size=(800,500))    

