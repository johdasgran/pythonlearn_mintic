# Import os y crear funcion lambda con operador ternario
# Una forma de hacer esta función más concisa es utilizar un operador ternario y declarar una función lambda.

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

## Actividad Reto de la semana: Elabora un programa de inicio de sesión con validación de captcha de seguridad. (Reto 1)

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

    # Define la contraseña
    # password=52615
    # Crea lista de contraseñas en caso de que la quiera actualizar
    # listPassword=[]

    ## Password
    passUser = int(input("Ingrese contraseña: "))
    if(passUser == 52615):
        # Añade la primera contraseña a la lista de contraseñas
        # listPassword.append(passUser)

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
            print ("Sesión iniciada")

            # RF01:

            count=0
            c=0
            confirmacion=0
            listasllenas=0
            # listPassword=[]
            # validateListPassword=[]
            while (count<3):
            # for count in range(0, 3):

                option1=("1. Cambiar contraseña.\n")
                option2=("2. Ingresar coordenadas actuales.\n")
                option3=("3. Ubicar zona wifi más cercana.\n")
                option4=("4. Guardar archivo con ubicación cercana.\n")
                option5=("5. Actualizar registros de zonas wifi desde archivo.\n")
                option6=("6. Elegir opción de menú favorita.\n")
                option7=("7. Cerrar sesión.")

                print("",option1, option2, option3, option4, option5, option6, option7)

                # RF02: 51625
                # El usuario ingresa al sistema el número 6 del menú de opciones.
                


                option = int(input("Elija una opción: "))
                
                # print(listPassword)
                # opciones 1, 2, 3, 4 y 5 del menu

                if(option==1 or option==2 or option==3 or option==4 or option==5):

                    if(option==1):
                        # print("Usted ha elegido la opción 1")
                        # Password = 52615
                        #RF01 Reto 3
                        listPassword=[]
                        validateListPassword=[]
                        if(c==0):
                            listPassword.append(passUser)
                        else:
                            listPassword.append(newPass)

                        validatePass= int(input("Ingrese la contraseña actual: "))
                        validateListPassword.append(validatePass)
                        
                        # Valida que la contraseña sea correcta para pruebas xd
                        # if(validateListPassword==listPassword):
                        #     print("true")
                        # else:
                        #     print("false")

                        ## contador de nuevas contraseñas
                        # print(c)
                        for x in range(0,1):
                            if(validateListPassword==listPassword):
                                c+=1
                              
                                newPass=int(input("Nueva contraseña del usuario: "))
                                listPassword.append(newPass)
                                
                                
                                if(validateListPassword[0]==listPassword[1]):
                                    # Valida en la lista que la contraseña actual y la ingresada sean la misma y devuelve el error
                                    print("Error, no se puede cambiar la contraseña por la misma anterior.")
                                    # Elimina las contraseñas ingresadas por el usuario a las listas, 
                                    # no es necesario borrarlas ya que finaliza el programa si son las mismas.. Pero si queremos
                                    # que en case de que sea la misma le de mas intentos es necesario borrar las listas anteriores y 
                                    # poner a (c=0) para que se reinicie el contador.
                                    # c=0
                                    # listPassword.pop(1)
                                    # validateListPassword.pop(0)
                                    # print(validateListPassword)
                                    # print(listPassword)
                                    quit()



                                if(c==1):
                                    # Me borra de las dos listas el valor (52615) de las contraseñas anteiores en 
                                    # caso de que se ejecute correctamente la nueva contrasseña, así evitamos que 
                                    # marque error al volverse a ejecutar el for y valide las listas
                                    listPassword.remove(52615)
                                    validateListPassword.remove(52615)

                                # Imprime las listas para ver que esta guardando en las dos listas en estos 
                                # momentos en casa ejecucion del for.
                                # print(validateListPassword)
                                # print(listPassword)
                       

                            else:
                                # En caso de que tengan que ejeuctar varias veces el for, así el usuario 
                                # se haya equivacado al escribir la contraseña, deben borrar el indice (0) del validador de lista//
                                # validateListPassword.pop(0)
                                # Si la actual contraseña no coinciden con la ingresada por el usuario
                                # marca Error y finaliza la ejecucion.
                                print("Error, la contraseña no coincide con la actual")
                                quit()
                  
                                
                      

                    elif(option==2):

                        # print("Usted ha elegido la opción 2")
                        # RF02: El programa permite al usuario ingresar las coordenadas de los tres sitios 
                        # que más frecuenta (trabajo, casa, parque).
                        # if('sitios' in globals()):
                        #     print("Error actualización, las coordenas ya estan definidas")
                        # else:                                                          
                                         
                        # La validación de las coordenadas ingresadas se hará a partir de la siguiente tabla.
                        # Digito del grupo (5) - Municipio La Paz, Cesar - 
                        # Latitud Sup: 10.462 Inf: 9.757 - Longitud Or: -76.493 Occ: -73.623

                        # Ingresar latitud y longitud del trabajo y validar con las restriciones de coordenadas
                        # try valida si se puede ejecutar, except en caso de que el flotante contenga espacios
                        # valor=(2,4)[5>3]
                        # print(f"Resultado: {valor}")
                        # while(confirmacion!=1):
                        if(confirmacion!=1):

                            for a in range(0, 1):

                                trabajo=[]
                                casa=[]
                                parque=[]
                                                    
                                try:
                                  
                                    latitud_trabajo=float(input("Ingrese la latitud del trabajo: "))
                                    trabajo.append(latitud_trabajo)                               
                                    
                                    if (latitud_trabajo<9.757 or latitud_trabajo>10.462):
                                        print("Error coordenada")
                                        count=3
                                        break
                                        # quit()
                                    
                                    longitud_trabajo=float(input("Ingrese la longitud del trabajo: "))
                                    trabajo.append(longitud_trabajo)
                                    if(longitud_trabajo>(-73.623) or longitud_trabajo<(-76.493)):
                                        print("Error coordenada")
                                        count=3
                                        break

                                    # Ingresar latitud y longitud de casa y validar con las restriciones de coordenadas
                                    latitud_casa=float(input("Ingrese la latitud del casa: "))
                                    casa.append(latitud_casa)
                                    if(latitud_casa<9.757 or latitud_casa>10.462):
                                        print("Error coordenada")
                                        count=3
                                        break
                                    longitud_casa=float(input("Ingrese la longitud del casa: "))
                                    casa.append(longitud_casa)
                                    if(longitud_casa>(-73.623) or longitud_casa<(-76.493)):
                                        print("Error coordenada")
                                        count=3
                                        break

                                    # Ingresar latitud y longitud del parque y validar con las restriciones de coordenadas
                                    latitud_parque=float(input("Ingrese la latitud  del parque: "))
                                    parque.append(latitud_parque)
                                    if(latitud_parque<9.757 or latitud_parque>10.462):
                                        print("Error coordenada")
                                        count=3
                                        break
                                    longitud_parque=float(input("Ingrese la longitud del parque: "))
                                    parque.append(longitud_parque)
                                    if(longitud_parque>(-73.623) or longitud_parque<(-76.493)):
                                        print("Error coordenada")
                                        count=3
                                        break
                                    
                                 
                                    confirmacion+=1
                                    sitios=[trabajo, casa, parque]
                                    break

                                except:
                                    # Si al ingresar algun datos a la matriz esta vacio finaliza programa con Error
                                    print("Error")
                                    # finalizarPrograma()
                                    break
                            

                                # sitios=[trabajo, casa, parque]
                                # print(sitios)
                           
                    
                        else:
                        
                            #RF03 Reto 3
                            # globals() busca si la variable 'sitios' existe o no, la existencia depende 
                            # de si se ha ejecutado antes la opcion 2.
                            if('sitios' in globals()):
                                # print("esta defninda o existe?")
                                print("1. Coordenada trabajo [latitud, longitud] :", trabajo)
                                print("2. Coordenada casa [latitud, longitud] :", casa)
                                print("3. Coordenada parque [latitud, longitud] :" ,parque)
                                print("La coordenada 1 ubicada más al sur")
                                print("La coordenada 2 ubicada más al oriente")
                                # sitios=[trabajo, casa, parque]

                                press=int(input("Presione 1, 2 o 3 para actualizar la respectiva coordenada\no presione 0 para salir: "))

                                ## Dejamos que pueda actualizar la matriz de coordenadas de forma correcta hasta 100 intentos.
                                ## Si se equivoca en uno de los intentos finaliza ejecucion.
                                

                                try:
                                
                                    if(press==1):

                                        # Borrar datos anteriores y ingresar los nuevos actualizados
                                        trabajo.pop(0)
                                        trabajo.pop(0)
                                        # Ingresar latitud y longitud de casa y validar con las restriciones de coordenadas
                                        latitud_trabajo=float(input("Ingrese la latitud  del trabajo: "))
                                
                                        trabajo.append(latitud_trabajo)
                                        if (latitud_trabajo<9.757 or latitud_trabajo>10.462):
                                            print("Error coordenada")
                                            break
                                        longitud_trabajo=float(input("Ingrese la longitud del trabajo: "))
                                    
                                        trabajo.append(longitud_trabajo)
                                        if(longitud_trabajo>(-73.623) or longitud_trabajo<(-76.493)):
                                            print("Error coordenada")
                                            break
                                        

                                    elif(press==2):

                                        # Borrar datos anteriores y ingresar los nuevos actualizados
                                        casa.pop(0)
                                        casa.pop(0)

                                        # Ingresar latitud y longitud de casa y validar con las restriciones de coordenadas
                                        latitud_casa=float(input("Ingrese la latitud  del casa: "))
                                
                                        casa.append(latitud_casa)
                                        if(latitud_casa<9.757 or latitud_casa>10.462):
                                            print("Error coordenada")
                                            break
                                        longitud_casa=float(input("Ingrese la longitud del casa: "))
                                
                                        casa.append(longitud_casa)
                                        if(longitud_casa>(-73.623) or longitud_casa<(-76.493)):
                                            print("Error coordenada")
                                            break
                                    

                                    elif(press==3):

                                        # Borrar datos anteriores y ingresar los nuevos actualizados
                                        parque.pop(0)
                                        parque.pop(0)

                                        # Ingresar latitud y longitud del parque y validar con las restriciones de coordenadas
                                        latitud_parque=float(input("Ingrese la latitud  del parque: "))
                            
                                        parque.append(latitud_parque)
                                        if(latitud_parque<9.757 or latitud_parque>10.462):
                                            print("Error coordenada")
                                            break
                                        longitud_parque=float(input("Ingrese la longitud del parque: "))
                                
                                        parque.append(longitud_parque)
                                        if(longitud_parque>(-73.623) or longitud_parque<(-76.493)):
                                            print("Error coordenada")
                                            break
                                    
                                    
                                    elif(press==0):
                                        # break
                                        C=0

                                    else:
                                        print("Error actualización.")
                                        break
                                        

                                    # sitios sera igual a las nuevas coordenadas actualizadas 
                                    sitios=[trabajo, casa, parque]
                                    # print(sitios)


                                except:
                                    # Si al ingresar algun datos a la matriz esta vacio finaliza programa con Error
                                    print("Error")
                                    break


                        # else:
                        #     print("Debes ingresar primero las coordenadas en la opcion 2")
                        #     break







                    elif(option==3):
                        print("Usted ha elegido la opción 3")
                        break
                    elif(option==4):
                        print("Usted ha elegido la opción 4")
                        break
                
                    elif(option==5):
                        print("Usted ha elegido la opción 5")
                        break



                        


                        # print("Usted ha elegido la opción 5")
                        # break

                        
                    
               
                
                # opcion 6 del menu
                elif(option==6): 

                    favorite = int(input("Seleccione opción favorita: "))

                    if(favorite==1 or favorite==2 or favorite==3 or favorite==4 or favorite==5):
                        validate1= int(input("Soy más de uno sin llegar a tres y llego a cuatro cuando dos me des. ¿Cuál número soy? "))

                        if(validate1==2):
                            validate2= int(input("Cuenta los dedos de tu mano y también los de uno de tus pies y sabrás que número es.. ¿Cuál número soy? "))

                            if(validate2==5):
                                # print("yujuuuuu!")

                                if(favorite==1):
                                    clearConsole()
                                    print("",option1, option2, option3, option4, option5, option6, option7)
                                elif(favorite==2):
                                    clearConsole()
                                    option2=("1. Ingresar coordenadas actuales.\n")
                                    option1=("2. Cambiar contraseña.\n")
                                    print("",option2, option1, option3, option4, option5, option6, option7)
                                elif(favorite==3):
                                    clearConsole()
                                    option3=("1. Ubicar zona wifi más cercana.\n")
                                    option1=("2. Cambiar contraseña.\n")
                                    option2=("3. Ingresar coordenadas actuales.\n")
                                    print("",option3, option1, option2, option4, option5, option6, option7)
                                elif(favorite==4):
                                    clearConsole()
                                    option4=("1. Guardar archivo con ubicación cercana.\n")
                                    option1=("2. Cambiar contraseña.\n")
                                    option2=("3. Ingresar coordenadas actuales.\n")
                                    option3=("4. Ubicar zona wifi más cercana.\n")
                                    print("",option4, option1, option2, option3, option5, option6, option7)
                                elif(favorite==5):
                                    clearConsole()
                                    option5=("1. Actualizar registros de zonas wifi desde archivo.\n")
                                    option1=("2. Cambiar contraseña.\n")
                                    option2=("3. Ingresar coordenadas actuales.\n")
                                    option3=("4. Ubicar zona wifi más cercana.\n")
                                    option4=("5. Guardar archivo con ubicación cercana.\n")
                                    print("",option5, option1, option2, option3, option4, option6, option7)

                            
                                # Elja una opcion RF02
                                # Aqui seria el posible import del reto 3
                                option0 = int(input("Elija una opción: "))
                                
                                if(option0==1 or option0==2 or option0==3 or option0==4 or option0==5):
                                   
                                    if(option0==1):                            
                                        print("Usted ha elegido la opción 1")
                                    elif(option0==2):                          
                                        print("Usted ha elegido la opción 2")
                                    elif(option0==3):                          
                                        print("Usted ha elegido la opción 3")
                                    elif(option0==4):                          
                                        print("Usted ha elegido la opción 4")
                                    elif(option0==5):        
                                        print("Usted ha elegido la opción 5")
                                                
                                elif(option0==7):
                                    print("Hasta pronto")

                                break

                            else:
                                print("Error")
                        else:
                            print("Error")
                    else:
                        print("Error")
                        break

                # opcion 7 del menu
                elif(option==7):
                    print("Hasta pronto")
                    break

                # opciones distintas a la 1, 2, 3, 4, 5, 6, 7
                else:
                    count+=1
                    print("Error")

        else: 
            print ("Error") 
    else:
        print ("Error")

    