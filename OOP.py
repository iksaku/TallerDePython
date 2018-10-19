class Persona:
    def __init__(self, nombre: str, edad: int, correo=None):
        self._name = nombre
        self._age = edad
        self._email = correo
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

    def setAge(self, age: int):
        self._age = age

    def getEmail(self):
        return self._email
    
    def setEmail(self, email: str):
        self._email = email
