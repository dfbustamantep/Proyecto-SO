import random

class Memoria:
    def __init__(self,tipo:str,tamanio:int,tamanio_marco:int):
        self.__tipo = tipo
        self.__tamanio = tamanio
        self.__tamanio_inicial = tamanio
        self.__tamanio_marco = tamanio_marco
        self.__paginas = self.calcular_numero_paginas()
        self.__matriz_memoria = ['O'] * self.__paginas
        
        if self.__tipo.lower() == "memoria principal":
            self.__matriz_memoria = ['SO'] + ['O'] * (self.__paginas-1)
        else:
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
        
    def set_matriz(self,matriz):
        self.__matriz_memoria = matriz
    
    def calcular_numero_paginas(self):
        # // divison entera/quiere decir que solo nos da el numero entero
        return self.__tamanio//self.__tamanio_marco
    
    def get_paginas_dipsonibles(self):
        return self.__paginas - sum(1 for marco in self.__matriz_memoria if marco != 'O')
    
    def set_paginas_ocuapadas(self,numero_paginas:int,proceso:str,tamanio_pagina:int,id_pagina_proceso:int=00):
        # Mientras el numero de paginas que ocupa el proceso es diferente de 0
        while numero_paginas>0:
            id_pagina_proceso += 1 
            # Generamos un indice aleatorio al cual vamos a ocupar con el proceso
            indice_aleatorio = random.randint(0, len(self.__matriz_memoria) - 1)
            print()

            if self.__matriz_memoria[indice_aleatorio] == 'O':
                self.__matriz_memoria[indice_aleatorio] = proceso + "."+str(id_pagina_proceso)
                self.__tamanio -= tamanio_pagina
                numero_paginas -= 1
        
        return id_pagina_proceso
    
    def set_liberar_paginas(self,proceso:str):
        print("Liberar paginas")
        print(proceso)
        for i in range(len(self.__matriz_memoria)):
            
            if self.__matriz_memoria[i].startswith(proceso):
                print(self.__matriz_memoria[i])
                self.__matriz_memoria[i]='O'
                print(f"Página liberada: {i} del proceso {proceso}")
            #else:
                #print(f"posicion {i} {self.__matriz_memoria[i]}")