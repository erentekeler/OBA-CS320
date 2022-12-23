import PySimpleGUI as sg 

sg.theme('LightGreen6')   # select theme     
temp_list = ['Account1','Account2','Account3']

layout = [[sg.Text('Select the Account: ',size = (17, 1), font=('Arial',12,'bold')), sg.Combo(temp_list, size = 40)],
          [sg.Button('Enter', size = (8, 1),font=("Arial",12,'bold'), pad=(10,10)),sg.Button('Go Back', size = (8, 1),font=("Arial",12,'bold'), pad=(10,10), button_color='Dark Grey')]]


                       

window = sg.Window('Account List Page - OBA', layout,input, size=(300,150),element_justification='c')    
