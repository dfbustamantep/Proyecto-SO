from recurso import Recurso
from proceso import Procesos

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
                recurso = str(input("Ingrese el id del recurso que va a necesitar el proceso: "))
                for rec in self.recursos:
                    if rec.get_id_recurso() == int(recurso):
                        recursosP.append(rec)
                        encontrado = True 
                        # Aca se comprueba si el recurso esta disponible se cambia la disponibilidad a false y mas adelante agregamos el proceos a la cola del recurso
                        '''
                        if rec.get_dipsonible() == True:
                            print("recurso pasando a usado")
                            rec.set_dipsonible(False)  
                        else: 
                            print("Recurso no disponible en este momento,el recurso sera asignado en orden de llegada")
                        '''  
                        # Vamos a agregar el proceso a la lista del recurso el cual necesita
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
        # Pasamos los elementos que estan en la cola de bloqueado a la cola de listo para mirar si ya se pueden ejecutar
        while self.cola_bloqueado:
            # Guardamos el proceso que este de primeras en la cola de nuevo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_bloqueado.pop(0)
            self.cambiar_estado("listo",proceso)
            
        # Pasamos los elementos que estan en la cola de nuevo a la cola de listo        
        while self.cola_nuevo:
            # Guardamos el proceso que este de primeras en la cola de nuevo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_nuevo.pop(0)
            self.cambiar_estado("listo",proceso)
          
        # Pasamos los elementos que estan en la cola de listo a ejecucion        
        while self.cola_listo:
            # Guardamos el proceso que este de primeras en la cola de listo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_listo.pop(0)
            recursos_necesarios = proceso.get_recursos()
            
            print("Recursos necesarios")
            for r in recursos_necesarios:
                print(r.mostrar_recurso())

            recursos_disponibles = True
            # Cambiamos el proceso a estado de ejecucion,ya en estado de ejecucion revisamos si los recursos estan disponibles
            self.cambiar_estado("ejecucion",proceso)
            
            #Comprobamos si todos los recursos que necesita se pueden usar al meomento
            for recurso in recursos_necesarios:
                print(f"Revisando disponibilidad del recurso: {recurso.get_nombre()}")
                #Si el nombre del recurso es alguno se verifica que este en la cola de ese recurso y este de primeras en esa cola
                if recurso.get_nombre() == "CPU":
                    #self.cpu.set_dipsonible(False)
                    if not (proceso in self.cola_cpu and self.cola_cpu[0] == proceso):
                        recursos_disponibles = False
                        print("Cola CPU")
                        for elemento in self.cola_cpu:
                            print("ID proceso:",elemento.get_id())  

                elif recurso.get_nombre() == "Memoria RAM":
                    if not(proceso in self.cola_memoria and self.cola_memoria[0] == proceso):
                        recursos_disponibles = False
                        print("Cola Memoria")
                        for elemento in self.cola_memoria:
                            print("ID proceso:",elemento.get_id())  
                        
                elif recurso.get_nombre() == "Disco Duro":
                    if not(proceso in self.cola_disco and self.cola_disco[0] == proceso):
                        recursos_disponibles = False
                        print("Cola DD")
                        for elemento in self.cola_disco:
                            print("ID proceso:",elemento.get_id())  
                        
                elif recurso.get_nombre() == "Impresora":
                    if not(proceso in self.cola_impresora and self.cola_impresora[0] == proceso):
                        recursos_disponibles = False
                        print("Cola Impresora")
                        for elemento in self.cola_impresora:
                            print("ID proceso:",elemento.get_id())  
                        
            # Si todos los recurso estan disponibles pasamos el proceso a ejecucion
            if recursos_disponibles:
                for recurso in recursos_necesarios:
                #Si el nombre del recurso es alguno se verifica que este en la cola de ese recurso y este de primeras en esa cola
                    if recurso.get_nombre() == "CPU":
                        self.cola_cpu.pop(0)
                                
                    elif recurso.get_nombre() == "Memoria RAM":
                        self.cola_memoria.pop(0)
                                
                    elif recurso.get_nombre() == "Disco Duro":
                        self.cola_disco.pop(0)
                                
                    elif recurso.get_nombre() == "Impresora":
                        self.cola_impresora.pop(0)
            
                
                print(f"Ejecutando proceso {proceso.get_id()}")
                
                proceso.simular_proceso()
                
                #Si el proceos tiene un tamanio de 0 quiere decir que ya finalizo
                if proceso.get_tamanio()==0:
                    self.cambiar_estado("terminado",proceso)
                    
                #print(proceso.get_estado())
                print()
                # Despyues de que se ejecute el proceso se deben liberar los recursos
                
                #Si el proceos no termino vuelve a la cola de listo
                if proceso.get_estado() != "terminado":
                    self.cambiar_estado("listo",proceso)

                    #Si el proceso no ha terminado,lo volvemos a agregar a la lista de recursos
                    for recurso in recursos_necesarios:
                        #
                        if recurso.get_nombre() == "CPU":
                            self.cola_cpu.append(proceso)
                                    
                        elif recurso.get_nombre() == "Memoria RAM":
                            self.cola_memoria.append(proceso)
                                    
                        elif recurso.get_nombre() == "Disco Duro":
                            self.cola_disco.append(proceso)
                                    
                        elif recurso.get_nombre() == "Impresora":
                            self.cola_impresora.append(proceso)

                
                        
            else:
                # Si no están todos los recursos, el proceso regresa a 'listo'
                print(f"Proceso {proceso.get_id()} no tiene todos los recursos disponibles. Pasa a la cola 'bloqueado'.")
                self.cola_bloqueado.append(proceso)
                self.cambiar_estado("bloqueado",proceso)
                
        self.mostrar_procesos()
        self.mostar_colas_estados()
    
    def cambiar_estado(self,nuevo_estado:str,proceso:Procesos):
        if nuevo_estado in BCP.estados_procesos:
            estado_anterior=proceso.get_estado()
            
            # Al cambiar de estado tenemos que quitar el proceso de la cola de procesos del estado que tenia,primero verificamos que si 
            # este en la cola del estado anterior y añadirla a la cola del nuevo estado
            
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

            # Cambiamos el estado del proceso
            proceso.set_estado(nuevo_estado)
            
            #Eliminamos el proceso de la cola en donde estaba
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
            
            
            
            
            
        
            
       