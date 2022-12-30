class Catalogo:
    espaciopelicula = 0

    def __init__(self, nombre_película) -> None:
        self.nombre_pelicula = nombre_película
        self._numero_pelicula = Catalogo.espaciopelicula
    
    def agregar_peliculas (self, PeliculaN=None):
        self.nombre_pelicula.append(self.PeliculaN)

    def __str__(self) -> str:
        with open ('Catalogo.txt', 'a', encoding='utf8') as pelicula:
            pelicula_valor = self.nombre_pelicula 
            pelicula.write(pelicula_valor + '\n')
        return self.nombre_pelicula
        



