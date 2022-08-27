import PySimpleGUI as sg
import onu_conection as oc

# Configurações do Layout
sg.theme('DarkGrey11')

ip_address = [
    [sg.Text('IP:'), sg.Input(key="ip_address", default_text='192.168.1.1', size=(33, 1))]
]
wan_settings = [
    [sg.Text('TYPE:'), sg.Combo(default_value='PPPoe', button_arrow_color='DarkGrey', values=('PPPoe', 'Bridge(not work)'), size=(10, 2)),
     sg.Push()],
    [sg.Text('VLAN:'), sg.Input(default_text='2800', size=(12, 1), key='vlan'), sg.Push()],
    [sg.Text('PPPoe LOGIN:', size=(13, 1)), sg.Input(size=(15, 1), key='pppoe_user'), sg.Push()],
    [sg.Text('PASSWORD:', size=(13, 1)), sg.Input(size=(15, 1), default_text='123', key='pppoe_pass'), sg.Push()],
    [sg.Text('ENABLE LAN PORTS:')],
    [sg.Checkbox('LAN1', default=True, key='lan1'), sg.Checkbox('LAN2', default=True, key='lan2'),
     sg.Checkbox('LAN3', default=True, key='lan3'), sg.Checkbox('LAN4', default=True, key='lan4')]
]
wifi_settings = [
    [sg.Text('WIFI 5G:', size=(10, 1)), sg.Input(size=(23, 1), key='wifi_5_name'), sg.Push()],
    [sg.Text('PASSWORD', size=(10, 1)), sg.Input(size=(23, 1), key='wifi_5_pass'), sg.Push()],
    [sg.Text('WIFI 2.4G:', size=(10, 1)), sg.Input(size=(23, 1), key='wifi_2.4_name'), sg.Push()],
    [sg.Text('PASSWORD', size=(10, 1)), sg.Input(size=(23, 1), key='wifi_2.4_pass'), sg.Push()]
]
admin_settings = [
    [sg.Text('USER:', size=(15, 1)), sg.Input(default_text='admin', size=(18, 1)), sg.Push()],
    [sg.Text('PASSWORD:', size=(15, 1)), sg.Input(default_text='admin', size=(18, 1), key='oldpass'), sg.Push()],
    [sg.Text('NEW PASSWORD:', size=(15, 1)), sg.Input(default_text='redefibra2016', size=(18, 1), key='newpass'),
     sg.Push()]

]
services = [
    [sg.Checkbox('UPNP', default=True, key='upnp')]
]
others = [
    [sg.Checkbox('PING', default=True, key='ping')]
]
layout = [
    [sg.Frame('IP ADDRESS', layout=ip_address)],
    [sg.Frame('WAN SETTINGS', layout=wan_settings)],
    [sg.Frame('WIFI SETTINGS', layout=wifi_settings)],
    [sg.Frame('ADMIN SETTINGS', layout=admin_settings)],
    [sg.Frame('SERVICES', layout=services), sg.Frame('OTHERS', layout=others), sg.Button('CONFIGURAR')]
]

window = sg.Window('STAVIX AUTO CONFIG', layout, grab_anywhere=True, alpha_channel=0.9)

while True:
    event, values = window.read()
    if event == 'CONFIGURAR':
        window.set_title(title='CONFIGURANDO AGUARDE!')
        window.set_alpha(0.5)
        if len(str(values['pppoe_user'])) and len(str(values['wifi_2.4_name'])) and len(
                str(values['wifi_5_name'])) and len(str(values['wifi_2.4_pass'])) and len(
                str(values['wifi_5_pass'])) > 0:
            if '*' not in values['wifi_2.4_pass'] and values['wifi_5_pass']:
                if len(values['wifi_2.4_pass']) and len(values['wifi_5_pass']) >= 8:
                    # window.hide()
                    sg.popup_auto_close('CONFIGURANDO AGUARDE', no_titlebar=True)

                    oc.ip_access(values['ip_address'])

                    oc.login()

                    oc.wifi_config(values['wifi_2.4_name'], values['wifi_2.4_pass'], values['wifi_5_name'],
                                   values['wifi_5_pass'])
                    sg.popup_auto_close('WIFI OK', no_titlebar=True, auto_close_duration=2)

                    oc.pon_config(values['vlan'], values['pppoe_user'], values['pppoe_pass'], values['lan1'],
                                  values['lan2'], values['lan3'], values['lan4'])
                    sg.popup_auto_close('PON OK', no_titlebar=True, auto_close_duration=2)

                    oc.services_config(values['upnp'])
                    sg.popup_auto_close('SERVICES OK', no_titlebar=True, auto_close_duration=1)

                    oc.advance_config(values['ping'])
                    sg.popup_auto_close('ADVANCE OK', no_titlebar=True, auto_close_duration=2)

                    oc.admin_config(values['oldpass'], values['newpass'])
                    sg.popup_auto_close('ADMIN OK', no_titlebar=True, auto_close_duration=2)

                    sg.popup_auto_close('CONFIGURAÇÃO CONCLUIDA', no_titlebar=True)
                    window.set_title('STAVIX AUTO CONFIG')
                    window.set_alpha(0.9)
                    # window.un_hide()
                else:
                    sg.popup_auto_close('O tamanho mínimo da senha é de 8 caracteres', no_titlebar=True)
            else:
                sg.popup_auto_close('Não pode conter * na senha', no_titlebar=True)
        else:
            sg.popup_auto_close('Não pode conter campos vazios', no_titlebar=True)

    if event == sg.WINDOW_CLOSED:
        break
