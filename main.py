# Tercera Práctica, tablas de dispersión, asignada en clase 9

from DirectorioContactos import DirectorioContactos

def intinput(string):
    flag = False
    while not flag:
        try:
            integer = int(input(string))
            flag = True
        except ValueError:
            print("No es un entero válido")
    return integer

size = intinput('Ingrese el tamaño del directorio: ')
directory = DirectorioContactos(size)

option = 0
while option != 5:
    option = intinput("Digite la opcion que requiera: \n"
                      "1. Agregar contacto \n"
                      "2. Mostrar todos los contactos \n"
                      "3. Buscar contacto \n"
                      "4. Eliminar contacto \n"
                      "5. Salir \n: ")
    match option:
        case 1:
            directory.insert(input('Ingrese el nombre: '),intinput('Ingrese el número telefónico: '))
        case 2:
            print(directory)
        case 3:
            if (number := directory.search(input('Ingrese el nombre: '))):
                print('Número:',number)
            else:
                print('No se encontró un contacto con ese nombre')
        case 4:
            if directory.delete(input('Ingrese el nombre: ')):
                print('Contacto eliminado')
            else:
                print('No se encontró un contacto con ese nombre')
        case 5:
            print('Saliendo del programa...')
        case _:
            print('Opción no válida')