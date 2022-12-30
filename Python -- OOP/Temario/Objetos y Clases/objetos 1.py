class Persona:
    def __init__(self,nombre, apellido,edad) -> None:
        self.nombre =  nombre
        self.apellido = apellido
        self.edad = edad
        

persona1 = Persona('Juan', 'Perez', '28')
persona2 = Persona('Monica', 'Campodonico', '22')

print(persona1.nombre,',', persona1.apellido,',', persona1.edad)
persona1.nombre = 'Juan Carlos'   #Modificamos los valores de los objetos de esta manera
persona1.apellido = 'Juarez'
persona1.edad = 25 
print('Agregamos datos a persona 1: ')
print(persona1.nombre,',', persona1.apellido,',', persona1.edad)

print(persona2.nombre,',', persona2.apellido,',', persona2.edad)
persona2.nombre = 'Monica Ailen'
persona2.apellido = 'Campodonico Bechara'
persona2.edad = 21 
print('Agregamos datos a persona 2: ')
print(persona2.nombre,',', persona2.apellido,',', persona2.edad)
