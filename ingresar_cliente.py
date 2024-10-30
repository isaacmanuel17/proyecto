import PySimpleGUI as sg

# Variables globales para gestionar el número de registro
numero_registro = 1

# Función para registrar un nuevo usuario
def registrar_usuario(data):
    sg.popup(f'Usuario {data["nombre"]} {data["apellido"]} registrado correctamente.\n'
             f'Nro Registro: {data["nro_registro"]}\n'
             f'Tipo de Paquete: {data["tipo_paquete"]}\n'
             f'Habitación: {data["habitacion"]}')

# Función para mostrar la interfaz de ingresar usuario
def ingresar_usuario():
    global numero_registro
    
    # Layout de la interfaz
    layout = [
        # Topbar: Nro Registro y Tipo de Paquete
        [
            sg.Text('Nro Registro:'),
            sg.InputText(f'{numero_registro}', key='-NRO_REGISTRO-', size=(10, 1), readonly=True),
            sg.Text('Tipo de Paquete:', pad=((10, 0), 0)),
            sg.InputText(key='-TIPO_PAQUETE-', size=(15, 1))
        ],
        # Body: Información personal
        [
            sg.Text('Cédula:', size=(15, 1)), sg.InputText(key='-CEDULA-', size=(30, 1))
        ],
        [
            sg.Text('Nombre:', size=(15, 1)), sg.InputText(key='-NOMBRE-', size=(30, 1))
        ],
        [
            sg.Text('Apellido:', size=(15, 1)), sg.InputText(key='-APELLIDO-', size=(30, 1))
        ],
        [
            sg.Text('Segundo Apellido:', size=(15, 1)), sg.InputText(key='-SEGUNDO_APELLIDO-', size=(30, 1))
        ],
        [
            sg.Text('Fecha de Nacimiento:', size=(15, 1)), sg.InputText(key='-FECHA_NACIMIENTO-', size=(30, 1))
        ],
        [
            sg.Text('Nacionalidad:', size=(15, 1)), sg.InputText(key='-NACIONALIDAD-', size=(30, 1))
        ],
        # Body: Información de habitación y descripción
        [
            sg.Text('Habitación:', size=(15, 1)), sg.InputText(key='-HABITACION-', size=(30, 1))
        ],
        [
            sg.Text('Descripción:', size=(15, 1)), sg.Multiline(key='-DESCRIPCION-', size=(30, 5))
        ],
        # Botones para registrar y salir
        [sg.Button('Registrar Usuario', key='-REGISTRAR-', size=(15, 1)), sg.Button('Salir', size=(10, 1))]
    ]

    # Crear la ventana
    window = sg.Window('Ingresar Usuario', layout, size=(600, 400))

    # Bucle de eventos
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        # Evento para registrar usuario
        if event == '-REGISTRAR-':
            # Capturar los datos del formulario
            data = {
                'nro_registro': numero_registro,
                'tipo_paquete': values['-TIPO_PAQUETE-'],
                'cedula': values['-CEDULA-'],
                'nombre': values['-NOMBRE-'],
                'apellido': values['-APELLIDO-'],
                'segundo_apellido': values['-SEGUNDO_APELLIDO-'],
                'fecha_nacimiento': values['-FECHA_NACIMIENTO-'],
                'nacionalidad': values['-NACIONALIDAD-'],
                'habitacion': values['-HABITACION-'],
                'descripcion': values['-DESCRIPCION-']
            }

            # Registrar usuario (mostrar popup y luego incrementar el número de registro)
            registrar_usuario(data)
            numero_registro += 1
            window['-NRO_REGISTRO-'].update(f'{numero_registro}')
            window['-TIPO_PAQUETE-'].update('')
            window['-CEDULA-'].update('')
            window['-NOMBRE-'].update('')
            window['-APELLIDO-'].update('')
            window['-SEGUNDO_APELLIDO-'].update('')
            window['-FECHA_NACIMIENTO-'].update('')
            window['-NACIONALIDAD-'].update('')
            window['-HABITACION-'].update('')
            window['-DESCRIPCION-'].update('')

    # Cerrar la ventana
    window.close()

