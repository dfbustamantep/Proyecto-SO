from BCP import BCP

def printLines():
    print("----------------------------------------------------------------------")

# tamaño del marco 5 unidades
tamanio_marco = 5 


printLines()
print("\tSimulador funcionamiento de un Sistema Operativo")
printLines()

bcp = BCP()

print("Crear procesos")
bcp.creacion_procesos()

print("Mostrar procesos")
bcp.mostrar_procesos()
#bcp.mostar_colas_estados()

ejecutar = input("Desea ejecutar?(s/n): ")
print()

if(ejecutar=='s' or ejecutar=='S'):
    print("Ejecucion")
    bcp.ejecutar()
    #print("Colas de estados")
    #bcp.mostar_colas_estados()



