import recurso
from proceso import Procesos

# Metodo estatico para imprimir lineas
@staticmethod
def printLines():
    print("----------------------------------------------------------------------")

#Bloque de Control del Proceso
class BCP:
    # Tupla de estados que pueden haber - La tupla es una estructura de datos inmutable
    estados_procesos = ("listo","bloqueado","ejecucion","terminado")

    # Lsita donde se almacenaran todos los proceos
    procesos = []

    #Cola que se usara para cada proceso
    cola_listo =[]
    cola_bloqueado =[]
    cola_ejecucion =[]
    cola_terminado =[]

    # Recursos
    recursos = ()
    recurso1 = []
    
    def creacion_proceos(self):
        numero_procesos = int(input ("Ingrese el numero de procesos que desea crear "))
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
            estado=input("Ingrese cual va a ser el estado inicial del proceso (listo,bloqueado,ejecucion,terminado): ")
            while estado not in self.estados_procesos:
                print("Ingrese un estado valido")
                estado = input()
            printLines()
            proceso = Procesos(id_proceso,espacio,estado,ejecuciones,numero_recursos)
            self.procesos.append(proceso)
        
        
    
    def mostrar_procesos(self):
        for elemento in self.procesos:
            print(elemento.mostrarProceso())
        
       