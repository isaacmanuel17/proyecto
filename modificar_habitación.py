import PySimpleGUI as sg

# Generar las habitaciones por piso (6 pisos, 12 habitaciones por piso)
habitaciones = {}
for piso in range(1, 7):
    for num_hab in range(1, 13):
        codigo_hab = f"{piso}{num_hab:02d}"  # Ej: 101, 102, ..., 612
        habitaciones[codigo_hab] = {
            'estado': 'disponible',
            'limpieza': 'limpia',
            'descripcion': f'Habitación {codigo_hab}, descripción inicial.'
        }

# Función para actualizar la información de la habitación seleccionada
def actualizar_habitacion(hab_num, limpieza, descripcion):
    if hab_num in habitaciones:
        habitaciones[hab_num]['limpieza'] = limpieza
        habitaciones[hab_num]['descripcion'] = descripcion
        sg.popup(f'Información de la habitación {hab_num} actualizada correctamente.')
    else:
        sg.popup('Número de habitación no encontrado.')

# Función para mostrar la interfaz de modificar habitación
def modificar_habitacion():
    # Lista de habitaciones para el selector
    lista_habitaciones = list(habitaciones.keys())

    # Layout de la interfaz
    layout = [
        # Topbar: Número de Habitación con selector y botón de guardar
        [
            sg.Text('Nro Habitación'),
            sg.Combo(lista_habitaciones, key='-HABITACION-', size=(10, 1)),
            sg.Push(),
            sg.Button('Guardar Información', key='-GUARDAR-', size=(15, 1))
        ],
        # Body: Estado de limpieza
        [
            sg.Text('Limpieza:'),
            sg.Radio('Limpia', "LIMPIEZA", key='-LIMPIA-', default=True),
            sg.Radio('Sucia', "LIMPIEZA", key='-SUCIA-'),
            sg.Radio('Mantenimiento', "LIMPIEZA", key='-MANTENIMIENTO-')
        ],
        # Body: Descripción
        [
            sg.Text('Descripción:'),
            sg.Multiline(size=(50, 5), key='-DESCRIPCION-', default_text='Escribe la descripción de la habitación aquí...')
        ],
        # Botón Salir
        [sg.Button('Salir', size=(10, 1))]
    ]

    # Crear la ventana
    window = sg.Window('Modificar Habitación', layout, size=(600, 300))

    # Bucle de eventos
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        # Evento de guardar información
        if event == '-GUARDAR-':
            hab_num = values['-HABITACION-']
            if hab_num:
                # Determinar el estado de limpieza seleccionado
                if values['-LIMPIA-']:
                    limpieza = 'limpia'
                elif values['-SUCIA-']:
                    limpieza = 'sucia'
                else:
                    limpieza = 'mantenimiento'

                # Obtener la descripción ingresada
                descripcion = values['-DESCRIPCION-'].strip()

                # Actualizar la información de la habitación
                actualizar_habitacion(hab_num, limpieza, descripcion)
            else:
                sg.popup('Por favor, selecciona un número de habitación.')

    # Cerrar la ventana
    window.close()


