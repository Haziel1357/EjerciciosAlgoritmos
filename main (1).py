import random
import os
from prettytable import PrettyTable 
from PIL import Image

#Si quiero agrupar muchas funciones, hago una libreria 

datosPoliperros={
    "nombre":[],
    "huella dactilar":[],
    "foto":[]
}
numPerros=0

def menu():
    print ("\n * Bienvenido(a) *\n")
    print ("¿Qué acción desea realizar?")
    print ('* 1) Registrar Poliperro')
    print ('* 2) Mostrar Poliperros')
    print ('* 3) Imprimir BBD')
    print ('* 4) Mostrar un poliperro')
    print ('* 5) Salir del sistema')
    opcion=int(input('Ingrese la opcion: '))
    return opcion

def registrarPoliperros(numPerros):
    os.makedirs("BDDPERROS", exist_ok=True)
    archivo = open("poliperros.txt", "a")
    #"w" reescribe en el archivo, "a" añade en el archivo, "r" lee el archivo
    for i in range(numPerros): 
        print ("Ingrese los datos del poliperro ", i+1)
        nombre = input("Nombre: ")
        huellaDactilar = input("Huella Dactilar: ")


        print("¿El poliperro tiene foto ?")
        tieneFoto = input('Ingrese si o  no: ')
        if tieneFoto == "si":
            rutaOriginal=input("Ingrese la ruta de la foto: ") 
            ima = Image.open(rutaOriginal) 
        else : 
            ima = Image.open("dog.png")  

        rutaGuardada= f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
        ima.save(rutaGuardada)

        datosPoliperros["nombre"].append(nombre)
        datosPoliperros["huella dactilar"].append(huellaDactilar)
        datosPoliperros["foto"].append(rutaGuardada)

        archivo.write("BDD Poliperros \n")
        archivo.write(f"{nombre} -- {huellaDactilar} -- {rutaGuardada}\n")

    archivo.close()

def mostrarPoliperros(): 
    for i in range(len(datosPoliperros["nombre"])):
        print ("-------------------------")
        print ("Mostrar lods datos del poliperro {i+1}")
        print("* Nombre", datosPoliperros["nombre"][i])
        print("* Huella Dcatilar", datosPoliperros["huella dactilar"][i])
        print("* Foto", datosPoliperros["foto"][i])
        imagen = Image.open(datosPoliperros["foto"][i])
        imagen.show()      

def imprimirArchivo(): 
    archivo = open("poliperros.txt","r")
    lineas = archivo.readlines()
    for l in lineas:
        print(l,end=" ")

    archivo.close()

def mostrarUnPoliperro(): 
    encontrar = False 
    buscado = input("Ingrese la huella dactilar del  poliperro: ")
    for i in range(len(datosPoliperros["huella dactilar"])):
        if datosPoliperros["huella dactilar"][i]==buscado:
            print("* Nombre", datosPoliperros["nombre"][i])
            print("* Huella Dcatilar", datosPoliperros["huella dactilar"][i])
            print("* Foto", datosPoliperros["foto"][i])
            imagen = Image.open(datosPoliperros["foto"][i])
            imagen.show()      
            encontrar = True
            break
    if encontrar==False: 
        print ("Poliperro no encontrado.\n")

def main():
    print ("----------------POLIPERROS--------------")
    opcion = menu()
    while opcion != 5: 
        if opcion == 1: 
            numPerros = int(input("Ingrese el numero de poliperros a registrar: "))
            registrarPoliperros(numPerros)
        elif opcion == 2:
            mostrarPoliperros()
        elif opcion==3: 
            imprimirArchivo()
        elif opcion==4:
            mostrarUnPoliperro()

        opcion=menu()
    print("Gracias por usar el sistema")

main()
