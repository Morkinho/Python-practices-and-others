class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos) -> None:   
        self.__nombre =  nombre
        self.apellido = apellido
        self.edad = edad

    @property     
    def nombre(self):                                               
        return self.__nombre                                        

 #   @nombre.setter 
    
 #   def nombre (self, nombre):   
 #       self.__nombre = nombre  

    def mostrar_detalles(self):          
        print (f'Persona: {self._nombre} {self.apellido} {self.edad}')   


persona1 = Persona('Juan', 'Perez', '28')           
persona1.nombre = 'Juan Carlos'       #Se puede acceder agregando un '_' al 'nombre' pero, esto no se hace 
print(persona1._nombre)

