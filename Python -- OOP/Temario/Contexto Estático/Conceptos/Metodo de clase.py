class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self): #Desde instancia podemos acceder a los metodos de clase y estatocps
        self.metodo_clase()      
        self.metodo_instancia()
        print(self.variable_clase)
        print(self.variables_instancia)

#Accede a las variables de clase directamente, sin pasar por la clase en si.
# "cls" es la referencia a la clase

MiClase.metodo_clase()

#Tambien podemos acceder al metodo clase desde un objeto

miObjet1 = MiClase('Varible Variable Instancia')
miObjet1.metodo_clase()
