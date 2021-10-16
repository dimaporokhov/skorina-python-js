import PySimpleGUI as sg


layout = [
          [sg.Text('Addition of numbers')],
          [sg.Text('Number 1'), sg.InputText(key='num1')],
          [sg.Text('Number 2'), sg.InputText(key='num2')],
          [sg.Output(key='output')],
          [sg.Submit('Add'), sg.Button('Clear'), sg.Exit()]
         ]

window = sg.Window('Addition of numbers', layout)
while True:
    try:
        event, values = window.read()
        if event == 'Add':
            print(float(values['num1']) + float(values['num2']))
        if event == 'Clear':
            window.find_element('output').update('')
            window.find_element('num2').update('')
            window.find_element('num1').update('')
            window.find_element('num1').set_focus(force=True)
        if event in (None, 'Exit'):
            break
    except ValueError:
        print("Input number please")
