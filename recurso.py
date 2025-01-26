class Recurso:
    
    def __init__(self,id:int,nombre:str):
        # __ para hacer atributos privados
        self.__id_recurso = id
        self.__nombre=nombre
    
    def get_id_recurso(self):
        return self.__id_recurso
            
    def get_nombre(self):
        return self.__nombre
  
    def mostrar_recurso(self):
        return (f"ID recurso: {self.get_id_recurso()} \nNombre del recurso: {self.get_nombre()}")
    
       