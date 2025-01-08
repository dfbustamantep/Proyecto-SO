from BCP import BCP
from app.forms import CreateProcesForm
from memoria import Memoria
from flask import request,make_response,redirect,render_template,session,url_for,flash

from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_proceso')
def crear_proceso():
    form = CreateProcesForm()
    return render_template('crear_proceso.html',form=form)

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