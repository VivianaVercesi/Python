nombre = input("Nombre: ").strip()
apellido = input("Apellido: ").strip()
edad = input("Edad: ").strip()
email = input("Email: ").strip()

if (nombre=="" or apellido=="" or email=="" or edad=="" or int(edad)<18 ):
        print("Error")
else:
        print(nombre,apellido,edad,email, sep="\n")
