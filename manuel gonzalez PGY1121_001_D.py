import sys


def valida_num(num,texto):
    while True:
        try:
            num=int(input(texto))
            return num
        except ValueError:
            print("error debe ser un numero entero")    
def valida_rut(dato,texto,largo=None) : 
    while True:
        dato=str(input(texto))  
        if len(dato)==9:
            print(texto)
            print("rut aceptado")  
            return dato
        else:
            print("error al ingresar el rut")         

def valida_nombre(dato,texto,largo=None) : 
    while True:
        dato=str(input(texto))  
        if len(dato)>2:
            print(texto)  
            return dato
        else:
            print("error al ingresar el rut")      
def valida_año(dato,texto) : 
    while True:
        dato=int(input(texto))  
        if dato>1943:
            print(texto)  
            return dato
        else:
            print("error al ingresar año")   
def valida_categoria(dato,texto) : 
    while True:
        dato=str(input(texto))  
        if dato== "oro"or dato=="plata" or dato=="bronce":
            print(texto)  
            return dato
        else:
            print("error al ingresar categoria")


def valida_correo(correo,texto):

    correo=input(texto)
    return correo

    pass        
def pedir_datos(rut=None,fecha_nacimiento=None,nombre=None,nombre_pareja=None,categoria=None,correo=None):
    rut=valida_rut(rut,"ingrese su rut ")
    fecha_nacimiento=valida_año(fecha_nacimiento,"ingrese año de nacimiento no puede ser menosr a 1944 ")
    nombre=valida_nombre(nombre,"ingrsese su nombre y apellido ")
    nombre_pareja=valida_nombre(nombre_pareja,"ingrese el nombre de la pareja ")
    categoria=valida_categoria(categoria,"ingrese  su categoria solo oro plata o bronce ")
    correo=valida_correo(correo,"ingrese su correo")
    guardar(rut,fecha_nacimiento,nombre,nombre_pareja,categoria,correo)
    menu()


def guardar(valor1,valor2,valor3,valor4,valor5,valor6) : 
    
    jugadores={}
    todos_datos=[valor2,valor3,valor4,valor5,valor6]
    jugadores[valor1]=todos_datos
    buscar_jugador(jugadores)
    imprimir_parejas(jugadores)



    buscar=input("ingrese el rut del jugador que desea buscar")

    if buscar in jugadores:
        encontrado=jugadores[buscar]
        print(encontrado)
        for i in encontrado:
            print(i)
            menu()


def buscar_jugador(valor1=None,valor2=None):
    jugadores={}
    buscar=input("ingrese el rut del jugador que desea buscar")

    if buscar in jugadores:
        encontrado=jugadores[buscar]
        for i in encontrado:
            print(i)
            menu()

def imprimir_parejas(valor1=None):
    jugadores=[valor1]
    for i in jugadores:
        print(i)
        menu()



def menu(opc=None):
    opc=valida_num(opc,"ingrese su opcion 1/para ingresar datos/2 buscar jugador/3 imprimir parejas/4 salir")
    if opc==1:
        print("guardar")
        pedir_datos()
    elif opc==2:
        print("buscar")
        buscar_jugador()
    elif opc==3:
        print("imprimir parejas")
        imprimir_parejas()
        
    elif opc==4:
        print ("saliendo") 
        sys.exit()  

menu()