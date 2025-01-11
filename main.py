from app.forms import CreateProcesForm
from flask import request,make_response,redirect,render_template,session,url_for,flash

from app import create_app

from BCP import BCP,Procesos,Recurso,Memoria

# Lista donde se almacenan todos los procesos
procesos = BCP.procesos

# Colas de estados
cola_nuevo = BCP.cola_nuevo
cola_listo = BCP.cola_listo
cola_bloqueado = BCP.cola_bloqueado
cola_ejecucion = BCP.cola_ejecucion
cola_terminado = BCP.cola_terminado

# Lista de recursos
recursos = BCP.recursos

# Colas de recursos
cola_cpu = BCP.cola_cpu
cola_memoria = BCP.cola_memoria
cola_disco = BCP.cola_disco
cola_impresora = BCP.cola_impresora

    # tamaño memoria RAM(Principal)
tamanio_MP = BCP.tamanio_MP

    # tamaño memoria virtual (2 veces el tamaño de la memoria principal)
tamanio_MV = BCP.tamanio_MV 

    # tamaño del marco de pagina 4 unidades 
tamanio_marco = BCP.tamanio_marco
    
    #Porcentaje que se sube a cada memoria
porcentaje_MP = BCP.porcentaje_MP
porcentaje_MV = BCP.porcentaje_MV

    #Memorias
memoria_principal = BCP.memoria_principal 
memoria_virtual = BCP.memoria_virtual 

id_proceso=len(procesos)

#variable para manejar el id del proceso autoincremental
app = create_app()

@app.route('/crear_proceso',methods=["GET","POST"])
def crear_proceso():
    
    global id_proceso # Vamos a usar la variable global
    create_proces_form = CreateProcesForm()
    #id_proceso += 1
    
    #id_proceso = len(procesos)+1
    #if create_proces_form.validate_on_submit():
    # Pasamos la lista de recursos al contexto para mostrarla en la vista
    context = {
        "create_proces_form":create_proces_form,
        "recursos": recursos,
        "id_proceso":id_proceso
    }
    if create_proces_form.validate_on_submit():
        id_proceso = id_proceso
        tamanio = create_proces_form.tamanio.data
        recursos = create_proces_form.recursos.data
        hilos = create_proces_form.hilos.data
        preminencia = create_proces_form.preminencia.data
        
        Procesos(id_proceso,tamanio,hilos,recursos,preminencia)    
        flash("Proceso registrado correctamente")
        '''
        username = login_form.username.data
        session["username"]=username
        flash("Nombre de usuario registrado correctamente")
        '''
        
        return redirect(url_for("index"))
    
    return render_template('crear_proceso.html',**context)

@app.route('/visualizar_procesos')
def visualizar_procesos():
    return render_template('visualizar_procesos.html')

@app.route('/visualizar_memoria')
def visualizar_memoria():
    return render_template('visualizar_memoria.html')

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