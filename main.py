from app.forms import CreateProcesForm
from flask import request,make_response,redirect,render_template,session,url_for,flash

from app import create_app

from BCP import BCP,Procesos,Recurso,Memoria


BCP = BCP()
# Lista donde se almacenan todos los procesos
procesos = BCP.get_procesos()

# Colas de estados
cola_nuevo = BCP.get_cola_nuevo()
cola_listo = BCP.get_cola_listo()
cola_bloqueado = BCP.get_cola_bloqueado()
cola_ejecucion = BCP.get_cola_ejecucion()
cola_terminado = BCP.get_cola_terminado()

# Colas de recursos
cola_cpu = BCP.get_cola_cpu()
cola_memoria = BCP.get_cola_memoria()
cola_disco = BCP.get_cola_disco()
cola_impresora = BCP.get_cola_impresora()

    # tamaño memoria RAM(Principal)
tamanio_MP = BCP.get_tamanio_MP()

    # tamaño memoria virtual (2 veces el tamaño de la memoria principal)
tamanio_MV = BCP.get_tamanio_MV() 

    # tamaño del marco de pagina 4 unidades 
tamanio_marco = BCP.get_tamanio_marco()
    
    #Porcentaje que se sube a cada memoria
porcentaje_MP = BCP.get_porcentaje_MP()
porcentaje_MV = BCP.get_porcentaje_MV()

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
    create_proces_form = CreateProcesForm()
    #id_proceso += 1
    recursos = BCP.get_lista_recursos()
     # Asigna los recursos al campo 'choices' del formulario
    create_proces_form.recursos.choices = [(recurso.get_id_recurso(), recurso.get_nombre()) for recurso in recursos]
    
    id_proceso = get_ultimo_id()
    #if create_proces_form.validate_on_submit():
    # Pasamos la lista de recursos al contexto para mostrarla en la vista
    context = {
        "create_proces_form":create_proces_form,
        "recursos": recursos,
        "id_proceso":id_proceso
    }
    if create_proces_form.validate_on_submit():
        # Datos del formulario
        tamanio = create_proces_form.tamanio.data
        recursos_seleccionados = create_proces_form.recursos.data  # IDs seleccionados
        hilos = create_proces_form.hilos.data
        preminencia = create_proces_form.preminencia.data
        
          # Mapear los IDs a objetos de recursos
        recursos_seleccionados = [r for r in recursos if str(r.get_id_recurso()) in recursos_seleccionados]
        # Creacion proceso
        proceso = Procesos(id_proceso,tamanio,hilos,recursos_seleccionados,preminencia)  
        # Agregar procesos a lista de procesos,cola de nuevo y cola de los recursos respectivos
        lista_procesos = BCP.get_procesos()
        lista_procesos.append(proceso)
        BCP.set_procesos(lista_procesos)
        cola_nuevo= BCP.get_cola_nuevo()
        cola_nuevo.append(proceso)
        BCP.set_cola_nuevo(cola_nuevo)
        
        cola_cpu = BCP.get_cola_cpu()
        cola_memoria = BCP.get_cola_memoria()
        cola_disco = BCP.get_cola_disco()
        cola_impresora = BCP.get_cola_impresora()
        
        for rec in recursos_seleccionados:
            if rec.get_nombre() == "CPU":
                cola_cpu.append(proceso)
                BCP.set_cola_cpu(cola_cpu)
            elif rec.get_nombre() == "Memoria RAM":
                cola_memoria.append(proceso)
                BCP.set_cola_memoria(cola_memoria)
            elif rec.get_nombre() == "Disco Duro":
                cola_disco.append(proceso)
                BCP.set_cola_disco(cola_disco)
            elif rec.get_nombre() == "Impresora":
                cola_impresora.append(proceso)
                BCP.set_cola_impresora(cola_impresora)
                                       
        flash("Proceso registrado correctamente")
        return redirect(url_for("index"))
    
    return render_template('crear_proceso.html',**context)

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
    
    print(cola_nuevo)
    print(cola_listo)
    print(cola_bloqueado)
    print(cola_ejecucion)
    print(cola_terminado)
    
    context={
        "cola_nuevo":cola_nuevo,
        "cola_listo":cola_listo,
        "cola_bloqueado":cola_bloqueado,
        "cola_ejecucion":cola_ejecucion,
        "cola_terminado":cola_terminado
    }
    
    return render_template('visualizar_estados.html',**context)

@app.route('/visualizar_recursos')
def visualizar_recursos():
    # Colas de recursos
    cola_cpu = BCP.get_cola_cpu()
    cola_memoria = BCP.get_cola_memoria()
    cola_disco = BCP.get_cola_disco()
    cola_impresora = BCP.get_cola_impresora()
    
    print(cola_cpu)
    print(cola_memoria)
    print(cola_disco)
    print(cola_impresora)
    
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
    porcentaje_MV = BCP.get_porcentaje_MV()
    memoria_principal = BCP.get_memoria_principal()
    memoria_virtual = BCP.get_memoria_virtual()

    
    context={
        "tamanio_MP":tamanio_MP,
        "tamanio_MV":tamanio_MV,
        "tamanio_marco":tamanio_marco,
        "porcentaje_MP":porcentaje_MP,
        "porcentaje_MV":porcentaje_MV,
        "memoria_principal":memoria_principal,
        "memoria_virtual":memoria_virtual
    }
    
    return render_template('visualizar_memoria.html',**context)

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)

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