import PySimpleGUI as sg


#   Criação do layout
def window_layout():
    sg.theme('Black')
    row = [
        [sg.Input(''), sg.Checkbox('')]
    ]
    layout = [
        [sg.Frame('TASKS', layout=row, key='container')],
        [sg.Button('New Task'), sg.Button('Reset')]
    ]

    return sg.Window('To do list', layout=layout, finalize=True, alpha_channel=.8, grab_anywhere=True,  resizable=True)


#   Criar janela
window = window_layout()

#   Regras da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'New Task':
        window.extend_layout(window['container'], [[sg.Input(''), sg.Checkbox('')]])
    elif event == 'Reset':
        window.close()
        window = window_layout()
