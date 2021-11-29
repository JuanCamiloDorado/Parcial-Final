#Diccionario, el cual tiene como función, almacenar los datos del comprador.
cliente = {}

#Un diccionario, el cual tiene como función, almacenar los datos del producto a comprar.
producto = {}

#Información del cliente, se pide en un solo input, en la cual, debe ingresar, el nombre y la cedula, separados por espacios.  
cliente["rol"],cliente["cedula"] = input().split()

#Información del producto, se pide en un solo input, en el cual, debe ingresar, el codigo,cantidad de unidades y precio del prodcto, separado por espacios.
producto["codigo"],producto["cantidad"],producto["precio"] = input().split()

#Este condicional, tiene como función, evaluar si la persona es un profesor, si lo es, haria lo siguiente:
if cliente["rol"] == "profesor":

    #Calcular el precio a pagar sin iva, multiplicando la cantidad de unidades, y el precio del prodcuto.
    precio = int(producto["cantidad"]) * int(producto["precio"])

    #Calcular el descuento, multiplicando el precio, por el 20%, ya que es un prefesor.
    descuento = precio*0.2

    #Calcular el total a pagar, restandole, el descuento, al total a pagar sin iva.
    producto["precio"] = precio-descuento

#Al ser solamente dos condiciones, este else, determina, que si la anterior condicion no se cumplio, debe acceder a ella, haciendo el mismo proceso que el anterior, pero con un descuento del 50%.
else:
    precio = int(producto["cantidad"]) * int(producto["precio"])
    descuento = precio*0.5
    producto["precio"] = precio-descuento

#Se imprime el mensaje con la modalidad de formato, al usar diccionarios, no tuvimos la necesidad, de hacer varios prints teniendo en cuenta si era profesor, o estudiante. 
print("El %s con cedula %s, debe pagar %d por el producto %s" %(cliente["rol"],cliente["cedula"],producto["precio"],producto["codigo"]))
