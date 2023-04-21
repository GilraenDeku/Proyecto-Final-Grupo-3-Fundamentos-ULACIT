"""

Universidad Latinoamericana de Ciencia y Tecnología 

160353 - Fundamentos de Tecnologías de Información 

Proyecto Final
NEMA Consulting

Estudiantes: 

Gerald Bustamante Camacho 

Brandon Chavarría Zúñiga 

Camila Reyes Barquero 

Dayanna Quesada Solís

Profesor: 

Jorge Bastos García

4/20/2023

"""

#Creación de listas

#lista que contiene todos los nombres de los planes
lista_Plan_nombres=["Emergencia", "Salud ocupacional", "Regencias químicas", "Regencias Ambientales"]

#lista con los códigos de cada plan
lista_Plan=[0, 1, 2, 3]

#lista que contiene todos los nombres de los clientes
lista_Clientes=["Fulano"]

#lista que contiene todos los códigos de los clientes
lista_Clientes_codigo=[1234]

#Lista que guarda todas las transacciones que realiza el cliente
lista_facturacion_por_cliente=[]

#lista utilizada en el sistema para guardar una transacción específica del cliente
lista_temp_facturacion=[]

#Lista que guarda los precios de cada una de las transacciones del cliente
precio_total=[]

#Creación de variables

#Variable utilizada para salir de un bloque
salir=0

#Variable que guarda el nombre del cliente que se está trabajando en el instante
nombre_cliente_proceso=""

#Variable con valor defaul del precio por personal
valor_personal=2500

#Variable con valor defaul del precio por metro cuadrado
valor_metro_cuadrado=3000


"""
Esta función se encarga de verificar si el código del cliente existe en el sistema,
en caso de que el código sea correcto se guarda el nombre del cliente en la variable
global nombre_cliente_proceso
@return resultado_busqueda (1 si el código no se encontró, 0 si se encontró)
"""
def encontrar_cliente():
    global nombre_cliente_proceso
    print("")
    codigo_cliente=int(input("Por favor ingrese el código del cliente: "))
    print("")
    i=0
    resultado_busqueda=1
    largo=int(len(lista_Clientes_codigo))
    for i in range(largo):
        if (codigo_cliente==lista_Clientes_codigo[i]):
            nombre_cliente_proceso=lista_Clientes[i]
            resultado_busqueda=0
        else:
            if(resultado_busqueda==0):
                resultado_busqueda=0
            else:
                resultado_busqueda=1
    return resultado_busqueda

"""
Esta función se encarga de verificar si el plan que se elige existe en el sistema,
en caso de que se encuentre se guarda el nombre del plan en la lista_temp_facturacion
@return respuesta (0 si el código no se encontró, 1 si se encontró)
"""
def escoger_plan():
    global lista_temp_facturacion
    global lista_Plan_nombres
    global nombre_cliente_proceso

    print("")
    print("Inicio del proceso del cliente: " + str(nombre_cliente_proceso))
    print("")
    
    lista_temp_facturacion.clear()
    print("")
    print("Recordatorio de la lista de planes")
    print(lista_Plan_nombres)
    print("")
    
    print("")
    codigo_plan=int(input("Por favor ingrese el código del plan: "))
    print("")

    largo_lista_plan=int(len(lista_Plan))

    respuesta=0

    for d in range(largo_lista_plan):

        if(codigo_plan==lista_Plan[d]):
            respuesta=1
            print("")
            print("Se encontro el plan: " + str(lista_Plan_nombres[d]))
            print("")
            lista_temp_facturacion.append(lista_Plan_nombres[d])
        else:
            if(respuesta==1):
                respuesta=1
            else:
                respuesta=0
                
    return respuesta

"""
Esta función se encarga de guardar en la variable global precio_total el precio
total de una transacción
"""
def facturacion_precio_final():

    global precio_total
    global lista_temp_facturacion

    precio_plan=int(lista_temp_facturacion[1])
    precio_personal=int(lista_temp_facturacion[2])*int(valor_personal)
    precio_metro_cuadrado=int(lista_temp_facturacion[3]*int(valor_metro_cuadrado))

    precio_completo=precio_plan+precio_personal+precio_metro_cuadrado

    precio_total.append(precio_completo)

    
"""
Esta función se encarga de realizar y guardar la facturación del cliente
"""
def guardar_facturacion_cliente():
    
    print("")
    precio_facturacion=int(input("Por favor ingrese el precio del plan: "))
    print("")
    cantidad_personal_facturacion=int(input("Por favor ingrese la cantidad del personal que va a trabajar: "))
    print("")
    metros_cuadrados_facturacion=int(input("Por favor ingrese los metros cuadrados: "))
    print("")

    global lista_temp_facturacion
                
    lista_temp_facturacion.append(precio_facturacion)
    lista_temp_facturacion.append(cantidad_personal_facturacion)
    lista_temp_facturacion.append(metros_cuadrados_facturacion)

    global lista_facturacion_por_cliente
    lista_facturacion_por_cliente.append(lista_temp_facturacion[0:4])

    facturacion_precio_final()

