from claseLibro import Libro

class ManejadorLibro:
    __libros = []

    def __init__(self):
        self.__libros = []

    def addLibro(self,id,titulo,autor,editorial,isbn,cantcapt):
        if id.isdigit() and cantcapt.isdigit():
            id = int(id)
            cantcapt = int(cantcapt)
            newLibro = Libro(id,titulo,autor,editorial,isbn,cantcapt)
            self.__libros.append(newLibro)
    
    def setCapitulo(self,idLibro,titulo,cantPags):
        if idLibro.isdigit() and cantPags.isdigit():
            idLibro = int(idLibro)
            cantPags = int(cantPags)
            pos = idLibro - 10001
            self.__libros[pos].addCapitulo(titulo,cantPags)
    
    def searchLibro(self,idLibro):
        if idLibro.isdigit():
            idLibro = int(idLibro)
            i = 0
            esta = False
            while i < len(self.__libros) and not esta:
                idBuscada = self.__libros[i].getId()
                if idBuscada == idLibro:
                    esta = True
                    libro = self.__libros[i]
                i += 1
            if esta:
                #Muestro los datos del libro encontrado
                libro.showData()
            else:
                print('Libro no encontrado.')
        else:
            print('Error: ID de libro incorrecta')
    
    def searchPalabra(self,palabra):
        #Encabezado
        header = '+'+'-'*50+'+'
        print(header)
        print('|{0:^50}|'.format('BUSQUEDA POR PALABRA'))
        print(header)
        print('| Palabra buscada: {0:32}|'.format(palabra))
        print(header)
        print('| {0:49}|'.format('Coincidencias:'))
        
        #Busqueda
        palabra = palabra.lower()
        ninguna = True
        for libro in self.__libros:
            #Analizo el titulo
            titulo = libro.getTitulo()
            tituloMin = titulo.lower()
            esta = tituloMin.find(palabra)
            if esta == -1:
                #Si no esta en el titulo analizo los titulos de los capitulos
                j = 0
                titulosCaps = libro.getTitulosCapitulos() 
                while j < len(titulosCaps) and esta == -1:
                    tituloCapsMin = titulosCaps[j].lower()
                    if tituloCapsMin.find(palabra) != -1:
                        esta = 1
                    j += 1     
            #Analizo el resultado de busqueda en titulo y titulo capitulos y muestro resultados
            if esta != -1:
                if ninguna:
                    ninguna = False
                autor = libro.getAutor()  
                print('| Titulo: {0:41}|'.format(titulo))
                print('| -Autor: {0:41}|'.format(autor))
        if ninguna:
            frase = 'La palabra ' +palabra+ ' no fue encontrada.'
            print('| {0:49}|'.format(frase))
        print(header)