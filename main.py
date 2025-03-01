import math
from app.forms import CreateProcesForm
from flask import request,make_response,redirect,render_template,session,url_for,flash

from app import create_app

from BCP import BCP,Procesos,Recurso,Memoria


BCP = BCP()

    # tamaño memoria RAM(Principal)
tamanio_MP = BCP.get_tamanio_MP()

    # tamaño memoria virtual (2 veces el tamaño de la memoria principal)
tamanio_MV = BCP.get_tamanio_MV() 

    # tamaño del marco de pagina 4 unidades 
tamanio_marco = BCP.get_tamanio_marco()
    
    #Porcentaje que se sube a cada memoria
porcentaje_MP = BCP.get_porcentaje_MP()


    #Memorias
memoria_principal = BCP.get_memoria_principal() 
memoria_virtual = BCP.get_memoria_virtual() 

#variable para manejar el id del proceso autoincremental
app = create_app()

def get_ultimo_id():
    lista_procesos = BCP.get_procesos()
    if lista_procesos:
        # Si la lista no está vacía, obtenemos el último elemento y su ID
        ultimo_proceso = lista_procesos[-1]
        return ultimo_proceso.get_id()+1
    else:
        return 1
    
@app.route('/crear_proceso',methods=["GET","POST"])
def crear_proceso():
    cola_nuevo = BCP.get_cola_nuevo()
    
    create_proces_form = CreateProcesForm()
    #id_proceso += 1
    recursos = BCP.get_lista_recursos()
     # Asigna los recursos al campo 'choices' del formulario
    create_proces_form.recursos.choices = [(recurso.get_id_recurso(), recurso.get_nombre()) for recurso in recursos]
    id_proceso = get_ultimo_id()
    memoria_principal_disponible = BCP.get_memoria_principal().get_paginas_dipsonibles() * BCP.get_tamanio_marco()
    memoria_virtual_disponible = BCP.get_memoria_virtual().get_paginas_dipsonibles() * BCP.get_tamanio_marco()

    #if create_proces_form.validate_on_submit():
    # Pasamos la lista de recursos al contexto para mostrarla en la vista
    context = {
        "create_proces_form":create_proces_form,
        "recursos": recursos,
        "id_proceso":id_proceso,
        "memoria_principal_disponible":memoria_principal_disponible,
        "memoria_virtual_disponible":memoria_virtual_disponible
    }
    if create_proces_form.validate_on_submit():
        # Datos del formulario
        tamanio = int(create_proces_form.tamanio.data)
        print(f"Tamanio proceso {id_proceso} :{tamanio}")
         # Math.ceil se usa para aproximar al siguiente entero en caso de que la division no se exacta 
        paginas_proceso = math.ceil(tamanio/BCP.get_tamanio_marco())
        #paginas_memoria_principal=math.ceil(paginas_proceso*BCP.get_porcentaje_MP())
        paginas_memoria_principal=BCP.get_porcentaje_MP()
        paginas_memoria_virtual=paginas_proceso-paginas_memoria_principal
        
        print(f"Paginas proceso {id_proceso} :{paginas_proceso}\npaginas memoria principal:{paginas_memoria_principal}\npaginas memoria virtual:{paginas_memoria_virtual}")
        memoria_principal = BCP.get_memoria_principal()
        memoria_virtual = BCP.get_memoria_virtual()
        
         # Validación de memoria disponible
         #and \ me permite poner el resto de codigo abajo
        if memoria_principal.get_paginas_dipsonibles() < paginas_memoria_principal and \
            memoria_virtual.get_paginas_dipsonibles() < paginas_memoria_virtual:
            flash("No hay suficiente memoria disponible para crear el proceso.", "danger")
            return redirect(url_for("crear_proceso"))

        # Operaciones de asignación de memoria
        if memoria_principal.get_paginas_dipsonibles() >= paginas_memoria_principal:
            ultimo_id = memoria_principal.set_paginas_ocuapadas(paginas_memoria_principal, f"p{id_proceso}",
                                                                BCP.get_tamanio_marco(), 0)
            memoria_virtual.set_paginas_ocuapadas(paginas_memoria_virtual, f"p{id_proceso}", BCP.get_tamanio_marco(),
                                                  ultimo_id)
        else:
            memoria_virtual.set_paginas_ocuapadas(paginas_proceso, f"p{id_proceso}", BCP.get_tamanio_marco())
        
        recursos_seleccionados = create_proces_form.recursos.data  #IDs seleccionados
        # Mapear los IDs a objetos de recursos
        recursos_seleccionados = [r for r in recursos if str(r.get_id_recurso()) in recursos_seleccionados]
        print("Recursos")
        for recurso in recursos_seleccionados:
            print(recurso.get_nombre())
        
        hilos = calcular_hilos(tamanio)
        print(f"El proceso va a tener {hilos}")
        preminencia = create_proces_form.preminencia.data
        if preminencia.lower()  == 'si':
            preminencia = True
        else:
            preminencia = False
        print(f"Preminencia {preminencia}")
        
        # Creacion proceso
        proceso = Procesos(id_proceso,tamanio,hilos,recursos_seleccionados,preminencia,paginas_proceso,paginas_memoria_principal,paginas_memoria_virtual)  
        # Agregar procesos a lista de procesos,cola de nuevo y cola de los recursos respectivos
        lista_procesos = BCP.get_procesos()
        lista_procesos.append(proceso)
        BCP.set_procesos(lista_procesos)
        # Si tiene preminencia lo agregamos de primeras 
        if preminencia:
            # ultima psocion de la cola de nuevos
            indice_insercion = 0
            for proceso_n in cola_nuevo:  
            # proceso es el elemento actual de la cola
                if not proceso_n.get_preminencia():
                    break
                indice_insercion += 1
                
            print(proceso.get_id())
            cola_nuevo.insert(indice_insercion,proceso)
        else:
            cola_nuevo.append(proceso)    
        BCP.set_cola_nuevo(cola_nuevo)

        cola_cpu = BCP.get_cola_cpu()
        cola_memoria = BCP.get_cola_memoria()
        cola_disco = BCP.get_cola_disco()
        cola_impresora = BCP.get_cola_impresora()
            
        for rec in recursos_seleccionados:
            if rec.get_nombre() == "CPU" and proceso not in cola_cpu:
                if preminencia:
                    # ultima psocion de la cola
                    indice_insercion = 0
                    for proceso_n in cola_cpu:  
                    # proceso es el elemento actual de la cola
                        if not proceso_n.get_preminencia():
                            break
                        indice_insercion += 1
                    print(proceso.get_id())
                    cola_cpu.insert(indice_insercion,proceso)
                else:
                    cola_cpu.append(proceso)   
                BCP.set_cola_cpu(cola_cpu)
                print(f"Proceso agregado a cola de cpu")
                
            elif rec.get_nombre() == "Memoria RAM" and proceso not in cola_memoria:
                if preminencia:
                    # ultima psocion de la cola
                    indice_insercion = 0
                    for proceso_n in cola_memoria:  
                    # proceso es el elemento actual de la cola
                        if not proceso_n.get_preminencia():
                            break
                        indice_insercion += 1
                    print(proceso.get_id())
                    cola_memoria.insert(indice_insercion,proceso)
                else:
                    cola_memoria.append(proceso)
                BCP.set_cola_memoria(cola_memoria)
                print(f"Procesos agregado a cola de memoria")
                
            elif rec.get_nombre() == "Disco Duro" and proceso not in cola_disco:
                if preminencia:
                    # ultima psocion de la cola
                    indice_insercion = 0
                    for proceso_n in cola_disco:  
                    # proceso es el elemento actual de la cola
                        if not proceso_n.get_preminencia():
                            break
                        indice_insercion += 1
                    print(proceso.get_id())
                    cola_disco.insert(indice_insercion,proceso)
                else:
                    cola_disco.append(proceso)
                BCP.set_cola_disco(cola_disco)
                print(f"Procesos agregado a cola de disco")
            elif rec.get_nombre() == "Impresora" and proceso not in cola_impresora:
                if preminencia:
                    # ultima psocion de la cola
                    indice_insercion = 0
                    for proceso_n in cola_impresora:  
                    # proceso es el elemento actual de la cola
                        if not proceso_n.get_preminencia():
                            break
                        indice_insercion += 1
                    print(proceso.get_id())
                    cola_impresora.insert(indice_insercion,proceso)
                else:
                    cola_impresora.append(proceso)
                BCP.set_cola_impresora(cola_impresora)
                print(f"Procesos agregado a cola de impresora")
                           
        flash("Proceso registrado correctamente")
        return redirect(url_for("index"))
    
    return render_template('crear_proceso.html',**context)


