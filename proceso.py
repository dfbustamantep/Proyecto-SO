from recurso import Recurso

class Procesos:
    # En caso de no especificar recursos se inicialza con None
    def __init__(self,id:int,tamanio:float,hilos:int,recursos:Recurso = None):
        # __ para hacer atributos privados
        self.__id_Proceso = id
        self.__tamanio=tamanio
        self.__recursos_necesarios = recursos # va a ser una lista de recursos
        self.__estado = "nuevo"
        self.__hilos = hilos
        # self.__ejecuciones = ejecuciones
        
    def get_id(self):
        return self.__id_Proceso
    
    def get_tamanio(self):
        return self.__tamanio
    
    def get_recursos(self):
        return self.__recursos_necesarios
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado:str):
        self.__estado = estado
        
    def get_hilos(self):
        return self.__hilos
            
    def mostrar_proceso(self):
        return (f"ID Proceso: {self.get_id()} \nTamaño: {self.get_tamanio()} "
                f"\nEstado: {self.get_estado()} \nHilos: {self.get_hilos()}"
                f"\nRecursos: {self.get_recursos()}")
        
    def simular_proceso (self):
        print(f"Proceso {self.get_id}")
        #self.__ejecuciones -= 1
        
        #if self.get_ejecuciones == 0 :
        #    self.__estado = "terminado"