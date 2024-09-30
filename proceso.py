

from recurso import Recurso

def printLines():
    print("----------------------------------------------------------------------")
    
class Procesos:
    # En caso de no especificar recursos se inicialza con None
    def __init__(self,id:int,tamanio:float,hilos:int,recursos:list[Recurso] = None):
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
        
    def set_recursos(self,recursos:list[Recurso]):              
        self.__recursos_necesarios = recursos
        
    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado:str):
        self.__estado = estado
        
    def get_hilos(self):
        return self.__hilos
            
    def mostrar_proceso(self):
        print(f"ID Proceso: {self.get_id()}")
        print(f"Tamaño: {self.get_tamanio()}")
        print(f"Estado: {self.get_estado()}") 
        print(f"Hilos: {self.get_hilos()}")
        print("Recursos necesarios:")
        printLines()
        for recurso in self.__recursos_necesarios:
            if recurso:
                print(f"\tID: {recurso.get_id_recurso()} Nombre:{recurso.get_nombre()}")
            else:
                print("vacio")
        
        return ""
        
        
        
    def simular_proceso (self):
        print(f"Proceso {self.get_id}")
        #self.__ejecuciones -= 1
        
        #if self.get_ejecuciones == 0 :
        #    self.__estado = "terminado"