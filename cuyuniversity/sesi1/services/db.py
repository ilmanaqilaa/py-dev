import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_market'
)

# ? Untuk cek apakah sudah connect db atau belum
print(db.is_connected())