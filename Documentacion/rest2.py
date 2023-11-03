import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

# Crear la base de datos y la tabla si no existen
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (username TEXT, password TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Reservas (fecha TEXT, hora TEXT, personas INTEGER, mesa TEXT)''')
conn.commit()
conn.close()

# Función para crear un nuevo usuario
def crear_usuario():
    global nuevo_usuario_entry, nueva_contraseña_entry, mensaje_registro
    nuevo_usuario = nuevo_usuario_entry.get()
    nueva_contraseña = nueva_contraseña_entry.get()

    # Conectar a la base de datos y agregar el nuevo usuario
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Usuarios (username, password) VALUES (?, ?)", (nuevo_usuario, nueva_contraseña))
    conn.commit()

    conn.close()

    mensaje_registro.config(text="Usuario registrado con éxito")

# Función para verificar las credenciales del usuario
def verificar_credenciales():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    # Conectar a la base de datos y verificar las credenciales
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE username = ? AND password = ?", (usuario, contraseña))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        mensaje_login.config(text="Inicio de sesión exitoso")
        mostrar_interfaz_reserva()
    else:
        mensaje_login.config(text="Credenciales incorrectas")

# Función para mostrar la ventana de reserva
def mostrar_interfaz_reserva():
    ventana_login.destroy()  # Cerrar la ventana de inicio de sesión

    # Crear la ventana de reserva
    ventana_reserva = tk.Tk()
    ventana_reserva.title("Reserva de Mesa")

    def confirmar_reserva():
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        personas = int(personas_entry.get())
        mesa = mesa_entry.get()

        # Conectar a la base de datos y agregar la reserva
        conn = sqlite3.connect('mi_base_de_datos.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Reservas (fecha, hora, personas, mesa) VALUES (?, ?, ?, ?)", (fecha, hora, personas, mesa))
        conn.commit()

        conn.close()

        mensaje_confirmacion.config(text="Reserva confirmada")

    # Etiqueta y campo de entrada para la fecha
    fecha_label = ttk.Label(ventana_reserva, text="Fecha:")
    fecha_label.grid(row=0, column=0, padx=10, pady=10)
    fecha_entry = ttk.Entry(ventana_reserva)
    fecha_entry.grid(row=0, column=1, padx=10, pady=10)

    # Etiqueta y campo de entrada para la hora
    hora_label = ttk.Label(ventana_reserva, text="Hora:")
    hora_label.grid(row=1, column=0, padx=10, pady=10)
    hora_entry = ttk.Entry(ventana_reserva)
    hora_entry.grid(row=1, column=1, padx=10, pady=10)

    # Etiqueta y campo de entrada para el número de personas
    personas_label = ttk.Label(ventana_reserva, text="Número de Personas:")
    personas_label.grid(row=2, column=0, padx=10, pady=10)
    personas_entry = ttk.Entry(ventana_reserva)
    personas_entry.grid(row=2, column=1, padx=10, pady=10)

    # Etiqueta y campo de entrada para la mesa deseada
    mesa_label = ttk.Label(ventana_reserva, text="Mesa Deseada:")
    mesa_label.grid(row=3, column=0, padx=10, pady=10)
    mesa_entry = ttk.Entry(ventana_reserva)
    mesa_entry.grid(row=3, column=1, padx=10, pady=10)

    # Botón para confirmar la reserva
    confirmar_button = ttk.Button(ventana_reserva, text="Confirmar Reserva", command=confirmar_reserva)
    confirmar_button.grid(row=4, columnspan=2, padx=10, pady=10)

    # Etiqueta para mostrar un mensaje de confirmación
    mensaje_confirmacion = ttk.Label(ventana_reserva, text="")
    mensaje_confirmacion.grid(row=5, columnspan=2, padx=10, pady=10)

    ventana_reserva.mainloop()

# Función para mostrar la ventana de registro
def mostrar_ventana_registro():
    global nuevo_usuario_entry, nueva_contraseña_entry, mensaje_registro

    ventana_registro = tk.Tk()
    ventana_registro.title("Registro de Usuario")

    # Etiqueta y campo de entrada para el nuevo usuario
    nuevo_usuario_label = ttk.Label(ventana_registro, text="Nuevo Usuario:")
    nuevo_usuario_label.grid(row=0, column=0, padx=10, pady=10)
    nuevo_usuario_entry = ttk.Entry(ventana_registro)
    nuevo_usuario_entry.grid(row=0, column=1, padx=10, pady=10)

    # Etiqueta y campo de entrada para la nueva contraseña
    nueva_contraseña_label = ttk.Label(ventana_registro, text="Nueva Contraseña:")
    nueva_contraseña_label.grid(row=1, column=0, padx=10, pady=10)
    nueva_contraseña_entry = ttk.Entry(ventana_registro, show="*")
    nueva_contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

    # Botón para registrar un nuevo usuario
    registro_usuario_button = ttk.Button(ventana_registro, text="Registrar Usuario", command=crear_usuario)
    registro_usuario_button.grid(row=2, columnspan=2, padx=10, pady=10)

    # Etiqueta para mostrar un mensaje de registro de usuario
    mensaje_registro = ttk.Label(ventana_registro, text="")
    mensaje_registro.grid(row=3, columnspan=2, padx=10, pady=10)

    ventana_registro.mainloop()

# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")

# Etiqueta y campo de entrada para el nombre de usuario
usuario_label = ttk.Label(ventana_login, text="Usuario:")
usuario_label.grid(row=0, column=0, padx=10, pady=10)
usuario_entry = ttk.Entry(ventana_login)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y campo de entrada para la contraseña
contraseña_label = ttk.Label(ventana_login, text="Contraseña:")
contraseña_label.grid(row=1, column=0, padx=10, pady=10)
contraseña_entry = ttk.Entry(ventana_login, show="*")
contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

# Botón para iniciar sesión
iniciar_sesion_button = ttk.Button(ventana_login, text="Iniciar Sesión", command=verificar_credenciales)
iniciar_sesion_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar un mensaje de inicio de sesión
mensaje_login = ttk.Label(ventana_login, text="")
mensaje_login.grid(row=3, columnspan=2, padx=10, pady=10)

# Botón para abrir la ventana de registro
registro_button = ttk.Button(ventana_login, text="Registrar Nuevo Usuario", command=mostrar_ventana_registro)
registro_button.grid(row=4, columnspan=2, padx=10, pady=10)

ventana_login.mainloop()