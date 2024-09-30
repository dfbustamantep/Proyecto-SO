from recurso import Recurso
from proceso import Procesos

# Metodo estatico para imprimir lineas
@staticmethod
def printLines():
    print("----------------------------------------------------------------------")

#Bloque de Control del Proceso
class BCP:
    # Tupla de estados que pueden haber - La tupla es una estructura de datos inmutable
    estados_procesos = ("nuevo","listo","bloqueado","ejecucion","terminado")

    # Lsita donde se almacenaran todos los proceos
    procesos = []

    # Cola que se usara para cada proceso
    cola_nuevo =[]
    cola_listo =[]
    cola_bloqueado =[]
    cola_ejecucion =[]
    cola_terminado =[]

    # Recursos
    cpu = Recurso(1, "CPU")
    memoria = Recurso(2, "Memoria RAM")
    disco = Recurso(3, "Disco Duro")
    impresora = Recurso(4, "Impresora")
    
    # Tupla de recursos (No se puede modificiar)
    recursos = (cpu,memoria,disco,impresora)
    
    # Cola que se usara para cada recurso
    cola_cpu =[]
    cola_memoria =[]
    cola_disco =[]
    cola_impresora =[]
    
    
    def creacion_proceos(self):
        numero_procesos = int(input ("Ingrese el numero de procesos que desea crear: "))
        printLines()
        id_proceso = 00

        for i in range (0,numero_procesos):
            id_proceso += 1
            
            #print(id_proceso)
            print(f"\tProceso {id_proceso}")
            printLines()
            espacio = int(input("Ingrese el espacio requerido por el proceso: "))
            #ejecuciones = int(input("Ingrese el numero de veces a ejecutar el proceos: "))
            print("Recursos disponibles")
            for recurso in self.recursos:
                print(recurso.mostrar_recurso())
            
                            
            recursos = input("Ingrese los recursos que va a necesitar el proceso: ")
            hilos = int(input("Ingrese el numero de hilos que va a tener el proceos: "))
            
           
            printLines()
            
            # Creamos el proeceso y lo agregamos a la lista
            proceso = Procesos(id_proceso,espacio,hilos,recursos)
            # Agregamos el proceso a la lista de procesos
            self.procesos.append(proceso)
            
            # Vamos a agregar el proceso a la lista del estado al cual pertenece
            #if estado == "nuevo":
            #    self.cola_nuevo.append(proceso)
            #elif estado == "listo":
            #    self.cola_listo.append(proceso)
            #elif estado == "bloqueado":
            #    self.cola_bloqueado.append(proceso)
            #elif estado == "ejecucion":
            #    self.cola_ejecucion.append(proceso)
            #else:
            #    self.cola_terminado.append(proceso)
        
    
    def mostrar_procesos(self):
        print("\tProcesos")
        printLines()
        
        for elemento in self.procesos:
            print(elemento.mostrar_proceso())
            printLines()
            
    def mostar_colas(self):    
        print("\t\tColas de estados")
        printLines()
        
        print("\tCola nuevos")
        for elemento in self.cola_nuevo:
            print("ID proceso:",elemento.get_id())
        
        printLines()
        print("\tCola listos")    
        for elemento in self.cola_listo:
            print("ID proceso:",elemento.get_id())   

        printLines()
        print("\tCola bloqueados") 
        for elemento in self.cola_bloqueado:
            print("ID proceso:",elemento.get_id())
        
        printLines()
        print("\tCola ejecucion") 
        for elemento in self.cola_ejecucion:
            print("ID proceso:",elemento.get_id())  

        printLines()
        print("\tCola terminado") 
        for elemento in self.cola_terminado:
            print("ID proceso:",elemento.get_id())  
    
        
    def cambiar_estado(self,nuevo_estado:str,proceso:Procesos):
        if nuevo_estado in BCP.estados_procesos:
            estado_anterior=proceso.get_estado()
            
            # Al cambiar de estado tenemos que quitar el proceso de la cola de procesos del estado que tenia,primero verificamos que si 
            # este en la cola del estado anterior y añadirla a la cola del nuevo estado
            
            if estado_anterior == "nuevo":
                if proceso in self.cola_nuevo:
                    self.cola_nuevo.remove(proceso)
                    
            elif estado_anterior == "listo":
                if proceso in self.cola_listo:
                    self.cola_listo.remove(proceso)
                    
            elif estado_anterior == "bloqueado":
                if proceso in self.cola_bloqueado:
                    self.cola_bloqueado.remove(proceso)
                    
            elif estado_anterior == "ejecucion":
                if proceso in self.cola_ejecucion:
                    self.cola_ejecucion.remove(proceso)
                    
            elif estado_anterior == "terminado":
                if proceso in self.cola_terminado:
                    self.cola_terminado.remove(proceso)
            
            # Cambiamos el estado del proceso
            proceso.set_estado(nuevo_estado)
            
            
            if nuevo_estado == "nuevo":
                self.cola_nuevo.append(proceso)
            elif nuevo_estado == "listo":
               self.cola_listo.append(proceso)
            elif nuevo_estado == "bloqueado":
               self.cola_bloqueado.append(proceso)
            elif nuevo_estado == "ejecucion":
                self.cola_ejecucion.append(proceso)
            else:
                self.cola_terminado.append(proceso)
        
            
       