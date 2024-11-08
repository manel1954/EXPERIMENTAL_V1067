# -*- coding: utf-8 -*-
import tkinter as tk
import serial
import threading
import re
from colorama import Fore, Back, Style
from colorama import init

# Inicializar colorama para colores en la consola
init()

# Configuración del puerto serie
SERIAL_PORT = "/dev/virtual2"  # Cambia esto según tu sistema
BAUD_RATE = 9600

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Monitor MMDVMHost - Nextion")
root.geometry("350x210")
root.configure(bg="#483d8b")

# Crear widgets para mostrar datos
labels = {
    "Hotspot": tk.Label(root, text="Hotspot: N/A", fg="#ff8c00", bg="#483d8b", font=("Arial", 16, "bold")),
    "Frecuencia": tk.Label(root, text="Frecuencia: N/A", fg="#ff8c00", bg="#483d8b", font=("Arial", 16, "bold")),
    "Temperatura": tk.Label(root, text="Temperatura: N/A", fg="yellow", bg="#483d8b", font=("Arial", 12, "bold")),
    "TX/RX": tk.Label(root, text="TX/RX: N/A", fg="white", bg="#483d8b", font=("Arial", 16, "bold")),
    "IP": tk.Label(root, text="IP: N/A", fg="#ff0", bg="#483d8b", font=("Arial", 12, "bold")),
    "Estado": tk.Label(root, text="Estado: N/A", fg="white", bg="#483d8b", font=("Arial", 16, "bold")),
    "Ber": tk.Label(root, text="Ber: N/A", fg="#ff8c00", bg="#483d8b", font=("Arial", 12, "bold")),
}

for label in labels.values():
    label.pack(fill="x", padx=10, pady=2)

# Función para actualizar etiquetas en la GUI
def update_label(field, value):
    if field in labels:
        labels[field].config(text=f"{field}: {value}")

# Función para leer los datos del puerto serie
def read_data():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                data = ser.readline()
                if data:
                    data_str = data.decode('utf-8', errors='ignore')
                    print(Fore.WHITE + f"Datos recibidos: {data_str}" + Style.RESET_ALL)
                    parsed_data = parse_data(data_str)
                    for key, value in parsed_data.items():
                        root.after(0, update_label, key, value)
    except serial.SerialException as e:
        print(Fore.RED + f"Error al conectar con el puerto: {e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error desconocido: {e}" + Style.RESET_ALL)

# Función para procesar los datos recibidos
def parse_data(data_str):
    result = {}
    
    # Expresiones regulares para extraer datos
    patterns = {
        "Hotspot": r'20t0.txt="([^"]+)"',
        "TX/RX": r'50t2.txt="([^"]+)"',
        "Frecuencia": r'1t32.txt="([^"]+)"',
        "IP": r'20t3.txt="([^"]+)"',
        "Temperatura": r'1t20.txt="([^"]+)"',
        "Estado": r'1t0.txt="([^"]+)"',
        "Ber": r'1t7.txt="([^"]+)"',
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, data_str)
        if match:
            result[key] = match.group(1)

    return result

# Crear un hilo para la lectura de los datos
read_thread = threading.Thread(target=read_data, daemon=True)
read_thread.start()

# Ejecutar la interfaz gráfica
root.mainloop()
