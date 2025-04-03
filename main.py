
from servicios import *

def menu():
    while True:
        print("\n--- Menú de Gestión de Servicios Fotográficos ---")
        print("1. Agregar servicio")
        print("2. Editar servicio")
        print("3. Eliminar servicio")
        print("4. Ver todos los servicios")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_servicio()
        elif opcion == '2':
            editar_servicio()
        elif opcion == '3':
            eliminar_servicio()
        elif opcion == '4':
            servicios = cargar_servicios()
            if servicios:
                print("\nServicios Fotográficos Registrados:")
                for servicio in servicios:
                    print(servicio)
            else:
                print("No hay servicios registrados.")
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
MENU