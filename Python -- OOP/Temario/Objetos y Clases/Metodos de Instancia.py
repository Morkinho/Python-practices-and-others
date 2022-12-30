class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos) -> None:        # * genera una tupla variable //// ** genera diccionarios variables.
        self.nombre =  nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalles(self):             #Generamos un comportamiento que resume acciones de imprimir uno a uno los detalles, se crea igual que una clase, solamente que se le genera un nombre y un (self)
        print (f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')     #Otorgamos comportamiento


persona1 = Persona('Juan', 'Perez', '28', '1122334455', '1121', ocupacion='contador') 
persona1.mostrar_detalles()
   

persona2 = Persona('Monica', 'Campodonico', '22')
persona2.mostrar_detalles()


