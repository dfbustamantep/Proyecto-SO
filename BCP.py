from recurso import Recurso
from proceso import Procesos
from memoria import Memoria
import math

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
    
    # El tamanio de las memorias siempore deberia ser una potencia de 2
    '''
    2**0=1      2**1=2      
    2**2=4      2**3=8      
    2**4=16     2**5=32     
    2**6=64     2**7=128    
    2**8=256    2**9=512    
    2**10=1024
    '''
    # tamaño memoria RAM(Principal)
    tamanio_MP = 2**8

    # tamaño memoria virtual (2 veces el tamaño de la memoria principal)
    tamanio_MV = tamanio_MP*2

    # tamaño del marco de pagina 4 unidades 
    tamanio_marco = 4
    '''
    El tamaño del marco de pagina coge el tamanio del proceso y lo divide entre el quiere decir que si tenemos
    un proceos de tamanio 100,a la memoria principal van 30 y a la virtual 70,de esos 30 se divide entre 5 y 
    nos da 6,que serian el numero de paginas
    '''
    #intercambio de pagians se da despues de ejecucion
    # cuando esta bloqueado las paginas no se cambian
    # cuando el proceso termina libera la memoria

    # la primera fila de la memoria ram siempre va a tener el SO
    # Procentaje del proceso que se va a subir a la memoria ram y memoria secundaria
    porcentaje_MP = 0.3
    porcentaje_MV = 0.7

    memoria_principal = Memoria("Memoria principal",tamanio_MP,tamanio_marco)
    memoria_virtual = Memoria("Memoria virtual",tamanio_MV,tamanio_marco)

    proceso_ejecutado = 0
    # Getters y setters
    def get_procesos(self):
        return self.procesos
    
    def set_procesos(self,procesos:list[Procesos]):
        self.procesos=procesos
    
    def get_cola_nuevo(self):
        return self.cola_nuevo
    
    def set_cola_nuevo(self,cola_nuevo:list[Procesos]):
        self.cola_nuevo=cola_nuevo
        
    def get_cola_listo(self):
        return self.cola_listo
    
    def set_cola_listo(self,cola_listo:list[Procesos]):
        self.cola_listo=cola_listo
        
    def get_cola_bloqueado(self):
        return self.cola_bloqueado
    
    def set_cola_bloqueado(self,cola_bloqueado:list[Procesos]):
        self.cola_bloqueado=cola_bloqueado
    
    def get_cola_ejecucion(self):
        return self.cola_ejecucion
    
    def set_cola_ejecucion(self,cola_ejecucion:list[Procesos]):
        self.cola_ejecucion=cola_ejecucion
    
    def get_cola_terminado(self):
        return self.cola_terminado
    
    def set_cola_terminado(self,cola_terminado:list[Procesos]):
        self.cola_terminado=cola_terminado

    def get_lista_recursos(self):
        return self.recursos
    
    def set_lista_recursos(self,lista_recursos:list[Recurso]):
        self.recursos=lista_recursos 
    
    def get_cola_cpu(self):
        return self.cola_cpu
    
    def set_cola_cpu(self,cola_cpu:list[Recurso]):
        self.cola_cpu=cola_cpu
        
    def get_cola_memoria(self):
        return self.cola_memoria
    
    def set_cola_memoria(self,cola_memoria:list[Recurso]):
        self.cola_memoria=cola_memoria
    
    def get_cola_disco(self):
        return self.cola_disco
    
    def set_cola_disco(self,cola_disco:list[Recurso]):
        self.cola_disco=cola_disco
        
    def get_cola_impresora(self):
        return self.cola_impresora
    
    def set_cola_impresora(self,cola_impresora:list[Recurso]):
        self.cola_impresora=cola_impresora

    def get_tamanio_MP(self):
        return self.tamanio_MP

    def get_tamanio_MV(self):
        return self.tamanio_MV

    def get_tamanio_marco(self):
        return self.tamanio_marco   

    def get_porcentaje_MP(self):
        return self.porcentaje_MP

    def get_porcentaje_MV(self):
        return self.porcentaje_MV  

    def get_memoria_principal(self):
        return self.memoria_principal

    def get_memoria_virtual(self):
        return self.memoria_virtual 
    
    def get_proceso_ejecutado(self):
        return self.proceso_ejecutado
     
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
            # Math.ceil se usa para aproximar al siguiente entero en caso de que la division no se exacta
            paginas_proceso = math.ceil(espacio/self.tamanio_marco)
            paginas_memoria_principal=math.ceil(paginas_proceso*self.porcentaje_MP)
            paginas_memoria_virtual=paginas_proceso-paginas_memoria_principal
            
            #print(f"paginas disponibles memoria ram {self.memoria_principal.get_paginas_dipsonibles()}")
            #print(f"paginas disponibles memoria virtual {self.memoria_virtual.get_paginas_dipsonibles()}")
            print(f"El proceso requiere el uso de {paginas_proceso} paginas,de las cuales {self.porcentaje_MP*100}% van a la memoria principal y el resto a memoria virtual")
            if self.memoria_principal.get_paginas_dipsonibles()>= paginas_memoria_principal:
                print("El proceso tiene espacio suficiente en memoria RAM y virtual para ser creado")
                
                ultimo_id = self.memoria_principal.set_paginas_ocuapadas(paginas_memoria_principal,"p"+str(id_proceso),self.tamanio_marco,00)
                self.memoria_virtual.set_paginas_ocuapadas(paginas_memoria_virtual,"p"+str(id_proceso),self.tamanio_marco,ultimo_id)
                
            elif self.memoria_virtual.get_paginas_dipsonibles()>= paginas_proceso:
                print("El proceso no tiene espacio suficiente en memoria RAM,si embargo se puede crear en la memoria virtual")
                self.memoria_virtual.set_paginas_ocuapadas(paginas_memoria_virtual,"p"+str(id_proceso),self.tamanio_marco)
            else:
                print("El proceso no tiene espacio suficiente en memoria RAM ni en memoria virtual para ser creado")
                return 
            
            self.print_memorias()
            #print(f"Paginas proceso {paginas_proceso},paginas memoria ram {paginas_memoria_ram},paginas memoria virtual {paginas_memoria_virtual}")
            hilos = int(input("Ingrese el numero de hilos que va a tener el proceso: "))
            
            preminencia = input("El proceso tiene o no preminencia (si/no):").lower() in ['sí','si','s']
            
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
            proceso = Procesos(id_proceso,espacio,hilos,None,preminencia)    
            
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
            #proceso.set_preminencia(preminencia)
            self.cola_nuevo.append(proceso)
            # Agregamos el proceso a la lista de procesos
            self.procesos.append(proceso)
            # printLines()
            
        self.mostar_colas_recursos()
        print()
        self.mostar_colas_estados()

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
        if self.cola_bloqueado:
            # Guardamos el proceso que este de primeras en la cola de nuevo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_bloqueado.pop(0)
            # Si tiene preminencia, asegurarnos que obtiene los recursos
            if proceso.get_preminencia():
                # Liberar los recursos que necesita
                for recurso in proceso.get_recursos():
                    if recurso.get_nombre() == "CPU" and self.cola_cpu:
                        #Eliminamos el proceso si ya esta en la cola
                        self.cola_cpu = [p for p in self.cola_cpu if p != proceso]
                        # ultima psocion de la cola
                        indice_insercion = 0
                        for proceso_n in self.cola_cpu:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_cpu.insert(indice_insercion,proceso)
                    elif recurso.get_nombre() == "Memoria RAM" and self.cola_memoria:
                        self.cola_memoria = [p for p in self.cola_memoria if p != proceso]
                        # ultima psocion de la cola
                        indice_insercion = 0
                        for proceso_n in self.cola_memoria:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_memoria.insert(indice_insercion,proceso)
                    elif recurso.get_nombre() == "Disco Duro" and self.cola_disco:
                        self.cola_disco = [p for p in self.cola_disco if p != proceso]
                        # ultima psocion de la cola
                        indice_insercion = 0
                        for proceso_n in self.cola_disco:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_disco.insert(indice_insercion,proceso)
                    elif recurso.get_nombre() == "Impresora" and self.cola_impresora:
                        self.cola_impresora = [p for p in self.cola_impresora if p != proceso]
                        # ultima psocion de la cola
                        indice_insercion = 0
                        for proceso_n in self.cola_impresora:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_impresora.insert(indice_insercion,proceso)
                        
            self.cambiar_estado("listo",proceso)
            
        # Pasamos los elementos que estan en la cola de nuevo a la cola de listo        
        if self.cola_nuevo:
            # Guardamos el proceso que este de primeras en la cola de nuevo,le cambiamos el estado a listo,y lo añadimos a la cola de listo
            proceso = self.cola_nuevo.pop(0)
            self.cambiar_estado("listo",proceso)
          
        # Pasamos los elementos que estan en la cola de listo a ejecucion        
        if self.cola_listo:
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
                    if proceso in self.cola_cpu:
                        # Si tiene preminencia y no está primero, lo movemos al inicio
                        if proceso.get_preminencia():
                            self.cola_cpu.remove(proceso)
                            self.cola_cpu.insert(0, proceso)
                        # Verificar si está primero en la cola
                        if self.cola_cpu[0] != proceso:
                            recursos_disponibles = False
                            print("Cola CPU")
                            for elemento in self.cola_cpu:
                                print("ID proceso:", elemento.get_id())

                elif recurso.get_nombre() == "Memoria RAM":
                    if proceso in self.cola_memoria:
                        # Si tiene preminencia y no está primero, lo movemos al inicio
                        if proceso.get_preminencia():
                            self.cola_memoria.remove(proceso)
                            self.cola_memoria.insert(0, proceso)
                        # Verificar si está primero en la cola
                        if self.cola_memoria[0] != proceso:
                            recursos_disponibles = False
                            print("Cola Memoria")
                            for elemento in self.cola_memoria:
                                print("ID proceso:", elemento.get_id())
                                
                elif recurso.get_nombre() == "Disco Duro":
                    if proceso in self.cola_disco:
                        # Si tiene preminencia y no está primero, lo movemos al inicio
                        if proceso.get_preminencia():
                            self.cola_disco.remove(proceso)
                            self.cola_disco.insert(0, proceso)
                        # Verificar si está primero en la cola
                        if self.cola_disco[0] != proceso:
                            recursos_disponibles = False
                            print("Cola DD")
                            for elemento in self.cola_disco:
                                print("ID proceso:", elemento.get_id())
                                
                elif recurso.get_nombre() == "Impresora":
                    if proceso in self.cola_impresora:
                        # Si tiene preminencia y no está primero, lo movemos al inicio
                        if proceso.get_preminencia():
                            self.cola_impresora.remove(proceso)
                            self.cola_impresora.insert(0, proceso)
                        # Verificar si está primero en la cola
                        if self.cola_impresora[0] != proceso:
                            recursos_disponibles = False
                            print("Cola Impresora")
                            for elemento in self.cola_impresora:
                                print("ID proceso:", elemento.get_id()) 
                        
            # Si todos los recurso estan disponibles pasamos el proceso a ejecucion
            if recursos_disponibles:
                proceso_ejecutando = None
                for recurso in recursos_necesarios:
                #Si el nombre del recurso es alguno se verifica que este en la cola de ese recurso y este de primeras en esa cola
                    if recurso.get_nombre() == "CPU" and self.cola_cpu:
                        self.cola_cpu.pop(0)
                                
                    elif recurso.get_nombre() == "Memoria RAM" and self.cola_memoria:
                        self.cola_memoria.pop(0)
                                
                    elif recurso.get_nombre() == "Disco Duro" and self.cola_disco:
                        self.cola_disco.pop(0)
                                
                    elif recurso.get_nombre() == "Impresora" and self.cola_impresora:
                        self.cola_impresora.pop(0)
            
                
                print(f"Ejecutando proceso {proceso.get_id()} tamanio {proceso.get_tamanio()}")
                proceso.simular_proceso()
                self.intercambiar_memorias(f"p{proceso.get_id()}")
                self.proceso_ejecutado = proceso.get_id()
                
                #Si el proceos tiene un tamanio de 0 quiere decir que ya finalizo
                if proceso.get_tamanio()==0:
                    print(f"Proceso {proceso.get_id()} terminado")
                    self.cambiar_estado("terminado",proceso)
                    self.memoria_principal.set_liberar_paginas(f"p{proceso.get_id()}")
                    self.memoria_virtual.set_liberar_paginas(f"p{proceso.get_id()}")
                    self.print_memorias()
                    
                #print(proceso.get_estado())
                print()
                # Despyues de que se ejecute el proceso se deben liberar los recursos
                
                #Si el proceos no termino vuelve a la cola de listo
                if proceso.get_estado() != "terminado":
                    self.cambiar_estado("listo",proceso)

                    #Si el proceso no ha terminado,lo volvemos a agregar a la lista de recursos
                    for recurso in recursos_necesarios:
                        #Si el recurso tiene preminencia si agrega de primeras a la lista de recursos que necesite
                        if recurso.get_nombre() == "CPU":
                            if proceso not in self.cola_cpu:
                                if proceso.get_preminencia():
                                    self.cola_cpu.insert(0,proceso)
                                else:
                                    self.cola_cpu.append(proceso)
                                    
                        elif recurso.get_nombre() == "Memoria RAM":
                            if proceso not in self.cola_memoria:
                                if proceso.get_preminencia():
                                    self.cola_memoria.insert(0,proceso)
                                else:
                                    self.cola_memoria.append(proceso)
                                    
                        elif recurso.get_nombre() == "Disco Duro":
                            if proceso not in self.cola_disco:
                                if proceso.get_preminencia():
                                    self.cola_disco.insert(0,proceso)
                                else:
                                    self.cola_disco.append(proceso)
                                    
                        elif recurso.get_nombre() == "Impresora":
                            if proceso not in self.cola_impresora:
                                if proceso.get_preminencia():
                                    self.cola_impresora.insert(0,proceso)
                                else:
                                    self.cola_impresora.append(proceso)
            else:
                # Si no están todos los recursos, el proceso regresa a 'listo'
                print(f"Proceso {proceso.get_id()} no tiene todos los recursos disponibles. Pasa a la cola 'bloqueado'.")
                if proceso not in self.cola_bloqueado:
                    self.cambiar_estado("bloqueado",proceso)
                
        self.mostrar_procesos()
        print()
        self.mostar_colas_estados()
        print()
        self.print_memorias()
        
    
    def cambiar_estado(self,nuevo_estado:str,proceso:Procesos):
        if nuevo_estado in BCP.estados_procesos:
            estado_anterior=proceso.get_estado()
            
            # Al cambiar de estado tenemos que quitar el proceso de la cola de procesos del estado que tenia,primero verificamos que si 
            # este en la cola del estado anterior y añadirla a la cola del nuevo estado
            
            # Realizamos el cambio de estado,pero para hacer este cambio verificamos que este si se pueda hacer teniendo en cuenta la grafica que esta en el reademe
            if nuevo_estado == "listo" and (estado_anterior=="nuevo" or estado_anterior=="ejecucion" or estado_anterior=="bloqueado"):
                if proceso not in self.cola_listo:
                    if proceso.get_preminencia():
                        # ultima psocion de la cola
                        indice_insercion = 0
                        for proceso_n in self.cola_listo:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_listo.insert(indice_insercion,proceso)
                    else:
                        self.cola_listo.append(proceso)
                        
            elif nuevo_estado == "bloqueado" and estado_anterior=="ejecucion":
                if proceso not in self.cola_bloqueado:
                    if proceso.get_preminencia():
                        indice_insercion = 0
                        for proceso_n in self.cola_bloqueado:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_bloqueado.insert(indice_insercion,proceso)
                    else:
                        self.cola_bloqueado.append(proceso)
                        
            elif nuevo_estado == "ejecucion" and estado_anterior == "listo":
                if proceso not in self.cola_ejecucion:
                    if proceso.get_preminencia():
                        indice_insercion = 0
                        for proceso_n in self.cola_ejecucion:  
                            if not proceso_n.get_preminencia():
                                break
                            indice_insercion += 1
                        self.cola_ejecucion.insert(indice_insercion,proceso)
                    else:
                        self.cola_ejecucion.append(proceso)
                    
            elif nuevo_estado == "terminado" and estado_anterior == "ejecucion":
                if proceso not in self.cola_terminado:
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
                    
    def intercambiar_memorias(self,proceso:str):
        # Obtenemos las matrices de memoria
        memoria_principal = self.memoria_principal.get_matriz_memoria()
        memoria_virtual = self.memoria_virtual.get_matriz_memoria()
        
        # Debemos encontrar el primer elemento en las matrices que sea difernte a O y en la matriz de memoria principal
        # tambien debemos descartar al indice cuyo elemento sea SO
        indice_principal = None
        indice_virtual = None

        for i in range (len(memoria_principal)):
            if memoria_principal[i] != 'O' and memoria_principal[i] != 'SO' and memoria_principal[i].startswith(proceso):
                indice_principal = i
                break
            
        for i in range (len(memoria_virtual)):
            if memoria_virtual[i] != 'O' and memoria_virtual[i].startswith(proceso):
                indice_virtual = i
                break
                
        if indice_principal is not None and indice_virtual is not None:
            # Accedemos a los valores que vamos a intercambiar (a,b =b,a)
            # Desempaquetado multiple
            memoria_principal[indice_principal], memoria_virtual[indice_virtual] = (
            memoria_virtual[indice_virtual],
            memoria_principal[indice_principal],
        )
            
         # Guardar las matrices actualizadas en las clases de memoria
        self.memoria_principal.set_matriz(memoria_principal)
        self.memoria_virtual.set_matriz(memoria_virtual)
        
        self.print_memorias()
    
    def print_memorias(self):
            print("Memoria principal")
            print(self.memoria_principal.get_matriz_memoria())
            print("Memoria virtual")
            print(self.memoria_virtual.get_matriz_memoria())