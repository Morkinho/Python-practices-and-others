#funcion que se llama a si misma para completar una tarea

def factorial (numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial (numero - 1)

resultado = factorial (5)

print ('El valor de resultado es',  resultado)

