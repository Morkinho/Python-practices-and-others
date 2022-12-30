class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos) -> None:   
        self.__nombre =  nombre
        self.apellido = apellido
        self.edad = edad

    #Getter obtenemos los datos de la clase que están encapsulados
    @property      #Modifica el metodo, para acceder al mismo y lejos del encapsulamiento.
    def nombre(self):                                                #Utilizamos un nuevo 'nombre', con este mismo retornamos el valor de __nombre del objeto
        print('Llamando método Getter, con este vamos a poder traer __nombre')
        return self.__nombre                                          #Lo invocamos encapsulado

    #Setter nos permite modificar los valores

    @nombre.setter  #Con colocar el atributo y .setter podemos modificarlo.
    
    def nombre (self, nombre):   #Generamos una funcion editable
        print('Llamando Set, con este podemos editar el valor de __nombre')
        self.__nombre = nombre  

    def mostrar_detalles(self):          
        print (f'Persona: {self._nombre} {self.apellido} {self.edad}')   


persona1 = Persona('Juan', 'Perez', '28')
print(persona1.nombre)               
persona1.nombre = 'Juan Carlos'         # '.nombre' Hace que se pueda editar como una variable
print(persona1.nombre)


# "_" Se utiliza como nomenclatura en las clases para que no se editen los parametros fuera de los mismos.
# "__" Se utiliza para bloquear los parametros 