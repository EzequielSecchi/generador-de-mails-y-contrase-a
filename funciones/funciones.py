import random
import string
import csv

def leer_nombres(archivo):

    personas = []

    with open(archivo, 'r') as file:

        for linea in file:

            linea = linea.strip()

            if linea:

                partes = linea.split()

                if len(partes) == 2:

                    nombre = partes[0]
                    apellido = partes[1]
                    personas.append((nombre, apellido, 2))

                elif len(partes) >= 3:

                    primer_nombre = partes[0]
                    segundo_nombre = partes[1]
                    apellido = partes[2]
                    personas.append((primer_nombre, segundo_nombre, apellido, 3))
    
    return personas

def generar_correo_un_nombre(nombre, apellido):

    tres_letras = nombre[:3].lower()
    apellido_lower = apellido.lower()
    correo = f"{tres_letras}{apellido_lower}@gmail.com"
    return correo

def generar_correo_dos_nombres(primer_nombre, segundo_nombre, apellido):

    dos_letras = primer_nombre[:2].lower()
    tres_letras = segundo_nombre[:3].lower()
    apellido_lower = apellido.lower()
    correo = f"{dos_letras}{tres_letras}{apellido_lower}@gmail.com"
    return correo

def generar_contraseña():

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choices(caracteres, k=8))
    return contraseña

def guardar_en_csv(datos, archivo_csv):

    with open(archivo_csv, 'w', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow(['Correo', 'Contraseña'])
        writer.writerows(datos)
        writer.writerows(datos)
