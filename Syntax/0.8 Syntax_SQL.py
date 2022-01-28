import mysql.connector as mysql

config = {
'user': 'py_kris',
'password': 'ZVADygZNt5g1',
'host': '185.115.218.166',
'database': 'py_kris',
'raise_on_warnings': True
}   # dit is server

config2 = {
'user': 'root',
'password': 'Gloeilamp+123',
'host': '127.0.0.1',
'database': 'sakila',
'raise_on_warnings': True
}   # dit is local host


cnx = mysql.connect(**config)
cursor = cnx.cursor()

query = 'SELECT gr_id, naam FROM groente order by gr_id'
cursor.execute(query)

for (row) in cursor:
    print(row[0], row[1])   # row is een tuple


query = "INSERT INTO groente SET naam='aubergine'"
cursor.execute(query)
cnx.commit()

query = "UPDATE groente SET naam='bloemkool' WHERE naam='wortel'"
cursor.execute(query)
cnx.commit()

query = "DELETE FROM groente WHERE naam='komkommer'"
cursor.execute(query)
cnx.commit()


cursor.close()
cnx.close()