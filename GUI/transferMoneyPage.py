import PySimpleGUI as sg

sg.theme('DarkGreen')   # select theme
maximumAmount = 0
receiverName = 'receiverName1'

layout = [
        [sg.Text('Select the Sender Account : ',size = (21, 1), font=('Arial',12,'bold')), sg.Combo(values = [], key = "AccNames" , size = 10),sg.Text('',size = (8,1), font=('Arial',12,'bold')),sg.Text('Enter the Receiver Account ID: ',size = (24, 1), font=('Arial',12,'bold')), sg.InputText(key='receiverID', size=(12,1))],


        [sg.Text('The Maximum amount can be send:  '+str(maximumAmount),size = (50, 1), font=('Arial',12,'bold')),sg.Button('Verify', size = (10, 1),font=("Arial",12,'bold'), pad=(25,1), button_color='Dark Green')],
        #[sg.Text('Select the Account to Send Money to: ',size = (30, 1), font=('Arial',12,'bold')), sg.Combo(temp_list2, size = 40)],
        [sg.Text('Amount to be Sent: ',size = (21, 1), font=('Arial',12,'bold')), sg.InputText(key='amount', size=(12,1)),sg.Text('',size = (8, 1), font=('Arial',12,'bold')),sg.Text('Receiver\'s Name : '+receiverName,size = (30, 1), font=('Arial',12,'bold'))],
        [sg.Button('TRANSFER', size = (10, 1),font=("Arial",20,'bold'), pad=(25,25), button_color='Dark Green')],
        [sg.Button('Go Back', size = (10, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')],
        [sg.Button('Refresh Accounts List', size = (30, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')]

        
        ]
                       

window = sg.Window('Transfer Money Page - OBA', layout,input, size=(800,500))
