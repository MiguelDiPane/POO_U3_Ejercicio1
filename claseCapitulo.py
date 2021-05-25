class Capitulo:
    __titulo = ''
    __cantidadPaginas = 0

    def __init__(self,titulo='',cantPag=0):
        self.__titulo = titulo
        self.__cantidadPaginas = cantPag
    
    def getTituloCap(self):
        return self.__titulo
    
    def getCantPags(self):
        return self.__cantidadPaginas