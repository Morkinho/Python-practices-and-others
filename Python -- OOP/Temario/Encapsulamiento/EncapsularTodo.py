class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos) -> None:   
        self.__nombre =  nombre
        self.__apellido = apellido
        self.__edad = edad

    @property     
    def nombre(self):    
        return self.__nombre                                         

    @nombre.setter  
    def nombre (self, nombre):   
        self.__nombre = nombre  

    @property
    def apellido (self):
        return self.__apellido

    @apellido.setter 
    def apellido (self, apellido):
        self.__apellido = apellido

    @property
    def edad (self):
        return self.__edad

    @edad.setter
    def edad (self, edad):
        self.__edad = edad 



    def mostrar_detalles(self):          
        print (f'Persona: {self.__nombre} {self.__apellido} {self.__edad}')   

    def __del__(self):
        print(f'Persona {self.__nombre} {self.__apellido}')


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', '28')
    print(persona1.nombre)               
    persona1.apellido = 'Mondongo'
    persona1.edad = 30
    persona1.mostrar_detalles()
