## Actividad Reto de la semana: Elabora un programa de inicio de sesión con validación de captcha de seguridad. (Reto 1)

# platform: detecta el os desde el que se ejecuta el .py
# os: permite ejecutar comandos de consola (Linux / Windows / Mac)
import platform
import os
# TODO: clean comments//

## RF01 - El programa dispone de un mensaje de bienvenida al sistema
##        previo a la solicitud de las credenciales de acceso.

print ("*** Bienvenido al sistema de ubicación para zonas públicas WIFI ***")

## RF02 - El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola.
# User_Name = 51625
# Password = 52615
User_Name = int(input("Ingrese usuario: "))

if User_Name != 51625:
    print ("Error")
else:

## Password
    Password = int(input("Ingrese contraseña: "))
    if Password == 52615:

        ## RF03: - : El programa dispone de un captcha de seguridad que confirma
        ##           que el inicio de sesión corresponde a un usuario.
        ## Captcha
        Captcha = 625
        Captcha_Math = (6*2)-5-5
        Captcha_Final = (Captcha + Captcha_Math)
        Capcha_Validate = int(input("Complete la suma 625 + 2: "))

        # RF04: - : El programa confirma el ingreso al sistema con un mensaje de
        #            éxito en el inicio de sesión.
        if Captcha_Final == Capcha_Validate:

            ## Clear screent
            #8 sistema: variable que guarda el nombre del sistema operativo como un string 
            sistema = platform.system()
            # Show the os
            # print("Estamos en {}".format(sistema))

            if sistema == "Linux" or sistema == "Darwin":
                os.system('clear')
            elif sistema == "Windows":
                os.system('cls')    
            print ("Sesión iniciada")
        else: 
           print ("Error") 
    else:
        print ("Error")




