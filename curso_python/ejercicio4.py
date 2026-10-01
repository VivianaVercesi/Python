"""Nuestro cliente nos pide que el programa ahora haga lo siguiente:
● Formatee correctamente los textos ingresados en “apellido”
y “nombre”, convirtiendo la primera letra de cada palabra a
mayúsculas y el resto en minúsculas.
● Asegurarse que el correo electrónico no tenga espacios y
contenga solo una “@”.
● Que clasifique a sus clientes por rango etario basándose en
su edad (“Niño/a” para los y las menores de 15 años,
“Adolescente” de 15 a 18 y “Adulto/a” para personas
mayores de 18 años.)
El programa debe mostrar el apellido, nombre y dirección de correo
con el formato pedido, y el texto correspondiente a su rango etario."""

nombre = input("Nombre: ").strip().title()
apellido = input("Apellido: ").strip().title()
edad = input("Edad: ").strip()
email = input("Email: ").strip()

if nombre=="" or apellido=="" or email=="" or edad=="" or edad=="":
        print("Error. Debe ingresar todos los datos")
elif not edad.isdigit():
        print("Error. La edad debe ser un número entero válido")
elif " " in email or email.count("@")!=1:
        print("Formato de email inválido (no debe contener espacios y sólo un @)")
else:
        edad_num = int(edad)
        if edad_num<15:
            rango_etario = "Niño"
        elif edad_num<19:
            rango_etario = "Adolescente"
        else: 
            rango_etario = "Adulto"
        
        print("\n--- Datos Procesados ---")
        print(f"Apellido y Nombre: {apellido}, {nombre}")
        print(f"Correo electrónico: {email}")
        print(f"Rango etario: {rango_etario}")
