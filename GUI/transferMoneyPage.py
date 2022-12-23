import PySimpleGUI as sg

sg.theme('DarkGreen')   # select theme
maximumAmount = 0
receiverName = 'receiverName1'
logo = b'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'

layout = [
        [sg.Image(logo)],
        [sg.Text('Select the Sender Account : ',size = (21, 1), font=('Arial',12,'bold')), sg.Combo(values = [], key = "AccNames" , size = 10),sg.Text('',size = (8,1), font=('Arial',12,'bold')),sg.Text('Enter the Receiver Account ID: ',size = (24, 1), font=('Arial',12,'bold')), sg.InputText(key='receiverID', size=(12,1))],


        [sg.Text('The Maximum amount can be send:  '+str(maximumAmount),size = (50, 1), font=('Arial',12,'bold')),sg.Button('Verify', size = (10, 1),font=("Arial",12,'bold'), pad=(25,1), button_color='Dark Green')],
        #[sg.Text('Select the Account to Send Money to: ',size = (30, 1), font=('Arial',12,'bold')), sg.Combo(temp_list2, size = 40)],
        [sg.Text('Amount to be Sent: ',size = (21, 1), font=('Arial',12,'bold')), sg.InputText(key='amount', size=(12,1)),sg.Text('',size = (8, 1), font=('Arial',12,'bold')),sg.Text('Receiver\'s Name : '+receiverName,size = (30, 1), font=('Arial',12,'bold'))],
        [sg.Button('TRANSFER', size = (10, 1),font=("Arial",20,'bold'), pad=(25,25), button_color='Dark Green')],
        [sg.Button('Go Back', size = (10, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')],
        [sg.Button('Refresh Accounts List', size = (30, 1),font=("Arial",12,'bold'), pad=(25,25), button_color='Dark Grey')]

        
        ]
                       

window = sg.Window('Transfer Money Page - OBA', layout,input, size=(800,500))
