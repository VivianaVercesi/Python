import threading    
import time


#creo la función contar
def count(thread_name,first_num,last_num,sleep_time): 
    num= first_num
    while num<=last_num:
        print(f"{thread_name}: {num}")
        num += 1
        time.sleep(sleep_time)


#creo los hilos
thread1 = threading.Thread(target=count,args=("thread 1",1,5,1))
thread2 = threading.Thread(target=count,args=("thread 2",6,10,2))

#inicio los hilos
thread1.start()
thread2.start()

#espero que los hilos terminen
thread1.join()
thread2.join()
print("Finalizado")