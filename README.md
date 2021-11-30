# Parcial Final - Herramientas Computacionales.
Pontificia Universidad Javeriana, Cali - Juan Camilo Dorado y Kaner Murillo. 29/11/2021

## <p align=center>**Solución punto C**

### Archivo: Solución problema parcial final.py
  
- **Problema.**  
<p align=justify>
  El problema a resolver fue un sistema de la cafetería de la Universidad, la cual está ofreciendo un descuento a sus estudiantes del 50% y a sus profesores del 20%. Este problema pide que el usuario de la Universidad ingrese sus datos, los cuales son su rol y cédula, además de registrar el producto que escogieron con el código, cantidad y precio. Con la finalidad de que se les muestre a estos usuarios, su rol de la Universidad, número de cédula, el precio final de lo que deben pagar junto con el descuento y el código del producto que escogieron.

  
- **Solución al problema.** 

1. <p align=justify>  Para resolver este problema usamos el lenguaje de programación Python, para los datos de entrada lo primero que hicimos fue declarar variables y para esto usamos diccionarios los cuales con ellos se nos va a facilitar pedir e identificar los datos de entrada los cuales son los datos del usuario como el tipo de rol y su cédula, por otro lado, tambien vamos a pedir los datos del producto como el código, cantidad en unidades y su precio. 
  

2. <p align=justify>  Con estos datos obtenidos vamos a identificar el rol del usuario, con condicionales, si es profesor el descuento es del 20% por lo que debemos hacer una operación matemática lo cual primero va a ser multiplicar el precio de ese producto por la cantidad, lo cual nos va a dar el precio sin el descuento, por lo que después debemos calcular el descuento y para ello multiplicamos ese precio por 0.2 y eso lo restamos con el precio, para que nos del precio final con su respectivo descuento, y este mismo procedimiento lo hacemos con el estudiante, pero lo único que cambiamos es su descuento el cual es del 50% y por ello hacemos el cálculo con 0.5.


3. <p align=justify> Por último, para la salida de datos debemos imprimir el mensaje: "El (Rol) con cédula (Número), debe pagar (Valor) por el producto (Código)”. Para ello, en el print del mensaje llamamos a los diccionarios de los datos del cliente que son su rol y cédula, por otro lado, tambien llamamos a los datos del producto que son su precio final con su respectivo descuento según el rol del usuario, y código del producto. Y segun el rol del usuario se va imprimir el mensaje con sus datos y el valor a pagar, junto con el código del producto. 
