"""Parte 1:
1. Crear una lista con los nombres de los y las clientes que
vamos a procesar. Recorrer la lista y mostrar el nombre de
cada cliente o clienta, junto con su posición en la lista (por
ejemplo, Cliente 1, Cliente 2, etc.).
2. Recorrer la lista con un for y mostrar el nombre de cada
cliente junto con su posición en la lista (por ejemplo: Cliente
1: Ana).
3. Si encuentras un nombre vacío, mostrar un mensaje de
alerta indicando que ese dato no es válido.
Parte 2 (optativa)
Además, como bonus, probá aplicar el método .capitalize() de Python, que sirve para
poner en mayúscula la primera letra de una palabra y en minúscula el resto."""

clientes = ["agostina adami", "josefina adami", "Florencia vercesi", "juana Molina", "clara Castelli", "José arguello", "Faustino vercesi", "martina DiMarsi","" ,"Fernando DeAngelis"]

for i in range(len(clientes)):
    
    if clientes[i] == "":
        print(f"Dato no válido para cliente {i+1}")
        continue
    print(f"Cliente {i + 1}: {clientes[i].title()}")    