# yes

hola
proyecto
# menu 4
def Factura2(SubTotal, montodescuento, Total):
    global nombre, cedula, correo
    
    print("--- FACTURA ---")
    print("El SubTotal es de: ",SubTotal)
    print("El monto del descuento es de: ",montodescuento)
    print("El Total es de: ",Total)
    print("Cliente: ", nombre)
    print("Cedula: ", cedula )
    print("Correo: ", correo)
    print("----------------")

def Calculo(metPago, SubTotal):
    if metPago == "Efectivo":
        descuento = 0
    elif metPago == "Tarjeta":
        descuento = 0.05
    else:
        descuento = 0.1
    montodescuento = SubTotal * descuento
    Total = SubTotal - montodescuento
    Factura2(SubTotal, montodescuento, Total)
    
def Articulos(cantidadArticulos, nombre, cedula, correo):
    SubTotal = 0
    contador2 = 1
    while contador2 <= cantidadArticulos:
        nomProducto = input("Ingrese el nombre del producto: ")
        precProducto = int(input("Ingrese el precio del producto: "))
        cantidadProductos = int(input("Ingrese cuántas unidades va a comprar: "))
        print ("Nombre del articulo: ", nomProducto,)
        print ("Precio: ", precProducto)
        print ("Unidades", cantidadProductos)
        subtotal = cantidadProductos * precProducto
        SubTotal= SubTotal + subtotal
        contador2 = contador2 + 1   
    metPago = input("Ingrese el método de pago (Efectivo/Tarjeta/Otro): ")
    Calculo(metPago, SubTotal,)

def Factura(nomProducto, Total, montodescuento, precProducto, cantidadProductos):
    global nombre, cedula, correo

    print("--- FACTURA ---")
    print("Cliente: ", nombre)
    print("Cedula: ", cedula )
    print("Correo: ", correo)
    print("Producto:", nomProducto, "Precio = ", precProducto, "Cantidad = ", cantidadProductos)
    print("Descuento = ", montodescuento)
    print("Total = ", Total)
    print("----------------")


def Calculo2(nomProducto, metpago, precProducto, cantidadProductos):
    if metpago == "Efectivo":
        descuento = 0
    elif metpago == "Tarjeta":
        descuento = 0.05
    else:
        descuento = 0.1
    SubTotal = cantidadProductos * precProducto
    montodescuento = SubTotal * descuento
    Total = SubTotal - montodescuento
    Factura(nomProducto, Total, montodescuento, precProducto, cantidadProductos)
#menu 4

def menu4():
    print("--------Facturación--------")
    global nombre, cedula, correo
    if nombre == ""or cedula == "" or correo == "":
        print("No se ha registrado. Por favor regístrese primero.")
        nombre, cedula, _, correo = registroUsuario()

    cantidadArticulos = int(input("Ingrese la cantidad de articulos a comprar "))
    if cantidadArticulos > 1:
        Articulos(cantidadArticulos, nombre, cedula, correo)
        
    else:
        nomProducto = input("Ingrese el nombre del producto: ")
        precProducto = int(input("Ingrese el precio del producto: "))
        cantidadProductos = int(input("Ingrese cuántas unidades va a comprar: "))
        metpago = input("Ingrese el metodo de pago: ")
        Calculo2(nomProducto, metpago, precProducto, cantidadProductos)
    
def InicioSesion():
    intentos = 3
    while intentos > 0:
        usuarioIngresado = input("Ingrese el Usuario: ")
        claveIngresada = input("Ingrese la clave: ")
        if (usuarioIngresado == "admin" and claveIngresada == "1234") or (usuarioIngresado == "user" and claveIngresada == "5678"):
            Menu()
            intentos = 0
        else:
            intentos = intentos - 1
            print("El usuario o la contraseña son incorrectas quedan ", intentos, "intentos" )
               
def registroUsuario():
    nombre = input("Ingrese el nombre: ")
    cedula = int(input("Ingrese el # de cedula: "))
    numero = int(input("Ingrese el # de telefono: "))
    correo = input("Ingrese la direccion de correo electronico: ")
    return nombre, cedula, numero, correo
    
def menu2():
    print("--------Registro de Productos--------")
    print("funca x2")

def menu3():
    print("--------Revisar Inventario--------")
    print("funca x2")

def menu1():
    print("--------Registro de Usuario--------")
    global nombre, cedula, correo
    nombre, cedula, _, correo = registroUsuario()
    Menu()

def Menu():
    print("Seleccione una opción")
    print("1. Registro de Usuario")
    print("2. Registro de Productos") 
    print("3. Revisar Inventario") 
    print("4. Facturación")
    print("5. Salir")

    respuesta = int(input("Ingrese una opción: "))
    if respuesta == 1:
        menu1()
    elif respuesta == 2:
        menu2()
    elif respuesta == 3:
        menu3()
    elif respuesta == 4:
        menu4()
    elif respuesta == 5:
        InicioSesion()
    else:
        print("Opción no válida")
        Menu()
        
    print("funca x2")

nombre = ""
cedula = ""
correo = ""
InicioSesion()

def registroProductos():
    global valorInven, inventario
    registroproductos = int(input("¿Cuantos productos desea registrar? "))
    contador = 0
    valorInven = 0
    inventario = 0
    productos = []
    while contador < registroproductos:
        nombreProducto = input("Ingrese el nombre del producto: ")
        precioProducto = float(input("Ingrese el precio del producto: "))
        cantidadProducto = int(input("Ingrese la cantidad de productos: "))
        valorInven += precioProducto * cantidadProducto
        inventario += cantidadProducto
        productos.append((nombreProducto, precioProducto, cantidadProducto))
        contador += 1
    print("Productos registrados con éxito")
    return productos
def Menu():
    print("Bienvenido al menú principal")
    print("1. Registrar productos")
    print("2. Revisar inventario")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        menu2()
    elif opcion == 2:
        menu3()
    else:
        print("Opción inválida. Saliendo del sistema...")
        exit()

Menu()
     
def menu2(): #registro de productos
    RespuestaMenu2 = int(input("¿Desea registrar un producto? 1. Si 2. No "))
    if RespuestaMenu2 == 1:
        registroProductos()
def menu3(): #revisar inventario
    global valorInven, inventario
    if inventario == 0:
        print("No se han registrado productos. Por favor regístrelos primero.")
        registroProductos()

    print("La cantidad de productos en inventario es de:", inventario)
    print("El valor del inventario es de:", valorInven)
    YesNOt = input("¿Desea regresar al menú principal? Si/No: ")
    if YesNOt.lower() == "si":
        Menu()
    else:
        print("Saliendo del sistema...")
        exit()
