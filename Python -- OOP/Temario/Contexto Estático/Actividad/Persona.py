class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad) -> None:
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad 

    def __str__(self) -> str:
        return f'Persona [{self.id_persona}, {self.nombre}, {self.edad}]'

persona1 = Persona('Juan', 28)
print(persona1)

Persona2 = Persona('Daniel, Bilbao', 25)
print(Persona2)

persona3 = Persona('Jose', 30)
print(persona3)

print(f'Valor contado personas: {Persona.contador_personas}')

