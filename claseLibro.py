from claseCapitulo import Capitulo

class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = ''
    __cantidadCapitulos = 0
    __capitulos = []

    def __init__(self,idLibro,titulo,autor,editorial,isbn,cantidadCapitulos):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isbn = isbn
        self.__cantidadCapitulos = cantidadCapitulos
        self.__capitulos = []
    
    def addCapitulo(self,titulo,cantPags):
        newCapitulo = Capitulo(titulo,cantPags)
        self.__capitulos.append(newCapitulo)
    
    def getId(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor

    def calcCantPags(self):
        totalPags = 0
        for capitulo in self.__capitulos:
             totalPags += capitulo.getCantPags() #voy sumando las paginas
        return totalPags

    def getTitulosCapitulos(self):
        caps = []
        for capitulo in self.__capitulos:
            tituloCap = capitulo.getTituloCap()
            caps.append(tituloCap) #voy guardando los titulos de los capitulos
        caps
        return caps

    def showData(self):
        titulosCaps = self.getTitulosCapitulos()
        cantPaginas = self.calcCantPags()
        titulo = self.getTitulo()
        header = '+'+'-'*50+'+'
        print(header)
        print('|{0:^50}|'.format('FICHA LIBRO'))
        print(header)
        print('| Titulo: {0:41}|'.format(titulo))
        print(header)
        print('| {0:49}|'.format('Capitulos:'))
        i = 1
        for capitulo in titulosCaps: #Lista con los titulos de los capitulos
            print('|  {0}- {1:45}|'.format(i,capitulo))
            i+=1
        print(header)
        print('| Cantidad total de paginas: {0:22}|'.format(str(cantPaginas)))
        print(header)