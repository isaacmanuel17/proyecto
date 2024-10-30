import PySimpleGUI as sg

# Generar las habitaciones por piso (6 pisos, 12 habitaciones por piso)
habitaciones = {}
def ingresar_cliente(habitacion_num, cliente, acompañante, dias, cargo):
    habitaciones[habitacion_num]['estado'] = 'ocupada'
    habitaciones[habitacion_num]['ocupantes'] = {'principal': cliente, 'acompañante': acompañante}
    habitaciones[habitacion_num]['dias'] = dias
    habitaciones[habitacion_num]['cargos'].append(cargo)

def eliminar_cargo(habitacion_num, cargo):
    if cargo in habitaciones[habitacion_num]['cargos']:
        habitaciones[habitacion_num]['cargos'].remove(cargo)

# Definir el layout de la ventana
for piso in range(1, 7):
    for num_hab in range(1, 13):
        codigo_hab = f"{piso}{num_hab:02d}"  # Ej: 101, 102, ..., 612
        habitaciones[codigo_hab] = {
            'estado': 'disponible',
            'limpieza': 'limpia',
            'tipo': 's2' if num_hab % 2 == 0 else 's3',  # Alterna entre tipos s2 y s3
            'fecha_inicio': None,
            'fecha_fin': None,
            'usuario': None
        }

# Función para generar los datos de la tabla
def generar_datos_tabla():
    datos = []
    for hab_num, info in habitaciones.items():
        fila = [
            hab_num,
            info['estado'],
            info['limpieza'],
            info['tipo'],
            info['fecha_inicio'].strftime('%Y-%m-%d') if info['fecha_inicio'] else 'N/A',
            info['fecha_fin'].strftime('%Y-%m-%d') if info['fecha_fin'] else 'N/A',
            info['usuario'] if info['usuario'] else 'Ninguno'
        ]
        datos.append(fila)
    return datos

# Función para ver habitaciones
def ver_habitaciones():
    # Layout de la interfaz
    layout = [
        [sg.Text('Gestor de Habitaciones', font=('Helvetica', 16), justification='center', expand_x=True), 
         sg.Button('Actualizar', key='-ACTUALIZAR-', size=(10, 1))],
        [sg.Table(
            headings=['Número de Habitación', 'Estado', 'Limpieza', 'Tipo', 'Fecha de Inicio', 'Fecha Fin', 'Usuario Ocupando'],
            values=generar_datos_tabla(),
            key='-TABLA-',
            enable_events=False,
            auto_size_columns=True,
            justification='left',
            num_rows=20
        )],
        [sg.Button('Salir', size=(10, 10))]
    ]

    # Crear la ventana
    window = sg.Window('Ver Habitaciones', layout, size=(800, 400))

    # Bucle de eventos
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        if event == '-ACTUALIZAR-':
            # Al hacer clic en actualizar, simplemente regeneramos los datos de la tabla
            window['-TABLA-'].update(values=generar_datos_tabla())

    # Cerrar la ventana
    window.close()