"""
Esta función se encarga de imprimir el recibo del cliente
"""
def creacion_recibo():

    print("")
    print("***************************************************************************")
    print("Recibo de la transacción")
    print("")
    print("Nombre del cliente: " + str(nombre_cliente_proceso))
    print("")
    print("")

    largo_lista=int(len(lista_facturacion_por_cliente))

    for z in range(largo_lista):

        print("")
        print("------------------------------------------------------------------------------------")
        lista_temp=lista_facturacion_por_cliente[z]
        print("Nombre del Plan: " + str(lista_temp[0]))
        print("")
        print("")
        print("Precio del Plan: " + str(lista_temp[1]))
        print("")
        print("")
        print("Cantidad de Personal: " + str(lista_temp[2]) + " * " + str(valor_personal))
        print("")
        print("")
        print("Cantidad de Metros Cuadrados: " + str(lista_temp[3]) + " * " + str(valor_metro_cuadrado))
        print("")
        print("")
        print("Precio total: " + str(precio_total[z]))
        print("------------------------------------------------------------------------------------")
        print("")

"""
Esta función se encarga de realizar el cierre de caja del cliente
"""        
def cierre_de_caja():

    global lista_temp_facturacion
    global lista_facturacion_por_cliente
    global nombre_cliente_proceso
    global precio_total

    precio_final=0

    largo_lista=int(len(precio_total))

    for w in range(largo_lista):
        
        precio_final=precio_final+int(precio_total[w])

    creacion_recibo()

    print("---------------------------------------------------------------------------")
    print("")
    print("El precio final es de : " + str(precio_final))
    print("***************************************************************************")

    print("")


    
    print("Transacción realizada con éxito")

    print("")

    respuesta=str(input("¿Desea hacer otra transaccion con otro cliente? si/no: "))

    print("")
    
    if(respuesta=="si"):
        lista_facturacion_por_cliente=[]
        lista_temp_facturacion=[]
        nombre_cliente_proceso=""
        precio_total=[]
        
        return 1
    else:
        print("")
        print("Gracias por preferirnos")
        print("")
        return 0

"""
Esta función se encarga de eliminar un cliente del sistema
"""
def eliminar_Cliente():
    global lista_Clientes
    global lista_Clientes_codigo
    largo_lista=len(lista_Clientes)

    ID_Cliente=-1

    print("")
    cliente_a_eliminar=str(input("Por favor escriba el nombre del cliente que desea eliminar: "))
    print("")

    for x in range(largo_lista):
        if (cliente_a_eliminar==lista_Clientes[x]):
            ID_Cliente=x
        else:
            if(ID_Cliente==-1):
                ID_Cliente=-1
            else:
                ID_Cliente=ID_Cliente

    if(ID_Cliente==-1):
        print("")
        print("El cliente no se encuentra inscrito en el sistema")
        print("")
    else:
        lista_Clientes.pop(ID_Cliente)
        lista_Clientes_codigo.pop(ID_Cliente)
        print("")
        print("El cliente se ha encontrado y ha sido eliminado")
        print("")

"""
Esta función se encarga de agregar un cliente en el sistema
"""
def agregar_Clientes():
    global lista_Clientes
    global lista_Clientes_codigo
    largo_lista=len(lista_Clientes)

    print("")
    cliente_a_insertar=str(input("Por favor escriba el nombre del cliente que desea agregar al sistema: "))
    print("")

    lista_Clientes.append(cliente_a_insertar)

    print("")
    cliente_a_insertar_codigo=int(input("Por favor escriba el código del nuevo cliente que desea agregar al sistema: "))
    print("")

    lista_Clientes_codigo.append(cliente_a_insertar_codigo)

    print("")
    print("Cliente ingresado correctamente")
    print("")

"""
Esta función se encarga de modificar un cliente en el sistema
"""
def modificar_Clientes():
    global lista_Clientes
    global lista_Clientes_codigo
    largo_lista=len(lista_Clientes)

    ID_Cliente=-1

    print("")
    cliente_a_modificar=str(input("Por favor escriba el nombre del cliente que desea modificar: "))
    print("")

    for x in range(largo_lista):
        if (cliente_a_modificar==lista_Clientes[x]):
            ID_Cliente=x
        else:
            if(ID_Cliente==-1):
                ID_Cliente=-1
            else:
                ID_Cliente=ID_Cliente

    if(ID_Cliente==-1):
        print("")
        print("El cliente no se encuentra en el sistema, por favor inténtelo más tarde")
        print("")

    else:
        print("")
        cliente_Modificado=str(input("Por favor escriba el nuevo nombre del cliente modificado: "))
        print("")

        print("")
        cliente_Modificado_Codigo=str(input("Por favor escriba el nuevo código del cliente modificado: "))
        print("")

        lista_Clientes[ID_Cliente]=cliente_Modificado
        lista_Clientes_codigo[ID_Cliente]=cliente_Modificado_Codigo

        print("")
        print("El cliente ha sido modificado correctamente")
        print("")

