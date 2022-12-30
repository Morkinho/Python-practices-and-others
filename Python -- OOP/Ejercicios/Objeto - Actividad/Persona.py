class Persona:
    def __init__(self, nombre, edad, DNI):
        self._nombre = nombre
        self._DNI = DNI
        if 18<edad<100:
            self._edad = edad
            print('El usuario es valido para recibir una cuenta')
        else:
            print('El usuario no es valido para recibir una cuenta')
            self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad


    @property
    def DNI(self):
        return self._DNI
    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI

##########

    def Mostrar_Datos(self):
        return f'Nombre y Apellido: {self._nombre}' \
               f' -- Edad: {self._edad}' \
               f' -- Documento Nacional de Identidad: {self._DNI}'

       
    def Mayor_Edad (self):
        if self.edad < 18:
            print('El usuario es menor de edad')
        else:
            print('El usuario es mayor de edad')

persona1 = Persona('Jose, Hernandez', 48, '14.565.758')


print(f'{persona1.Mostrar_Datos()},{persona1.Mayor_Edad()}')