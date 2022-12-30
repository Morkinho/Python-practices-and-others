from Dispositivo_Entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    contador_mouse = 0

    def __init__(self, tipoentrada, marca) -> None:
        Mouse.__contador_mouse =+ 1
        IDMouse = Mouse.__contador_mouse
        super().__init__(tipoentrada, marca)


    def __str__(self) -> str:
        return f' ID Mouse: {self.__contador_mouse}, Marca {self._marca}, Tipo de Entrada: {self._tipoentrada}'
