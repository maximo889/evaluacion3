import os
os.system("cls")

titulo = '''         SALIDAMENUDEDATOS
----------------------------------------------------------
NOMBRE              MARCA   AÑO    KILOMETRAJE    COSTO
----------------------------------------------------------
'''





Menu = """
            MENU PRINCIPAL
1. Registrar vehiculo
2. Listar todos los vehiculos registrados
3. Imprimir orden de reparacion
4. Salir del programa

Seleccione una opcion: """

Ordenvehiculos = []
Salidademenudedatos=[]



def Registarvehiculos(): 
    Marcadelvehiculo=input("digame la marca del vehiculo: ")
    Añodefabricacion=input("¿Cual es el año de fabricacion?: ")
    kilometraje=int(input("¿Cuanto kilometraje tiene este vehiculo?: "))
    Costodereparacionestimado=int(input("costo de reparacion: "))
    Impuestocostodereparacion = Costodereparacionestimado*0.08
    Costototal = Costodereparacionestimado + Impuestocostodereparacion
    Ordenvehiculos.append[Marcadelvehiculo, Añodefabricacion, kilometraje, Costodereparacionestimado]
    print(Ordenvehiculos)
def Listarvehiculosregistrados(cargos):
    Salida = titulo
    for menuPrincipal in Ordenvehiculos
    Salida += f"{Menu(0):<13}"
    Salida += f"{Menu(0):<12}"
    Salida += f"{Menu(0):<8}"
    Salida += f"{Menu(0):<19}"
    Salida += f"{Menu(0):<11}"
    Salida += f"{Menu(0):<12}"
    Salida += f"{Menu(0):<14}"
    Salida += "\n"
    return Salida
def Imprimirordendereparacion():
    Imprimirordendereparacion = input(f"cargo a imprimir [todos/{cargos}]: ").upper()    
    if Imprimirordendereparacion == "todos":
        with open("listado.txt", "w") as archivo:
            archivo.write(Listarvehiculosregistrados(cargos=))
    elif Imprimirordendereparacion in cargos:
        with open("listado.txt", "w") as archivo:
            archivo.write(Listarvehiculosregistrados(cargos=Imprimirordendereparacion))
    else:
        print("cargo no valido")
        
while True:
    try:
        Opcion = int(input(Menu))
        if Opcion == '4'
        
        
        
       
   
    
        
    