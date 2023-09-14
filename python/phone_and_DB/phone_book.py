import sqlite3
 
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

cursor.execute( 'CREATE TABLE users ( \
    id INTEGER PRIMARY KEY, \
    name TEXT, \
    phone_number INTEGER, \
    address TEXT, \
    mail TEXT)')


conn.close()

while True:
    
    def add_user():
        name = input('Введите имя еонтакта = ')
