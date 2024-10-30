import PySimpleGUI as sg
from ver_habitacion import ver_habitaciones, habitaciones
from modificar_habitación import     modificar_habitacion
from ingresar_cliente import ingresar_usuario
import datetime


# Programa principal
if __name__ == "__main__":
        

    layout = [
        [sg.Text('Gestor de Habitaciones')],
        [sg.Button('Ver Habitaciones'), sg.Button('Modificar Habitaciones'), sg.Button('Ingresar Cliente')],
        [sg.Button('Salir')]
    ]

    # Crear la ventana
    window = sg.Window('Sistema de Hotel', layout)

    # Bucle de eventos
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        elif event == 'Ver Habitaciones':
            ver_habitaciones()


        elif event == 'Modificar Habitaciones':
            modificar_habitacion()


        elif event == 'Ingresar Cliente':
            ingresar_usuario()


        
    # Cerrar la ventana
    window.close()

