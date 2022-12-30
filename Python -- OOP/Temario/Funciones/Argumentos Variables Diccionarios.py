def listar_terminos(**kwargs):
    for llave, valor in kwargs.items():
        print (llave, valor)

listar_terminos(IDE = 'Integrated Developement Enviroment', PK = 'PrimaryKeys')
listar_terminos(DBMS = 'Database Management System')