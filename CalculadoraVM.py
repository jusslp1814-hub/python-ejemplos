
#declaración de variables cantidad
vCores = 0
RAM = 0
Almacenamiento = 0
Sistema_Operativo = 0
Gestor_Base_Datos = 0

#declaración de variables costo
Cost_vCores = 0
Cost_RAM = 0
Cost_Almacenamiento = 0
Cost_Sistema_Operativo = 0
cost_Gestor_Base_Datos = 0

#declaración de variables menus
Opcion_Base = 0

#declaración de variables licencia
Paquete_Licencia = 0

#Muentra menu de obciones
print("|-------------------------------------------------|")
print("| Hola, bienvenido a la Calculadora Virtual de VM |")
print("|    Por favor, configure la máquina virtual:     |")
print("|-------------------------------------------------|")
print("|             Menú                                |")
print("| 1 -> Configurar vCores                          |")
print("| 2 -> Configurar RAM                             |")
print("| 3 -> Configurar Almacenamiento                  |")
print("| 4 -> Configurar Sistema Operativo               |")
print("| 5 -> Configurar Gestor de Base de Datos         |")
print("|                                                 |")
print("| 6. Elija el número a configurar                 |")
print("|-------------------------------------------------|")

#Validar obciones, se debe configurar la base (1 a 3)
while Opcion_Base < 1 or Opcion_Base > 3:
    Opcion_Base = int(input(""))
    if Opcion_Base < 1 or Opcion_Base > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        
        
        
#proceso de configuracion base
if Opcion_Base == 1:
    #proceso de configuracion vCores1
    while vCores < 1 or vCores > 10:
        vCores = int(input("Ingrese la cantidad de vCores: "))
        if vCores < 1 or vCores > 10:
            print("Cantidad inválida. Por favor, ingrese un número entre 1 y 10.")
    print(f"Se configuraron {vCores} vCores. su costo es de {vCores * 2.35} $.")
    
    #proceso de configuracion RAM1
    Ram = int(input("Ingrese la cantidad de RAM (GB): "))
    while RAM < 128:
        RAM = int(input("Ingrese la cantidad de RAM (GB) >= 128: "))
        if RAM < 128 :
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 128.")
            
    #proceso de configuracion Almacenamiento1
    Almacenamiento = int(input("Ingrese la cantidad de Almacenamiento (GB): "))
    while Almacenamiento < 200:
        Almacenamiento = int(input("Ingrese la cantidad de Almacenamiento (GB) >= 200: "))
        if Almacenamiento < 200:
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 200.")
            
            
            
elif Opcion_Base == 2:
    
    #proceso de configuracion RAM2
    while RAM < 128:
        RAM = int(input("Ingrese la cantidad de RAM (GB) >= 128: "))
        if RAM < 128 :
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 128.")
    print(f"Se configuraron {RAM} GB de RAM. su costo es de {RAM * 1.15} $.")
    
    #proceso de configuracion vCores2
    vCores = int(input("Ingrese la cantidad de vCores: "))
    while vCores < 1 or vCores > 10:
        vCores = int(input("Ingrese la cantidad de vCores: "))
        if vCores < 1 or vCores > 10:
            print("Cantidad inválida. Por favor, ingrese un número entre 1 y 10.")
            
    #proceso de configuracion Almacenamiento2
    Almacenamiento = int(input("Ingrese la cantidad de Almacenamiento (GB): "))
    while Almacenamiento < 200:
        Almacenamiento = int(input("Ingrese la cantidad de Almacenamiento (GB) >= 200: "))
        if Almacenamiento < 200:
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 200.")
            
            
    
else:
    #proceso de configuracion Almacenamiento3
    while Almacenamiento < 200:
        Almacenamiento = int(input("Ingrese la cantidad de Almacenamiento (GB) >= 200: "))
        if Almacenamiento < 200:
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 200.")
    print(f"Se configuraron {Almacenamiento} GB de Almacenamiento. su costo es de {Almacenamiento * 0.5} $.")
    
    #proceso de configuracion vCores3
    vCores = int(input("Ingrese la cantidad de vCores: "))
    while vCores < 1 or vCores > 10:
        vCores = int(input("Ingrese la cantidad de vCores: "))
        if vCores < 1 or vCores > 10:
            print("Cantidad inválida. Por favor, ingrese un número entre 1 y 10.")
            
    #proceso de configuracion RAM3
    RAM = int(input("Ingrese la cantidad de RAM (GB): "))
    while RAM < 128:
        RAM = int(input("Ingrese la cantidad de RAM (GB) >= 128: "))
        if RAM < 128:
            print("Cantidad insuficiente. Por favor, ingrese un número mayor o igual a 128.")

#Menu Sistema Operativo
print("|-------------------------------------------------|")
print("|      Porfavor, elija el Sistema Operativo       |")
print("|-------------------------------------------------|")
print("| 1. Microsoft Windows Server                     |")
print("| 2. Red Hat                                      |")
print("|-------------------------------------------------|")
print("| elija la opción a configurar:                   |")
print("|-------------------------------------------------|")

#validar obciones, se debe configurar la base (1 a 2)
while Sistema_Operativo < 1 or Sistema_Operativo > 2:
    Sistema_Operativo = int(input(""))
    if Sistema_Operativo < 1 or Sistema_Operativo > 2:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 2.")

#proceso de configuracion Sistema Operativo
if Sistema_Operativo == 1:
    if vCores / 2 != 0:
        vcores = vCores + 1
        
        
        
        
        
        
        Paquete_Licencia = Paquete_Licencia + 1 #----------------------------------------------> Reparacion 
        
        
        
        
        
        
        
        
        Cost_Sistema_Operativo = 104.99
    print("Se configuró Microsoft Windows Server. su costo es de 104.99  $. Adema se configuraron "+ str(Paquete_Licencia) + " licencias de Microsoft Windows Server.")