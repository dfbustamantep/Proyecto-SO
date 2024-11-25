class Recurso:
    
    def __init__(self,id:int,nombre:str,disponible:bool = True):
        # __ para hacer atributos privados
        self.__id_recurso = id
        self.__nombre=nombre
        self.__disponible = disponible 
    
    def set_disponible(self,disponible:bool):
        self.__dipsonible = disponible
    
    def get_id_recurso(self):
        return self.__id_recurso
            
    def get_nombre(self):
        return self.__nombre
     
    def get_disponible(self):
        return self.__disponible
    
    def mostrar_recurso(self):
        return (f"ID recurso: {self.get_id_recurso()} \nNombre del recurso: {self.get_nombre()} "
                f"\nRecurso disponible: {self.get_disponible()}")
    
       