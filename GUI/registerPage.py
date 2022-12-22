import PySimpleGUI as sg 

sg.theme('DarkGreen')   # select theme     


layout = [
        [sg.Text('Register Your Account',size = (200, 1), font=('Arial',20,'bold'),justification = 'center')],   
        [sg.Text('Name: ',font=('Arial',12,'bold'),size =(12, 1)), sg.InputText(key='Name', size=(20,1))],   
        [sg.Text('Surname: ',font=("Arial",12,'bold'),size =(12, 1)), sg.InputText(key='Surname', size=(20,1))], 
        [sg.Text('Password:',font=("Arial",12,'bold'),size =(12, 1)), sg.InputText(key='Password', size=(20,1))],     
        [sg.Button('Create Account', size = (25, 1),font=("Arial",12,'bold'), pad=(25,25))],
        [sg.Text('Already have an account?'), sg.Button('SIGN IN',font=("Arial",8,'bold'))]
        ]
                       

window = sg.Window('Register Page - OBA', layout,input, size=(500,500),element_justification='c')    


