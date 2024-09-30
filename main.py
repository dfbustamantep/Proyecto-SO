from BCP import BCP

def printLines():
    print("----------------------------------------------------------------------")
    
printLines()
print("\tSimulador funcionamiento de un sistema operativo")
printLines()

bcp = BCP()

bcp.creacion_procesos()
bcp.mostrar_procesos()
