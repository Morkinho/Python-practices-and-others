class rectangulo:
    def __init__(self, altura, anchura) -> None:       
        self.altura = altura
        self.anchura = anchura

    def area (self):                         #Generamos la funcion con los parametros y acciones a realizar
        return self.anchura * self.anchura   #Generamos una accion y comportamientos.

PrimerValor = int(input('Coloque la altura del rectangulo: '))        #Generamos dinamismo
SegundoValor = int(input('Coloque la anchura del rectangulo: '))      

calculo = rectangulo (PrimerValor, SegundoValor)                      #Generamos una variable que utilice los valores dinamicos dentro de la clase

print(f'El valor del area es {calculo.area()}')                       #Esa variable le debe de pegar a los parametros deseados de la clase.

