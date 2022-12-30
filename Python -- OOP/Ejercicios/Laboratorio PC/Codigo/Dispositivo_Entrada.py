

###

class DispositivoEntrada:
    def __init__(self, tipoentrada, marca) -> None:
        self._tipoentrada = tipoentrada
        self._marca = marca

    def __str__(self) -> str:
        return f'Marca: [{self._marca}, Tipo de Entrada: {self._tipoentrada} ]'

