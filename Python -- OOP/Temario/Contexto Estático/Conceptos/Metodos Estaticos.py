class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print (MiClase.variable_clase)

# Metodo Estatico trabaja con la clase en si y no con los objetos
# No puede acceder a las instancias, no posee self.
# Puede acceder a la variable de clase desde la clase.

MiClase.metodo_estatico()