from OOP import Persona

nombre = None
edad = None
email = None

while nombre == None:
    try:
        nombre = str(input("Nombre: "))
    except ValueError:
        print("[Error] Nombre invalido.")

while edad == None:
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("[Error] Edad invalida")

persona = Persona(nombre, edad, email)
print("Se ha añadido a " + persona.getName() + ", tiene " + str(persona.getAge()) + " años")