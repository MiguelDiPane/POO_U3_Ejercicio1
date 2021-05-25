import csv
from claseManejadorLibros import ManejadorLibro
from claseMenu import Menu

if __name__ == '__main__':
    manejador = ManejadorLibro()
    archivo = open('libros.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        if fila[0].isdigit(): #Leyo el ID de un libro
            idLibro = fila[0]
            manejador.addLibro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        else: #Leyo un capitulo 
            manejador.setCapitulo(idLibro,fila[0],fila[1])
    archivo.close() 

    miMenu = Menu()
    miMenu.define_menu('Menu de opciones',['[1] - Buscar libro','[2] - Buscar por palabra','[0] - Salir'])
    miMenu.showMenu()
    op = miMenu.selectOption()

    while op != 0:
        #Apartado 1
        if op == 1:
            idLibro = input('Ingrese id de libro a buscar: ')
            manejador.searchLibro(idLibro)
            input('Presione ENTER para continuar...')
        #Apartado 2
        elif op == 2:
            palabra = input('Ingrese una palabra: ')
            manejador.searchPalabra(palabra)
            input('Presione ENTER para continuar...')

        miMenu.showMenu()
        op = miMenu.selectOption()