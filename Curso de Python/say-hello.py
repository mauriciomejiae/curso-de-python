# -*- coding: utf-8 -*-


def saludo():
    edad = int(input('Hola!, ¿cual es tu edad?'))

    saludar(edad)

def saludar(edad):
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

if __name__ == '__main__':
    saludo()