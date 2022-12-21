import PySimpleGUI as sg 

sg.theme('DarkGreen')   # select theme     
temp_list = ['Currency1','Currency2','Currency3']
temp_list2 = ['d','e','f']

layout = [
        [sg.Text('Select the Currency: ',size = (17, 1), font=('Arial',12,'bold')), sg.Combo(temp_list, size = 40)],
        # [sg.Text('Select the Account to Send Money to: ',size = (30, 1), font=('Arial',12,'bold')), sg.Combo(temp_list2, size = 40)],
        [sg.Text('Selling Amount : ',size = (13, 1), font=('Arial',12,'bold')), sg.InputText(key='amount', size=(20,1)),sg.Text('',size = (13, 1), font=('Arial',12,'bold')),sg.Text('Buying Amount : ',size = (13, 1), font=('Arial',12,'bold')), sg.InputText(key='amount', size=(20,1))],
       
       
        [sg.Button('SELL', size = (10, 1),font=("Arial",20,'bold'), pad=(100,25), button_color='Dark Green'),sg.Button('BUY', size = (10, 1),font=("Arial",20,'bold'), pad=(100,25), button_color='Dark Green')],
        [sg.Button('Go Back', size = (10, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')]
       
        ]

window = sg.Window('Sell/Buyy Currency Page - OBA', layout,input, size=(800,500))


