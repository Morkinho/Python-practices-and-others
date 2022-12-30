from xml.sax.handler import property_dom_node


class Persona:
    def __init__ (self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property     
    def nombre(self):    
        return self._nombre                                         
    @nombre.setter  
    def nombre (self, nombre):   
        self._nombre = nombre  

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido (self, apellido):
        self._apellido = apellido

    @property
    def edad (self):
        return self._edad
    @edad.setter
    def edad (self, edad):
        self._edad = edad

    def __str__(self):
        return f'Persona: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}'

class Empleado (Persona):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__() } Sueldo: {self.sueldo}'

empleado1 = Empleado('Gabriel', 'Gonzalez', 28, 5000)
print(empleado1.nombre)
print(empleado1.apellido)
print(empleado1.edad)
print(empleado1.sueldo)