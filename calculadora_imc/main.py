import PySimpleGUI as sg
from entrada_do_usuario import calculo_imc, set_float, show_more_infos

# Configuração das linhas e layout
sg.theme('BlueMono')

row_infos = [
    [sg.Text('ALTURA:', size=(10, 0)), sg.Push(),
     sg.Input(tooltip='exemplo: 1.75', size=(250, 0), key='altura_input')],
    [sg.Text('PESO:', size=(10, 0)), sg.Push(),
     sg.Input(tooltip='exemplo: 99.5', size=(250, 0), key='peso_input')],
    [sg.Push(), sg.Button('CALCULAR'), sg.Button('RESET'), sg.Push()]
]
# Resultado do calculo IMC
row_diagnostic = [
    [sg.Text('SEU IMC É:', size=(10, 0)), sg.Push(),
     sg.Input(size=(250, 0), disabled=True, key='resultado_imc')]
]
# Informações adicionais
row_more_infos = [
    [sg.Text('', key='grau_imc')],
    [sg.Text(' ')],
    [sg.Text(' ')]
]
# Exibição das linhas\layout
layout = [
    [sg.Frame('INFOS', layout=row_infos, size=(250, 100))],
    [sg.Frame('DIAGNOSTICO', layout=row_diagnostic, size=(250, 50))],
    [sg.Frame('INFORMAÇÕES ADICIONAIS', layout=row_more_infos, size=(250, 110))]
]

# Criação da janela
window = sg.Window('CALCULADORA IMC', layout).finalize()
# ‘Loop’ para manter a janela aberta
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        '''Fecha a janela'''
        break
    elif event == 'RESET':
        '''Limpa o campo dos inputs'''
        window.find_element('altura_input').update('')
        window.find_element('peso_input').update('')
    elif event == 'CALCULAR':
        """Captura as informações digitadas e as valida"""
        values['altura_input'] = set_float(values['altura_input'])
        values['peso_input'] = set_float(values['peso_input'])

        """Chama o calculo do IMC e exibe no campo do IMC | Exibe informações adicionais sobre o IMC"""
        if type(values['altura_input']) == float == type(values['peso_input']):
            resultado_imc = set_float(calculo_imc(values['altura_input'], values['peso_input']))
            window.refresh()
            window.find_element('resultado_imc').update(resultado_imc, text_color='black')
            window.find_element('grau_imc').update(show_more_infos(resultado_imc))
        else:
            window.refresh()
            window.find_element('resultado_imc').update(value='valor invalido', text_color='red')
            window.find_element('grau_imc').update('')

window.close()
