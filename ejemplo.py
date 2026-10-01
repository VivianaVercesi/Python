import threading
import time

#función que va a ejecutar cada hilo
def contar_numeros(nombre,contador):
    for i in range(1,6):
        time.sleep(1)
        print(f"{nombre} está contando: {contador + i}")

#creamos dos hilos
hilo1 = threading.Thread(target=contar_numeros, args=("Hilo1",0))
hilo2 = threading.Thread(target=contar_numeros, args=("Hilo2",5))

#iniciamos ambos hilos
hilo1.start()
hilo2.start()

#esperamos que ambos hilos terminen
hilo1.join()
hilo2.join()
print("¡Contador completo!")