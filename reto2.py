# Import os y crear funcion lambda con operador ternario
# Una forma de hacer esta función más concisa es utilizar un operador ternario y declarar una función lambda.

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# RF01:

# count=0
# while count < 3: 
count=0

# for count in range(0, 3):
while count < 3:

    

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

    

    # if(option!=6):
    #     count+=1
    #     # print("Error")

    # opciones 1, 2, 3, 4 y 5 del menu

    if(option==1 or option==2 or option==3 or option==4 or option==5):

        count=3
        if(option==1):
            print("Usted ha elegido la opción 1")
        elif(option==2):
            print("Usted ha elegido la opción 2")
        elif(option==3):
            print("Usted ha elegido la opción 3")
        elif(option==4):
            print("Usted ha elegido la opción 4")
        elif(option==5):
            print("Usted ha elegido la opción 5")


    # opcion 6 del menu

    elif(option==6): 

        # count=3
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
                    option = int(input("Elija una opción: "))

                    # elif(favorite==7):
                    #     count=3
                    #     print("Hasta pronto")
                    
                    if(option==1 or option==2 or option==3 or option==4 or option==5):

                        
                        if(option==1):                            
                            print("Usted ha elegido la opción 1")
                        elif(option==2):                          
                            print("Usted ha elegido la opción 2")
                        elif(option==3):                          
                            print("Usted ha elegido la opción 3")
                        elif(option==4):                          
                            print("Usted ha elegido la opción 4")
                        elif(option==5):        
                            print("Usted ha elegido la opción 5")
                                    
                    elif(option==7):
                        count+=3
                        print("Hasta pronto")

                    count+=3

                else:
                    print("Error")
            else:
                print("Error")
        else:
            count+=3
            print("Error")

    # opcion 7 del menu

    elif(option==7):
        count+=3
        print("Hasta pronto")

    # opciones distintas a la 1, 2, 3, 4, 5, 6, 7
    else:
        count+=1
        print("Error")

    