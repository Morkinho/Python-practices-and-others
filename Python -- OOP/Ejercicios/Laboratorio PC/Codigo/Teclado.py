from Dispositivo_Entrada import DispositivoEntrada

###


class Teclado(DispositivoEntrada):
    contador_teclado = 0 
    def __init__(self, tipoentrada, marca) -> None:
        super().__init__(tipoentrada, marca)
        Teclado.contador_teclado =+ 1
        self.IDTeclado = Teclado.contador_teclado
    
    def __str__(self) -> str:
        return f' ID Teclado: {self.IDTeclado}, Marca: {self._marca}, Tipo de Entrada: {self._tipoentrada}'