"""
Esta función se encarga de modificar el precio por personal
"""
def modificar_precio_personal():
    global valor_personal
    print("")
    precio_nuevo=int(input("Por favor indique el nuevo precio por personal: "))
    valor_personal=precio_nuevo
    print("")
    print("")
    print("Valor actualizado")
    print("")

"""
Esta función se encarga de modificar el precio por metros cuadrados
"""
def modificar_precio_metros_cuadrados():
    global valor_metro_cuadrado
    print("")
    precio_nuevo=int(input("Por favor indique el nuevo precio por metro cuadrado: "))
    valor_metro_cuadrado=precio_nuevo
    print("")
    print("")
    print("Valor actualizado")
    print("")

"""
Esta función se encarga de ejecutar el menú del desarrollador.

Este menú permite modificar datos del sistema, así como eliminar o agregar clientes a este
"""
def programa_desarrollador():

    opcion_Elegida="T"

    while(opcion_Elegida!="F"):
        print("")
        print("+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*+-*")
        print("")
        print("")
        print("Bievenid@s a NEMA Consulting - modo desarrollador")
        print("")
        print("")
        
        print("")
        print("Opciones a elegir")
        print("A) Eliminar un Cliente")
        print("B) Agregar un Cliente")
        print("C) Modificar un Cliente")
        print("D) Modificar precio del personal")
        print("E) Modificar precio del metro cuadrado")
        print("F) Salir")
        print("")
        print("")

        print("")
        opcion_Elegida=str(input("Por favor escriba la opción que desea ejecutar: "))
        print("")

        if(opcion_Elegida=="A"):
            eliminar_Cliente()
            print("")
        else:
            if(opcion_Elegida=="B"):
                agregar_Clientes()
                print("")
            else:
                if(opcion_Elegida=="C"):
                    modificar_Clientes()
                    print("")
                else:
                    if(opcion_Elegida=="D"):
                        modificar_precio_personal()
                        print("")
                    else:
                        if(opcion_Elegida=="E"):
                            modificar_precio_metros_cuadrados()
                            print("")
                        else:
                            if(opcion_Elegida=="F"):
                                print("")
                                print("Ha salido del sistema desarrollador")
                                print("")
                            else:
                                print("")
                                print("Debe escribir SOLAMENTE las letras mayúsculas: A, B, C, D ,E y F")
                                print("")
                        
    menu_principal()

"""
Esta función se encarga de ejecutar el programa principal de la empresa
"""
def programa_principal():

    global salir
    
    while(salir!=1):
        print("")
        print("****************************************************************************************************************************************")    
        print("")
        print("")
        print("Bievenid@s a NEMA Consulting")
        print("")
        print("")
        pregunta_cliente=encontrar_cliente()
        print("")
        if(pregunta_cliente==0):
            salir_facturacion=True
            while(salir_facturacion):
                print("")
                contador=escoger_plan()
                print("")
                if(contador==1):
                    guardar_facturacion_cliente()
                    print("")
                    preguntar_volver_a_generar_otra_facutacion=str(input("¿Desea generar otra facturación? si/no: "))
                    print("")
                    if(preguntar_volver_a_generar_otra_facutacion=="si"):
                        salir_facturacion=True
                    else:
                        salir_facturacion=False
                else:
                    print("")
                    print("El plan no se encuentra registrado en el sistema, por favor escribir el código del plan correcto")
                    print("")

                
            print("")
            print("Lista Final del cliente")
            print(lista_facturacion_por_cliente)
            print("")

            proceso_de_cierre=cierre_de_caja()

            if(proceso_de_cierre==1):
                salir=0
            else:
                salir=1
                print("")
                print("Ha salido del sistema principal")
                print("")
                    
        else:
            print("")
            print("El cliente no se encuentra registrado en el sistema, por favor escribir el código del cliente correcto")
            print("")

    menu_principal()

    
"""
Esta función se encarga de dar la opción de elegir el tipo de menú que se desea ejecutar así como de salir del sistema
"""
def menu_principal():
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("")
    print("Bienvenid@ a NEMA Consulting")
    print("")
    print("Opciones de menú: ")
    print("")
    print("A) Desarrollador (Permite adnimistrar los clientes del sistema) ")
    print("B) Principal ")
    print("C) Salir del sistema")
    print("")
    menu_elegido=str(input("Por favor elija la opción del menú que desea visualizar: "))
    print("")

    if(menu_elegido=="A"):
        programa_desarrollador()
    else:
        if(menu_elegido=="B"):
            programa_principal()
        else:
            if(menu_elegido=="C"):
                print("")
                print("Gracias por preferirnos, l@ esperamos pronto")
                print("")
                exit
            else:
                print("")
                print("Por favor escriba SOLAMENTE A, B o C para elegir el menú")
                print("")
                menu_principal()

    


menu_principal()



                
