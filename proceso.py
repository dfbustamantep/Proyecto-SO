class Procesos:
    # En caso de no especificar recursos se inicialza con None
    def __init__(self,id,espacio,estado,ejecuciones,recursos = None):
        # __ para hacer atributos privados
        self.__id_Proceso = id
        self.__espacio=espacio
        self.__recursos_necesarios = recursos # va a ser una lista de recursos
        self.__estado = estado 
        self.__ejecuciones = ejecuciones
        
    def get_id(self):
        return self.__id_Proceso
    
    def get_espacio(self):
        return self.__espacio
    
    def get_recursos(self):
        return self.__recursos_necesarios
    
    def get_estado(self):
        return self.__estado
        
    def get_ejecuciones(self):
        return self.__ejecuciones
    
    def simular_proceso (self):
        print(f"Proceso {self.get_id}")
        self.__ejecuciones -= 1
        
        if self.get_ejecuciones == 0 :
            self.__estado = "terminado"
            
    def mostrarProceso(self):
        return (f"ID Proceso: {self.get_id()} \nEspacio: {self.get_espacio()} "
                f"\nEstado: {self.get_estado()} \nEjecuciones: {self.get_ejecuciones()} "
                f"\nRecursos: {self.get_recursos()}")