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