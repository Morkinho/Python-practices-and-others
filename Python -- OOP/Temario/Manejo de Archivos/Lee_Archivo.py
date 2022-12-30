archivo = open('prueba.txt', 'r', encoding='utf8')

#Leer el archivo
#print(archivo.read())

#Leer líneas completas
#print(archivo.readline())
#print(archivo.readline())

#Iterar el archivo.
#for linea in archivo:
#    print(linea)

#leer lineas
#print(archivo.readlines())

#Acceder a una linea de la lista
#print(archivo.readlines()[1])

#Abrimos un nuevo archivo
# a - anexar información.
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close
archivo2.close

print('Se ha terminado el proceso de copia de archivo')