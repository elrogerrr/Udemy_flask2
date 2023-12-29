import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'elrogerrr',
    password = 'zapatanomurio666',
    database = 'rogerdb'
)

cursor = midb.cursor()

# cursor.execute('SELECT * FROM Usuario')
# resultado = cursor.fetchall()
# print(resultado)

sql = ' INSERT INTO Usuario (nombre,apellido,email) values (%s,%s,%s) '
values = ('pitufo','papa','papapit@aldeadehongos.com.mx')

cursor.execute(sql,values)
midb.commit()
print (cursor.rowcount)

