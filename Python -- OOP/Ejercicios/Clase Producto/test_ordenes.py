from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Short', 254.00)
producto3 = Producto('Media', 50.00)
producto4 = Producto('Zapatos', 520.00)


productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
print(f'Total de Orden 1: ', orden1.calcular_total())

orden2 = Orden(productos2)
print(orden2)
print(f'Total de Orden 2: ', orden2.calcular_total())