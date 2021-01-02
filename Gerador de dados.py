from PySimpleGUI import PySimpleGUI as sg
import random

seis = "\n[]  []\n[]  []\n[]  []\n..."
cinco = "\n[]  []\n  []\n[]  []\n..."
quatro = "\n[]  []\n[]  []\n..."
tres = "\n[]\n  []\n    []\n..."
dois = "\n[]\n \n   []\n..."
um = "\n[]\n..."

sg.theme('DarkAmber')   # Add a touch of color
layout = [
            [sg.Text('Dados de 6 faces aleatório:')],
            [sg.Text('Quantidade de dados:'), sg.Input(key='valor', size=(2, 1))],
            [sg.Button('Gerar')]
]
janela = sg.Window('Gerador de dados', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Gerar':
        lista = [um, dois, tres, quatro, cinco, seis]
        quant = int(valores['valor'])
        aleatorio = random.choice(lista)
        s = 0
        while s < quant:
            aleatorio = random.choice(lista)

            sg.popup_ok(aleatorio)

            s = s + 1
