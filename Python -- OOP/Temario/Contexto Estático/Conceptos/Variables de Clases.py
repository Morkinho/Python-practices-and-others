# Las variables de clases son variables que se asosian con la clase u se comparte entre los objetos.
# Se crea fuera del metodo init

class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

print(MiClase.variable_clase)             #Se puede acceder a la variable de clase sin un objeto, desde la clase

ClaseObjeto = MiClase('Valor variable instancia')   #Creamos un objeto para acceder a la variable desde instancia
print (ClaseObjeto.variables_instancia)           #Accedemos
print(ClaseObjeto.variable_clase)                #Tambien podemos acceder a la variable clase desde el objeto

MiClase.variable_clase2 = 'Valor variable clase 2'  #Podemos generar este tipo de valores al vuelo

ClaseObjeto2 = MiClase('Otro Valor de Variable Instancia')
print(ClaseObjeto2.variables_instancia)
print(ClaseObjeto2.variable_clase)

print(MiClase.variable_clase2)               #Cuando generamos al vuelo podemos accederla en cualquier objeto
print(ClaseObjeto2.variable_clase2)                #O a la clase
