### Imports
 
from Computadora import Computadoras
from Monitor import Monitor
from Mouse import Mouse
from Teclado import Teclado

#####

from Orden import Orden

m1 = Monitor('HDMI', 'LG', 25.3)
mo1 = Mouse('USB', 'Red Dragon')
t1 = Teclado('USB', 'Xtrike')

computadora1 = Computadoras(m1, mo1, t1, 'Gamer')
print(computadora1)

m2 = Monitor('VGA', 'Samsung', 23)
mo1 = Mouse('USB', 'Logitec')
t1 = Teclado('USB', 'Static')

computadora2 = Computadoras(m2, mo1, t1, 'Escritorio', )
print(computadora2)

ListaComputadoras = [computadora1, computadora2]

orden1 = Orden(ListaComputadoras)

print(ListaComputadoras)


