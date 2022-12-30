from Persona import Persona

class Cuenta(Persona):
    def __init__(self, nombre, edad, DNI, cantidad=0, titular=None):
        super().__init__(nombre, edad, DNI)
        self.__cantidad = cantidad
        self._titular = titular
        self._titular = {self._nombre, self._edad, self._DNI}



####


    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad


    ###


    if titular != 0:
        def Mostrar_Cuenta(self):

            return f' Datos de la cuenta' \
                    f' -- {self._titular}' \
                    f' -- Dinero en Cuenta: {self.__cantidad}' \


    if titular == None:
        def NoDatos(self):
            if self.titular == None:
                print('No hay una cuenta')


####



persona1C = Cuenta('Daniel', 28, '15.151.154' , 0)

print(persona1C.Mostrar_Cuenta())