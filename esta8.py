import sqlite3
import datetime
from datetime import datetime
import math
conn = sqlite3.connect('vehiculos.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tabla_vehiculos
             (ID INTEGER PRIMARY KEY AUTOINCREMENT, patente VARCHAR(6), nombre VARCHAR(40), telefono int, departamento int, fecha_ingreso timestamp,
             fecha_salida timestamp, tiempo_estacionado text, tarifa int, valor_a_pagar int, comentario VARCHAR(40), last_mod timestamp)''')
conn = sqlite3.connect('vehiculos.db')
c = conn.cursor()
class Vehiculo:
    def __init__(self, patente, nombre, telefono, departamento, fecha_ingreso, fecha_salida=None, tiempo_estacionado=None, tarifa=None, valor_a_pagar=None, comentario=None, last_mod=None):
        self.patente = patente
        self.nombre = nombre
        self.telefono = telefono
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.tiempo_estacionado = tiempo_estacionado
        self.tarifa = tarifa
        self.valor_a_pagar = valor_a_pagar
        self.comentario = comentario
        self.last_mod = last_mod
vehiculos_estacionados = []
def registrar_vehiculo():
    patente = input("Ingrese la patente del automóvil: ")
    nombre = input("Ingrese el nombre de la visita: ")
    telefono = input("Ingrese el número de teléfono: ")
    departamento = input("Ingrese el departamento: ")
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M")
    last_mod = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO tabla_vehiculos VALUES (NULL,?,?, ?, ?, ?, NULL, NULL, NULL, NULL, NULL, ?)", 
              (patente, nombre, telefono, departamento, fecha_ingreso, last_mod))
    conn.commit()    
    print("\n <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>")
    print("Automóvil registrado con éxito.")
def mostrar_vehiculos_in():
    c = conn.cursor()
    c.execute("SELECT * FROM tabla_vehiculos WHERE fecha_salida IS NULL")
    list = c.fetchall()
    if list is None:
        print("\n......................") 
        print("No hay vehículos sin pagar.") 
        print("......................") 
        print("\n")       
    else:
        for vehiculo in list:
            id, patente, nombre, telefono, departamento, fecha_ingreso, fecha_salida, tiempo_estacionado, tarifa, valor_a_pagar, comentario, last_mod = vehiculo
            print("\n===========================")
            print("Listado de vehículos:")
            print(f"\nid: {id}")
            print(f"Patente: {patente}")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {telefono}")
            print(f"Departamento visitado: {departamento}")
            print(f"Fecha/Hora de Ingreso: {fecha_ingreso}")
            print("------------------------")
def mostrar_vehiculos_pagados():
    c = conn.cursor()
    c.execute("SELECT * FROM tabla_vehiculos WHERE fecha_salida IS NOT NULL")
    list = c.fetchall()
    if list is None:
        print("\n......................") 
        print("No hay vehículos pagados.") 
        print("......................") 
        print("\n")
    else:
        for vehiculo in list:
            id, patente, nombre, telefono, departamento, fecha_ingreso, fecha_salida, tiempo_estacionado, tarifa, valor_a_pagar, comentario, last_mond = vehiculo
            print("\n===========================")
            print("\nVehículos con Salida Registrada:")
            print(f"\nid: {id}")
            print(f"Patente: {patente}")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {telefono}")
            print(f"Departamento visitado: {departamento}")
            print(f"Fecha/Hora de Ingreso: {fecha_ingreso}")
            print(f"Fecha/Hora de Salida: {fecha_salida}")
            print(f"Tiempo Estacionado: {tiempo_estacionado}")
            print(f"Tarifa: {tarifa}")
            print(f"Valor a Pagar: {valor_a_pagar}")
            print(f"Comentario: {comentario}")
            print("------------------------")
def pagar_vehiculo():
    c = conn.cursor()
    saliente = int(input(f"Ingrese id del vehiculo: "))
    c.execute("SELECT * FROM tabla_vehiculos WHERE fecha_salida IS NULL AND id= ?", (saliente,))
    result = c.fetchone()
    if result is None or len(result) == 0:
        print("\n......................") 
        print("No se encontró el vehículo.") 
        print("......................") 
        print("\n")
        return
    id, patente, nombre, telefono, departamento, fecha_ingreso, fecha_salida, tiempo_estacionado, tarifa, valor_a_pagar, comentario, lugar_mod = result
    tarifa = int(input(f"Ingrese trifa: "))
    comentario = input(f"Ingrese comentario: ")
## al leer el ingreso (str) debeo cambiar a datetime   
    fecha_ingreso_DT = datetime.strptime(fecha_ingreso, "%Y-%m-%d %H:%M")
    fecha_salida1 = datetime.now().strftime("%Y-%m-%d %H:%M")
    fecha_salida = datetime.now().strptime(fecha_salida1, "%Y-%m-%d %H:%M")    
    tiempo_estacionado_delta = fecha_salida - fecha_ingreso_DT
    calcular_y_redondeo = tiempo_estacionado_delta.total_seconds() / 60 * tarifa
    valor_a_pagar = math.floor(calcular_y_redondeo)
    last_mod = datetime.now().strftime("%Y-%m-%d %H:%M")
    tiempo_estacionado = str(tiempo_estacionado_delta)
    c.execute("UPDATE tabla_vehiculos SET fecha_salida=?, tiempo_estacionado=?, tarifa=?, valor_a_pagar=?, comentario=?, last_mod=? WHERE id=?", 
                                            (fecha_salida, tiempo_estacionado, tarifa, valor_a_pagar, comentario, last_mod, id))
    conn.commit()
    print(tiempo_estacionado)
    print(valor_a_pagar)
    print("\n <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>")
    print("Automóvil actualizado con éxito.")
def administracion():   
    c = conn.cursor()
    c.execute("SELECT * FROM tabla_vehiculos")
    list = c.fetchall()
    for vehiculo in list:
        id, patente, nombre, telefono, departamento, fecha_ingreso, fecha_salida, tiempo_estacionado, tarifa, valor_a_pagar, comentario, last_mond = vehiculo
        print("\n******************************")
        print(f"id: {id}")
        print(f"Patente: {patente}")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Departamento visitado: {departamento}")
        print(f"Fecha/Hora de Ingreso: {fecha_ingreso}")
        print(f"Fecha/Hora de Salida: {fecha_salida}")
        print(f"Tiempo Estacionado: {tiempo_estacionado}")
        print(f"Tarifa: {tarifa}")
        print(f"Valor a Pagar: {valor_a_pagar}")
        print(f"Comentario: {comentario}")
        print("******************************") 
while True:
    print("==========================================")
    print("Bienvenido al sistema de gestión de vehículos")
    print("------------------------------------------")
    print("\nSeleccione una opción:")
    print("1. Registrar vehículo")
    print("2. Mostrar vehículos ingresados sin pago")
    print("3. Mostrar vehículos pagados")
    print("4. Marcar vehículo como salida")
    print("\n5. Salir")
    print("==========================================")    
    opcion = input("Ingrese el número de la opción: ")    
    if opcion == "1":
        registrar_vehiculo()
    elif opcion == "2":
        mostrar_vehiculos_in()
    elif opcion == "3":
        mostrar_vehiculos_pagados()
    elif opcion == "4":
        pagar_vehiculo()
    elif  opcion == "6":
        administracion()
    elif opcion == "5":  
        print("Saliendo del sistema...")
        print("\n")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        