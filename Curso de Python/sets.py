# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

def run():
    while True:
        country = str(input('Escribe el nombre de un país: ')).lower()

        if country == 's':
            break

        try:
            print('La población de {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            print('No tenemos el dato de la población de {}'.format(country))
        else:
            print('Resultado Exitoso')
        finally:
            print('A continuación, ingrese la letra s para salir o el nombre de otro país')


if __name__ == '__main__':
    print('P O B L A C I O N E S  D E  C A D A  P A I S')
    run() 