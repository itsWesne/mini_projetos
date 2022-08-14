import PySimpleGUI as sg

# Configurações do Layout
sg.theme('DarkGrey11')

ip_address = [
    [sg.Text('IP:'), sg.Input(default_text='192.168.1.1', size=(33, 1))]
]
wan_settings = [
    [sg.Text('TYPE:'), sg.Combo(default_value='PPPoe', button_arrow_color='DarkGrey', values=('PPPoe', 'Bridge'), size=(10, 2)), sg.Push()],
    [sg.Text('VLAN:'), sg.Input(default_text='2800', size=(12, 1)), sg.Push()],
    [sg.Text('PPPoe LOGIN:', size=(13, 1)), sg.Input(size=(15, 1)), sg.Push()],
    [sg.Text('PASSWORD:', size=(13, 1)), sg.Input(size=(15, 1), default_text='123'), sg.Push()],
    [sg.Text('ENABLE LAN PORTS:')],
    [sg.Checkbox('LAN1', default=True), sg.Checkbox('LAN2', default=True), sg.Checkbox('LAN3', default=True), sg.Checkbox('LAN4', default=True)]
]
wifi_settings = [
    [sg.Text('WIFI 2.4G:', size=(10, 1)), sg.Input(size=(23, 1)), sg.Push()],
    [sg.Text('PASSWORD', size=(10, 1)), sg.Input(size=(23, 1)), sg.Push()],
    [sg.Text('WIFI 5.8G:', size=(10, 1)), sg.Input(size=(23, 1)), sg.Push()],
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
    [sg.Frame('IP ADDRESS', layout=ip_address)],
    [sg.Frame('WAN SETTINGS', layout=wan_settings)],
    [sg.Frame('WIFI SETTINGS', layout=wifi_settings)],
    [sg.Frame('ADMIN SETTINGS', layout=admin_settings)],
    [sg.Frame('SERVICES', layout=services), sg.Frame('OTHERS', layout=others), sg.Button('CONFIGURAR')]
]


window = sg.Window('STAVIX AUTO CONFIG', layout, grab_anywhere=True, alpha_channel=0.8)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
