"""1. Solicite al usuario o usuaria los nombres de los clientes y clientas uno por uno y
valide que cada nombre no esté vacío. Si se deja el campo vacío, mostrale un
mensaje de advertencia y volvé a pedir el nombre.
2. Guarde cada nombre válido en una lista, asegurándote de agregarlo con el
método .append().
3. Permita que la persona finalice la carga de nombres escribiendo la palabra "fin".
4. Una vez finalizada la carga, ordene alfabéticamente los nombres en la lista y
muestre la lista ordenada de nombres utilizando un bucle for."""

clientes = []

print("Ingrese el nombre de un cliente o  fin para finalizar")

while True:
    cliente = input("Ingrese el nombre del cliente: ")
    if cliente.strip().lower() == "fin":
        break 
    if cliente == "":
        print("El nombre no puede estar vacío. Intente nuevamente.")
    clientes.append(cliente)

clientes.sort()

print("\n--- Lista de Clientes Ordenada ---")
for cliente in clientes:        
    print(f"- {cliente}")