import PySimpleGUI as sg 

sg.theme('LightGreen6')   # select theme     

layout = [
        [sg.Text('WELCOME',size = (200, 1), font=("Lucida",20,'bold'),justification = 'center')],      
        [sg.Text('ID:',font=("Lucida",12,'bold'),size =(12, 1)), sg.InputText(key='ID', size=(20,1))],      
        [sg.Text('Password:',font=("Lucida",12,'bold'),size =(12, 1)), sg.InputText(key='Password', password_char='*',size=(20,1))],
        [sg.Button('LOGIN', size = (10, 1),font=("Lucida",12,'bold'))],
        [sg.Text('Need an account?'), sg.Button('REGISTER',font=("Lucida",8,'bold'))]
        ]
                       

window = sg.Window('Ozyegin Banking Application - OBA', layout,input, size=(300,250),element_justification='c')    

while True:
    events, values = window.read()   

    user_id = values['ID']
    user_password = values['Password']

    if(events == 'LOGIN'):
        
    elif(events == 'REGISTER'):    
  
window.close()



