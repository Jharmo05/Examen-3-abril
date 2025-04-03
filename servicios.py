from almacenamiento import *


def pedir_numero_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isalpha():
            return valor
        else:
            print("Por favor, ingrese un texto válido (solo caracteres alfabéticos).")


def agregar_servicio():
    nombre = pedir_texto("Ingrese el nombre del paquete fotográfico: ")
    precio = pedir_numero_float("Ingrese el precio del servicio: ")
    tipo_evento = pedir_texto("Ingrese el tipo de evento (boda, retrato, producto, etc.): ")
    duracion = pedir_numero_float("Ingrese la duración estimada en horas: ")
    
   
    servicio = {
        'nombre': nombre,
        'precio': precio,
        'tipo_evento': tipo_evento,
        'duracion': duracion
    }
    
    
    servicios = cargar_servicios()
    servicios.append(servicio)
    guardar_servicios(servicios)
    print(f"Servicio '{nombre}' agregado exitosamente.")


def editar_servicio():
    nombre = pedir_texto("Ingrese el nombre del servicio que desea editar: ")
    servicios = cargar_servicios()
    
    for servicio in servicios:
        if servicio['nombre'].lower() == nombre.lower():
            print(f"Servicio encontrado: {servicio}")
            
            nuevo_nombre = input("Ingrese el nuevo nombre del paquete fotográfico (deje vacío para mantener el actual): ")
            if nuevo_nombre:
                servicio['nombre'] = nuevo_nombre
            
            nuevo_precio = input("Ingrese el nuevo precio del servicio (deje vacío para mantener el actual): ")
            if nuevo_precio:
                try:
                    servicio['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Valor de precio inválido. El precio debe ser un número.")
                    return
            
            nuevo_tipo_evento = input("Ingrese el nuevo tipo de evento (deje vacío para mantener el actual): ")
            if nuevo_tipo_evento:
                servicio['tipo_evento'] = nuevo_tipo_evento
            
            nueva_duracion = input("Ingrese la nueva duración estimada en horas (deje vacío para mantener la actual): ")
            if nueva_duracion:
                try:
                    servicio['duracion'] = float(nueva_duracion)
                except ValueError:
                    print("Valor de duración inválido. La duración debe ser un número.")
                    return
            
            guardar_servicios(servicios)
            print(f"Servicio '{nombre}' actualizado exitosamente.")
            return
    
    print(f"Servicio '{nombre}' no encontrado.")


def eliminar_servicio():
    nombre = pedir_texto("Ingrese el nombre del servicio que desea eliminar: ")
    servicios = cargar_servicios()
    
    for servicio in servicios:
        if servicio['nombre'].lower() == nombre.lower():
            servicios.remove(servicio)
            guardar_servicios(servicios)
            print(f"Servicio '{nombre}' eliminado exitosamente.")
            return
    
    print(f"Servicio '{nombre}' no encontrado.")