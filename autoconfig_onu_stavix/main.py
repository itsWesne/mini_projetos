import PySimpleGUI as sg

# Configurações do Layout
sg.theme('DarkGrey11')

wan_settings = [
    [sg.Text('TYPE:'), sg.Listbox(default_values=['PPPoe'], values=('PPPoe', 'Bridge'), size=(10, 2)), sg.Push()],
    [sg.Text('VLAN:'), sg.Input(default_text='2800', size=(12, 1)), sg.Push()],
    [sg.Text('PPPoe LOGIN:', size=(13, 1)), sg.Input(size=(15, 1)), sg.Push()],
    [sg.Text('PASSWORD:', size=(13, 1)), sg.Input(size=(15, 1), default_text='102030'), sg.Push()],
    [sg.Text('ENABLE LAN PORTS:')],
    [sg.Checkbox('LAN1', default=True), sg.Checkbox('LAN2', default=True), sg.Checkbox('LAN3', default=True), sg.Checkbox('LAN4', default=True)]
]
wifi_settings = [
    [sg.Text('WIFI 2.4G:', size=(10, 1)), sg.Input(default_text='_2.4G', size=(23, 1)), sg.Push()],
    [sg.Text('PASSWORD', size=(10, 1)), sg.Input(size=(23, 1)), sg.Push()],
    [sg.Text('WIFI 5.8G:', size=(10, 1)), sg.Input(default_text='_5G', size=(23, 1)), sg.Push()],
    [sg.Text('PASSWORD', size=(10, 1)), sg.Input(size=(23, 1)), sg.Push()]
]
admin_settings = [
    [sg.Text('USER:', size=(15, 1)), sg.Input(default_text='admin', size=(18, 1)), sg.Push()],
    [sg.Text('PASSWORD:', size=(15, 1)), sg.Input(default_text='admin', size=(18, 1)), sg.Push()],
    [sg.Text('NEW USER:', size=(15, 1)), sg.Input(default_text='admin', size=(18, 1)), sg.Push()],
    [sg.Text('NEW PASSWORD:', size=(15, 1)), sg.Input(default_text='redefibra2016', size=(18, 1)), sg.Push()]

]
services = [
    [sg.Checkbox('UPNP', default=True)]
]
others = [
    [sg.Checkbox('PING', default=True)]
]
layout = [
    [sg.Frame('WAN SETTINGS', layout=wan_settings)],
    [sg.Frame('WIFI SETTINGS', layout=wifi_settings)],
    [sg.Frame('ADMIN SETTINGS', layout=admin_settings)],
    [sg.Frame('SERVICES', layout=services), sg.Frame('OTHERS', layout=others), sg.Button('CONFIGURAR')]
]


window = sg.Window('STAVIX AUTO CONFIG', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
