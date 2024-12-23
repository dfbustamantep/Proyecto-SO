from BCP import BCP
from memoria import Memoria
def printLines():
    print("----------------------------------------------------------------------")

# El tamanio de las memorias siempore deberia ser una potencia de 2
# tamaño memoria RAM(Principal)
tamanio_MP = 1024
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

printLines()
print("\tSimulador funcionamiento de un Sistema Operativo")
printLines()

bcp = BCP()

#print("Crear procesos")
bcp.creacion_procesos()

#print("Mostrar procesos")
bcp.mostrar_procesos()
#bcp.mostar_colas_estados()

ejecutar = input("Desea ejecutar?(s/n): ")
print()

if(ejecutar=='s' or ejecutar=='S'):
    print("Ejecucion")
    bcp.ejecutar()
    #print("Colas de estados")
    #bcp.mostar_colas_estados()



