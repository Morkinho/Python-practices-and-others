from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
#    print(object)
    print (type(objeto))
    print(objeto.mostar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
print(empleado.mostrar_detalles())

gerente = Gerente('Carlos', 6000, 'RRHH')
print(gerente.mostrar_detalles())