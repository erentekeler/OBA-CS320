import PySimpleGUI as sg 

sg.theme('DarkGreen')   # select theme     
temp_list1 = ["accountName1",'Currency1','Buy/Sell1','Amount1']
temp_list2 = ["accountName2",'Currency2','Buy/Sell2','Amount2']
temp_list3 = ["accountName3",'Currency3','Buy/Sell3','Amount3']
temp_list4 = ["accountName4",'Currency4','Buy/Sell4','Amount4']
temp_list5 = ["accountName5",'Currency5','Buy/Sell5','Amount5']

layout = [
        [sg.Text('Account Name  |     Currency    |          BUY/SELL        |     Amount ',size = (100, 1), font=('Arial',12,'bold'))],
        [
        sg.Text(str(temp_list1[0]),size = (13, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list1[1]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list1[2]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list1[3]),size = (13, 1), font=('Arial',12,'bold')),],
         [
        sg.Text(str(temp_list2[0]),size = (13, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list2[1]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list2[2]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list2[3]),size = (13, 1), font=('Arial',12,'bold')),],
         [
        sg.Text(str(temp_list3[0]),size = (13, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list3[1]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list3[2]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list3[3]),size = (13, 1), font=('Arial',12,'bold')),],
         [
        sg.Text(str(temp_list4[0]),size = (13, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list4[1]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list4[2]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list4[3]),size = (13, 1), font=('Arial',12,'bold')),],
         [
        sg.Text(str(temp_list5[0]),size = (13, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list5[1]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list5[2]),size = (12, 1), font=('Arial',12,'bold')),
        sg.Text(str(temp_list5[3]),size = (13, 1), font=('Arial',12,'bold')),],
        [sg.Button('SELL', size = (10, 1),font=("Arial",20,'bold'), pad=(200,25))]

        ]

window = sg.Window('Transaction History Page - OBA', layout,input, size=(600,600))
window.read()

