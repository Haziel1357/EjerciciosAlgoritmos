import random

datosCliente = {
  "nombre": [],
  "apellido": [],
  "Telefono": [],
  "Direccion": [],
  "codioDelPedido":[],
  "precio":[]
}

def menu():
  print("¿Qué acción desea realizar?")
  print("* 1) Registrar productos")
  print("* 2) Mostrar pedidos")
  print("* 3) Mostrar detalle de un pedido")
  print("* 4) Eliminar pedido")
  print("* 5) Salir del sistema")
  opcion = int(input("Ingrese la opcion: "))
  return opcion

def paquetes(codigoDelPaquete):
  opcionLaptop = 0
  while True:
    print("* 1) Opción 1: PC + Monitor =  $500")
    print("* 2) Opción 2: PC + Monitor 4k = $2000")
    print("* 3) Opción 3: Lapot UltraProIA = $1500")
    print("* 4) Opción 4: Wordstation servidor = $3000")
    opcionLaptop = int(input("Ingrese la opcion: "))
    if(opcionLaptop > 0 and opcionLaptop < 5):
      print("")
      print("---------- Pedido registrado con exito ----------")
      print("")
      return opcionLaptop
    else:
      print("Error, ingrese una opcion válida")

def opcionesDePaquete(opcionLaptop):
  precio = 0
  if opcionLaptop == 1:
    precio = 500
  elif opcionLaptop == 2:
    precio = 2000
  elif opcionLaptop == 3:
    precio = 1500
  elif opcionLaptop == 4:
    precio = 3000
  else:
    print("Error...")
  precio = precio + (precio * 0.15)
  datosCliente["precio"].append(precio)

def registrarPedidos():
  codioDelPedido = 0
  print("--------------- Nuevo pedido ---------------")
  print("        Ingresar los datos del cliente")
  nombre = input("Nombre: ")
  apellido = input("Apellido: ")
  Telefono = input("Telefono: ")
  Direccion = input("Direccion: ")
  codioDelPedido = random.randint(1000, 9999)
  datosCliente["nombre"].append(nombre)
  datosCliente["apellido"].append(apellido)
  datosCliente["Telefono"].append(Telefono)
  datosCliente["Direccion"].append(Direccion)
  datosCliente["codioDelPedido"].append(codioDelPedido)
  
  print("")
  print("     Seleccione el paquete ofimático a contratar ")
  print("")
  opcionLaptop = paquetes(codioDelPedido)
  
  opcionesDePaquete(opcionLaptop)
  
def mostrarPedidos():
  if len(datosCliente["nombre"]) == 0:
    print("")
    print("------------------------------\n")
    print("No existen pedidos registrados\n")
    print("------------------------------\n")
    return
    
  print("------ Detalle de todos los pedidos ------")
  
  for i in range(len(datosCliente["nombre"])):
    print("")
    print("-----------------------------------------")
    print("Detalle del pedido", i + 1)
    print("")
    print("Datos del cliente")
    print("          * Nombre:", datosCliente["nombre"][i])
    print("          * Apellido:", datosCliente["apellido"][i])
    print("          * Telefono:", datosCliente["Telefono"][i])
    print("          * Direccion:", datosCliente["Direccion"][i])
    print("          * Codigo del pedido:", datosCliente["codioDelPedido"][i])
    print("          * Pago final con iva:", datosCliente["precio"][i])
    print("")
    
def mostrarUnPedido():
  if len(datosCliente["nombre"]) == 0:
    print("")
    print("------------------------------\n")
    print("No existen pedidos registrados\n")
    print("------------------------------\n")
    return
  encontrado = False
  print("")
  print("------ Detalle de un pedido ------")
  codigo = int(input("Ingrese el código del pedido: "))
  for i in range(len(datosCliente["nombre"])):
    if codigo == datosCliente["codioDelPedido"][i]:
      print("")
      print("Pedido encontrado")
      print("-----------------------------------------")
      print("Detalle del pedido", i + 1)
      print("")
      print("Datos del cliente")
      print("          * Nombre:", datosCliente["nombre"][i])
      print("          * Apellido:", datosCliente["apellido"][i])
      print("          * Telefono:", datosCliente["Telefono"][i])
      print("          * Direccion:", datosCliente["Direccion"][i])
      print("          * Codigo del pedido:", datosCliente["codioDelPedido"][i])
      print("          * Pago final con iva:", datosCliente["precio"][i])
      print("-----------------------------------------")
      print("")
      encontrado = True
      return
  if not encontrado:
    print("-------------------------------------------\n")
    print("*****  ERROR   *****\n")
    print("No existe ese código de pedido registrado.\n")
    print("-------------------------------------------\n")
    
def eliminarPedido():
  if len(datosCliente["nombre"]) == 0:
    print("")
    print("------------------------------\n")
    print("No existen pedidos registrados\n")
    print("------------------------------\n")
    return
  encontrado = False
  print("")
  codigo = int(input("Ingrese el código del pedido: "))
  for i in range(len(datosCliente["nombre"])):
    if codigo == datosCliente["codioDelPedido"][i]:
      datosCliente["nombre"].pop(i)
      datosCliente["apellido"].pop(i)
      datosCliente["Telefono"].pop(i)
      datosCliente["Direccion"].pop(i)
      datosCliente["codioDelPedido"].pop(i)
      datosCliente["precio"].pop(i)
      encontrado = True
      print("")
      print("------------------------------\n")
      print("Pedido eliminado con éxito \n")
      print("------------------------------\n")
      print("")
      
  if not encontrado:
    print("-------------------------------------------\n")
    print("*****  ERROR   *****\n")
    print("No existe ese código de pedido registrado.\n")
    print("-------------------------------------------\n")

def main():

  print("-------------- TECHWORD S.A ---------------")
  print(" *** Bienvenido(a) ***")
  
  opcion = 0
  opcion = menu()
  while opcion != 5:
    if opcion == 1:
      registrarPedidos()
    elif opcion == 2:
      mostrarPedidos()
    elif opcion == 3:
      mostrarUnPedido()
    elif opcion == 4:
      eliminarPedido()
    elif opcion == 5:
      return
    else:
      print("Error")
    opcion = menu()
  print("Muchas grcias...")
  
main()