def calcular_hilos(tamanio: int):
    if tamanio <= 20:
        return 1
    elif tamanio <= 40:
        return 2
    elif tamanio <= 60:
        return 3
    elif tamanio <= 80:
        return 4
    else:
        return 5
    
@app.route('/visualizar_procesos')
def visualizar_procesos():
    # Lista de proceos
    procesos = BCP.get_procesos()
    
    context={
        "procesos":procesos,
    }
    
    return render_template('visualizar_procesos.html',**context)


@app.route('/visualizar_estados')
def visualizar_estados():
    # Colas de estados
    cola_nuevo = BCP.get_cola_nuevo()
    cola_listo = BCP.get_cola_listo()
    cola_bloqueado = BCP.get_cola_bloqueado()
    cola_ejecucion = BCP.get_cola_ejecucion()
    cola_terminado = BCP.get_cola_terminado()
    procesadores = BCP.get_procesadores()
    print(f"Cola de nuevos:")
    for proceso in cola_nuevo:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
        
    print(f"Cola de listos: ")
    for proceso in cola_listo:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
        
    print(f"Cola de bloqueados: ")
    for proceso in cola_bloqueado:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
        
    print(f"Cola de ejecucion: ")
    for i, cola in enumerate(cola_ejecucion):
        print(f"\tProcesador {i+1}:")
        for proceso in cola:
            print(f"\tID proceso: {proceso.get_id()}") 
    
    for i in range (procesadores):
        for proceso in cola_ejecucion[i]:
            print(f"\tID proceso: {proceso.get_id()}")
        
        
    print(f"Cola de terminado:")
    for proceso in cola_terminado:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
    
    context={
        "cola_nuevo":cola_nuevo,
        "cola_listo":cola_listo,
        "cola_bloqueado":cola_bloqueado,
        "cola_ejecucion":cola_ejecucion,
        "cola_terminado":cola_terminado,
        "procesadores":procesadores
    }
    
    return render_template('visualizar_estados.html',**context)

