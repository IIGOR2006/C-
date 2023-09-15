import sqlite3
 
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# cursor.execute( 'CREATE TABLE users ( \
#     id INTEGER PRIMARY KEY, \
#     name TEXT, \
#     phone_number INTEGER, \
#     address TEXT, \
#     mail TEXT)')
        cursor.execute('INSERT INTO users (phone_number) VALUES (?)', (phone))
        conn.commit()
while True:
    
    conn = sqlite3.connect('book.db')
    cursor = conn.cursor()
    
    def add_user():
        name = input('Введите имя еонтакта = ')
        phone = input('Введите имя еонтакта = ')
        address = input('Введите имя еонтакта = ')
        mail = input('Введите имя еонтакта = ')
        cursor.execute('INSERT INTO users (name, phone_number, address, mail) VALUES (?, ?, ?, ?)', (name, phone, address, mail))
        conn.commit()
    
    def all_data():
        cursor.execute('SELECT * FROM users')
        all_result = cursor.fetchall()
        print(all_result)
        
    def delet():
        name = input('Введите имя контакта для удаления')
        cursor.execute('DELETE mail FROM users WHERE name = ?', [name])
        conn.commit()
    
        
    option = input("ddt = ")
    if option == '1':
        add_user()
    if option == '2':
        all_data()
    if option == '3':
        delet()
        
    conn.close()