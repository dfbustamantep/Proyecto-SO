
class Memoria:
    def __init__(self,tipo:str,tamanio:int,tamanio_marco:int):
        self.__tipo = tipo
        self.__tamanio = tamanio
        self.__tamanio_inicial = tamanio
        self.__tamanio_marco = tamanio_marco
        self.__paginas = self.calcular_numero_paginas()
        self.__matriz_memoria = ['O'] * self.__paginas
    #Getters
    def get_tipo(self):
        return self.__tipo
    
    def get_tamanio(self):
        return self.__tamanio
    
    def get_tamanio_inicial(self):
        return self.__tamanio_inicial
    
    def get_tamanio_marco(self):
        return self.__tamanio_marco

    def get_matriz_memoria(self):
       return self.__matriz_memoria
   
    def get_paginas(self):
        return self.__paginas
    #setters
    def set_tamanio(self,tamanio_nuevo:int):
        self.__tamanio = tamanio_nuevo
    
    def calcular_numero_paginas(self):
        # // divison entera/quiere decir que solo nos da el numero entero
        return self.__tamanio//self.__tamanio_marco
    
    