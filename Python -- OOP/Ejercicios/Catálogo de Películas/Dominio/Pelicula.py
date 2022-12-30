class Peliculas:
    pelicula = open('Catalogo.txt', 'w', encoding='utf8')
    
    def __init__(self, nombre) -> None:
        self.nombrepelicula = nombre

    def __str__(self) -> str:
        Peliculas.pelicula 

