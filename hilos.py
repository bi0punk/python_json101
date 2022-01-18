import time
import threading

def ejecucion_horaria(segundos):
    """
    Este es un thread con parametros.
    
    @param segundos: Ejecuta un print cada tantos segundos. 
    """
    print("Thread ejecuta cada %d" % segundos)
    print(segundos)
    for i in range(10):
        print("Ejecucion horaria, pasada %d" % i)
        time.sleep(segundos)

# Aqui creamos el thread.
# El primer argumento es el nombre de la funcion que contiene el codigo.
# El segundo argumento es una lista de argumentos para esa funcion .
# Ojo con la coma al final!

hilo = threading.Thread(target=ejecucion_horaria, args=(2,))
hilo.start()   # Iniciamos la ejecución del thread,

# La ejecución sigue de inmediato aqui, mientras el thread 
# ejecuta en paralelo. 
for i in range(100):
    print("Ejecución principal, pasada %d" % i)
    time.sleep(1)

