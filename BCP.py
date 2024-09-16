import recurso
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
    recursos = ()
    recurso1 = []
    
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
            ejecuciones = int(input("Ingrese el numero de veces a ejecutar el proceos: "))
            numero_recursos = input("Ingrese los recursos que va a necesitar el proceso: ")
            
            estado=input("Ingrese cual va a ser el estado inicial del proceso (nuevo,listo,bloqueado,ejecucion,terminado): ")
            while estado not in self.estados_procesos:
                print("Ingrese un estado valido")
                estado = input()
            printLines()
            
            # Creamos el proeceso y lo agregamos a la lista
            proceso = Procesos(id_proceso,espacio,estado,ejecuciones,numero_recursos)
            # Agregamos el proceso a la lista de procesos
            self.procesos.append(proceso)
            
            # Vamos a agregar el proceso a la lista del estado al cual pertenece
            if estado == "nuevo":
                self.cola_nuevo.append(proceso)
            elif estado == "listo":
                self.cola_listo.append(proceso)
            elif estado == "bloqueado":
                self.cola_bloqueado.append(proceso)
            elif estado == "ejecucion":
                self.cola_ejecucion.append(proceso)
            else:
                self.cola_terminado.append(proceso)
        
    
    def mostrar_procesos(self):
        print("\tProcesos")
        printLines()
        
        for elemento in self.procesos:
            print(elemento.mostrarProceso())
            printLines()
        
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
    
    
        
       