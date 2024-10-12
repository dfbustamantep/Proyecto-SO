from BCP import BCP

def printLines():
    print("----------------------------------------------------------------------")
    
printLines()
print("\tSimulador funcionamiento de un Sistema Operativo")
printLines()

bcp = BCP()

print("Crear procesos")
bcp.creacion_procesos()

print("Mostrar procesos")
bcp.mostrar_procesos()
#bcp.mostar_colas_estados()
print("Ejecucion")
bcp.ejecutar()

print("Cola de estados")
bcp.mostar_colas_estados()