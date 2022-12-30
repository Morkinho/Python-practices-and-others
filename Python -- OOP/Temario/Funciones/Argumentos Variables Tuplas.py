def listar_nombres(*nombres):                  # Se le agrega * Cuando no se conoce la cantidad de datos para los parametros, genera una tupla
    for nombre in nombres:                     # Recorremos los nombres como una tupla.
        print(nombre)                           

listar_nombres('Juan','Karen', 'Maria', 'Hernan') #Primer agregado
listar_nombres('Alberto', 'Giraldine')            #Segundo Agregado