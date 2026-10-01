import threading
import time

thread_counter = 0
add1 = 0
add2 = 0
condicion = threading.Condition() #Permite sincronizar los hilos para que solo impriman los resultados cuando ambos hayan terminado.

#función sumar
def add_num(threat_name,first_num,last_num):
    global add1, add2, thread_counter

    add_local = 0
    for i in range(first_num, last_num + 1):
        add_local += i

    with condicion:
        if threat_name == "thread 1":
            add1 = add_local
        else:
            add2 = add_local
        thread_counter += 1
        if thread_counter == 2:
            condicion.notify_all()
        else:
            condicion.wait()

#creo los hilos
thread1 = threading.Thread(target=add_num,args=("thread 1",1,5))
thread2 = threading.Thread(target=add_num,args=("thread 2",1,5))

#inicio los hilos
thread1.start()
thread2.start()

#espero a que terminen los hilos
thread1.join()
thread2.join()

with condicion:
    print(f"Suma del hilo 1: {add1}")
    print(f"Suma del hilo 2: {add2}")
    print(f"Suma total: {add1 + add2}")
