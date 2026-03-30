#Programa que lea el nombre y apellido de una persona en un archivo
#de texto llamado "nombres.txt", crear un mail con la siguiente
#estructura: [3 primeras letras del nombre][apellido]@gmail.com, crear
#una contraseña aleatoria de 8 digitos, y guardar mail y contraseña
#en otro archivo de tipo "csv"

from funciones.funciones import (
    leer_nombres,
    generar_correo_un_nombre,
    generar_correo_dos_nombres,
    generar_contraseña,
    guardar_en_csv
)

if __name__ == "__main__":

    personas = leer_nombres('nombres.txt')
    
    datos = []

    for persona in personas:

        if len(persona) == 3:

            nombre, apellido, _ = persona
            correo = generar_correo_un_nombre(nombre, apellido)
            info = f"{nombre} {apellido}"
            
        else:

            primer_nombre, segundo_nombre, apellido, _ = persona
            correo = generar_correo_dos_nombres(primer_nombre, segundo_nombre, apellido)
            info = f"{primer_nombre} {segundo_nombre} {apellido}"
        
        contraseña = generar_contraseña()
        datos.append((correo, contraseña))
        print(f"{info} -> {correo} | {contraseña}")
    
    guardar_en_csv(datos, 'mails.csv')