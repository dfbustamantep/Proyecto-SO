from app.forms import CreateProcesForm
from flask import request,make_response,redirect,render_template,session,url_for,flash

from app import create_app

from BCP import BCP
from recurso import Recurso

    # Recursos
cpu = Recurso(1, "CPU")
memoria = Recurso(2, "Memoria RAM")
disco = Recurso(3, "Disco Duro")
impresora = Recurso(4, "Impresora")
    
# Lista de recursos 
recursos = [cpu,memoria,disco,impresora]

id_proceso=1

#variable para manejar el id del proceso autoincremental
app = create_app()

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_proceso',methods=["GET","POST"])
def crear_proceso():
    global id_proceso # Vamos a usar la variable global
    create_proces_form = CreateProcesForm()
    #id_proceso += 1
    # Pasamos la lista de recursos al contexto para mostrarla en la vista
    context = {
        "create_proces_form":create_proces_form,
        "recursos": recursos,
        "id_proceso":id_proceso
    }
    id_proceso += 1
    return render_template('crear_proceso.html',**context)

@app.route('/visualizar_procesos')
def visualizar_procesos():
    return render_template('visualizar_procesos.html')

@app.route('/visualizar_memoria')
def visualizar_memoria():
    return render_template('visualizar_memoria.html')

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