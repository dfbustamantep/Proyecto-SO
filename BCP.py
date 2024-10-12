from recurso import Recurso
from proceso import Procesos

# Metodo estatico para imprimir lineas
#@staticmethod
def printLines():
    print("----------------------------------------------------------------------")

#Bloque de Control del Proceso
class BCP:
    # Tupla de estados que pueden haber - La tupla es una estructura de datos inmutable
    estados_procesos = ("nuevo","listo","bloqueado","ejecucion","terminado")

    # Lista donde se almacenaran todos los proceos
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
    
    # Lista de recursos 
    recursos = [cpu,memoria,disco,impresora]
    
    # Cola que se usara para cada recurso
    cola_cpu =[]
    cola_memoria =[]
    cola_disco =[]
    cola_impresora =[]
    
    
    def creacion_procesos(self):
        try:
            numero_procesos = int(input("Ingrese el número de procesos que desea crear: "))
            printLines()
        except ValueError:
            print("Por favor, ingrese un número válido.")
            printLines()
            return
        
        
        id_proceso = 00

        for i in range (0,numero_procesos):
            id_proceso += 1
            
            print(f"\tProceso {id_proceso}")
            printLines()
            espacio = int(input("Ingrese el espacio requerido por el proceso: "))
            #ejecuciones = int(input("Ingrese el numero de veces a ejecutar el proceos: "))
            hilos = int(input("Ingrese el numero de hilos que va a tener el proceos: "))
            
            print("Recursos disponibles")
            printLines()
            for recurso in self.recursos:
                print(recurso.mostrar_recurso())
            
            # proc es la variable que va a controlar el ciclo while,inicialmente es true para que pregunte por el primer recursos 
            # que se va a necesitar
            proc = True
            
            # Recuros que necesita el proceso
            recursosP =[]
            # Creamos el proeceso y lo agregamos a la lista
            proceso = Procesos(id_proceso,espacio,hilos)    
            
            while proc: 
                encontrado = False
                printLines()                            
                recurso = input("Ingrese el id del recurso que va a necesitar el proceso: ")
                for rec in self.recursos:
                    if rec.get_id_recurso() == int(recurso):
                        recursosP.append(rec)
                        encontrado = True
                        '''
                        if rec.get_dipsonible() == True:
                            print("recurso pasando a usado")
                            rec.set_dipsonible(False)  
                        else: 
                            print("Recurso no disponible en este momento,el recurso sera asignado en orden de llegada")
                        '''    
                        # Vamos a agregar el proceso a la lista del recurs el cual necesita
                        if rec.get_nombre() == "CPU":
                            self.cola_cpu.append(proceso)
                        elif rec.get_nombre() == "Memoria RAM":
                                self.cola_memoria.append(proceso)
                        elif rec.get_nombre() == "Disco Duro":
                            self.cola_disco.append(proceso)
                        elif rec.get_nombre() == "Impresora":
                            self.cola_impresora.append(proceso)
                        else:
                            print("No se agrego a la cola del recurso")
               
                if not encontrado:
                    print("ID de recurso inexistente")
         
                proc=input("Desea agregar otro recurso?(s/n): ").lower()
                if(proc!='s'):
                    proc = False
        
            
           
            printLines()
     
            # Creamos el proeceso y lo agregamos a la lista
            #proceso = Procesos(id_proceso,espacio,hilos,recursosP)
            proceso.set_recursos(recursosP)
            self.cola_nuevo.append(proceso)
            # Agregamos el proceso a la lista de procesos
            self.procesos.append(proceso)
            # printLines()
            
        self.mostar_colas_recursos()
        print()
        self.mostar_colas_estados()
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
        printLines()
        print("\tProcesos")
        printLines()
        
        for elemento in self.procesos:
            # Recorremos la lista de procesos,tomando cada procesos y mostrando sus datos
            elemento.mostrar_proceso()
            printLines()
            
    def mostar_colas_recursos(self):    
        print("\t\tColas de recursos")
        printLines()
        
        print("\tCola CPU")
        for elemento in self.cola_cpu:
            print("ID proceso:",elemento.get_id())
        
        printLines()
        print("\tCola Memoria")    
        for elemento in self.cola_memoria:
            print("ID proceso:",elemento.get_id())   

        printLines()
        print("\tCola Disco") 
        for elemento in self.cola_disco:
            print("ID proceso:",elemento.get_id())
        
        printLines()
        print("\tCola Impresora") 
        for elemento in self.cola_impresora:
            print("ID proceso:",elemento.get_id())  

    def mostar_colas_estados(self):    
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
    
    def ejecutar(self):
        # Pasamos los elementos que estan en la cola de nuevo a la cola de listo
        print("Cola nuevo")
        for elemento in self.cola_nuevo:
            print("ID proceso:",elemento.get_id())
        
        while self.cola_nuevo:
            # Guardamos el proceso que este de primeras en la cola de listo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_nuevo.pop(0)
            proceso.set_estado("listo")
            self.cola_listo.append(proceso)
        
        print("Cola listo")
        for elemento in self.cola_listo:
            print("ID proceso:",elemento.get_id())
    
    '''
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
            
            
            # Realizamos el cambio de estado,pero para hacer este cambio verificamos que este si se pueda hacer teniendo en cuenta la grafica que esta en el reademe
            if nuevo_estado == "listo" and (estado_anterior=="nuevo" or estado_anterior=="ejecucion" or estado_anterior=="bloqueado"):
               self.cola_listo.append(proceso)
            elif nuevo_estado == "bloqueado" and estado_anterior=="ejecucion":
               self.cola_bloqueado.append(proceso)
            elif nuevo_estado == "ejecucion" and estado_anterior == "listo":
                self.cola_ejecucion.append(proceso)
            elif nuevo_estado == "terminado" and estado_anterior == "ejecucion":
                self.cola_terminado.append(proceso)
            else:
                print("El cambio de estado no se puede realizar")
    '''    
            
       