### Imports 

from Monitor import *
from Mouse import *
from Teclado import *
from Dispositivo_Entrada import *

### 

class Computadoras:
    contador_computadoras = 0
 
    def __init__(self, Monitor, Mouse, Teclado, Nombre) -> None:
        Computadoras.contador_computadoras += 1 
        self.IDComputadoras = Computadoras.contador_computadoras
        self.Nombre = Nombre
        self.Monitor = Monitor
        self.Mouse = Mouse
        self.Teclado = Teclado

    
    def __str__(self) -> str:
        return f'''
        {self.Nombre}: {self.contador_computadoras} \n
        Detalles del Monitor: {self.Monitor} \n
        Detalles del Mouse: {self.Mouse} \n
        Detalles del Teclado: {self.Teclado} \n
        
        '''


