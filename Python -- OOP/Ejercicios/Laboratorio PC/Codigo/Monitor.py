from Dispositivo_Entrada import DispositivoEntrada

class Monitor(DispositivoEntrada):
    contador_monitores = 0

    def __init__(self, tipoentrada, marca, tamaño) -> None:
        super().__init__(tipoentrada, marca)
        Monitor.__contador_monitores =+ 1
        IDMonitor = Monitor.__contador_monitores
        self.tamaño = float(tamaño)

    def __str__(self) -> str:
        return f' IDMonitor: {self.__contador_monitores}, Marca: {self._marca}, Tipo de Entrada: {self._tipoentrada}'
