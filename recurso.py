class Recurso:
    
    def __init__(self,id:int,nombre:str,dipsonible:bool = True):
        # __ para hacer atributos privados
        self.__id_recurso = id
        self.__nombre=nombre
        self.__dipsonible = dipsonible 
    
    def set_dipsonible(self,dipsonible:bool):
        self.__dipsonible = dipsonible
    
    def get_id_recurso(self):
        return self.__id_recurso
            
    def get_nombre(self):
        return self.__nombre
     
    def get_dipsonible(self):
        return self.__dipsonible
    
    def mostrar_recurso(self):
        return (f"ID recurso: {self.get_id_recurso()} \nNombre del recurso: {self.get_nombre()} "
                f"\nRecurso disponible: {self.get_dipsonible()}")
    
       