@app.route('/visualizar_recursos')
def visualizar_recursos():
    # Colas de recursos
    cola_cpu = BCP.get_cola_cpu()
    cola_memoria = BCP.get_cola_memoria()
    cola_disco = BCP.get_cola_disco()
    cola_impresora = BCP.get_cola_impresora()
    
    
    print(f"Cola de cpu:")
    for proceso in cola_cpu:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
        
    print(f"Cola de memoria: ")
    for proceso in cola_memoria:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
        
    print(f"Cola de disco: ")
    for proceso in cola_disco:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
    
    print(f"Cola de impresora:")
    for proceso in cola_impresora:
        print(f"Proceso ID: {proceso.get_id()}, Tamaño: {proceso.get_tamanio()}")
    
    context={
        "cola_cpu":cola_cpu,
        "cola_memoria":cola_memoria,
        "cola_disco":cola_disco,
        "cola_impresora":cola_impresora
    }
    
    return render_template('visualizar_recursos.html',**context)

@app.route('/visualizar_memoria')
def visualizar_memoria():
    tamanio_MP = BCP.get_tamanio_MP()
    tamanio_MV = BCP.get_tamanio_MV()
    tamanio_marco = BCP.get_tamanio_marco()
    porcentaje_MP = BCP.get_porcentaje_MP()
    #porcentaje_MV = BCP.get_porcentaje_MV()
    memoria_principal = BCP.get_memoria_principal()
    memoria_virtual = BCP.get_memoria_virtual()

    
    context={
        "tamanio_MP":tamanio_MP,
        "tamanio_MV":tamanio_MV,
        "tamanio_marco":tamanio_marco,
        "porcentaje_MP":porcentaje_MP,
        #"porcentaje_MV":porcentaje_MV,
        "memoria_principal":memoria_principal,
        "memoria_virtual":memoria_virtual
    }
    
    return render_template('visualizar_memoria.html',**context)

@app.route('/ejecutar_procesos',methods=['POST'])
def ejecutar_procesos():
    BCP.ejecutar()
    proceso_id = BCP.get_proceso_ejecutado()
    if proceso_id != 0:
        flash(f"Se ejecutó el proceso {proceso_id}", "success")
    else:
        flash("No se pudo ejecutar ningún proceso", "warning")
    return redirect(url_for("visualizar_procesos"))

'''@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)'''
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #desde cualquier direccion
    app.run(host='0.0.0.0',port=81,debug=True)
'''

def printLines():
    print("----------------------------------------------------------------------")


printLines()
print("\tSimulador funcionamiento de un Sistema Operativo")
printLines()

bcp = BCP()

bcp.creacion_procesos()

bcp.mostrar_procesos()

ejecutar = input("Desea ejecutar?(s/n): ")
print()

if(ejecutar=='s' or ejecutar=='S'):
    print("Ejecucion")
    bcp.ejecutar()
    '''