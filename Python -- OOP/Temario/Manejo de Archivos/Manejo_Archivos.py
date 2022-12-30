try:
     archivo = open('prueba.txt', 'w', encoding='utf8') # Abre el archivo o lo crea
     archivo.write('Agregamos información al archivo\n')
     archivo.write('Adiós!\n')

except Exception as e:
    print(e)
finally:
    archivo.close #Luego del Close no se puede trabajar con el archivo.
    print('Cierre del archivo')

