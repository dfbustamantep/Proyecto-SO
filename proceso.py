class Procesos:
    # En caso de no especificar recursos se inicialza con None
    def __init__(self,id,tamanio,hilos,recursos = None):
        # __ para hacer atributos privados
        self.__id_Proceso = id
        self.__tamanio=tamanio
        self.__recursos_necesarios = recursos # va a ser una lista de recursos
        self.__estado = "nuevo";
        self.__hilos = hilos;
        # self.__ejecuciones = ejecuciones
        
    def get_id(self):
        return self.__id_Proceso
    
    def get_tamanio(self):
        return self.__tamanio
    
    def get_recursos(self):
        return self.__recursos_necesarios
    
    def get_estado(self):
        return self.__estado
        
    #def get_ejecuciones(self):
    #    return self.__ejecuciones
            
    def mostrarProceso(self):
        return (f"ID Proceso: {self.get_id()} \nTamaño: {self.get_tamanio()} "
                f"\nEstado: {self.get_estado()}"
                f"\nRecursos: {self.get_recursos()}")
        
    def simular_proceso (self):
        print(f"Proceso {self.get_id}")
        #self.__ejecuciones -= 1
        
        if self.get_ejecuciones == 0 :
            self.__estado = "terminado"