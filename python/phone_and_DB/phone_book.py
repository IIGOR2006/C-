import sqlite3
 
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# cursor.execute( 'CREATE TABLE users ( \
#     id INTEGER PRIMARY KEY AUTOINCREMENT, \
#     name TEXT, \
#     address TEXT, \
#     mail TEXT)')

# cursor.execute( 'CREATE TABLE phones ( \
#     id INTEGER PRIMARY KEY AUTOINCREMENT, \
#     id_user INTEGER, \
#     phone_number TEXT, \
#     FOREIGN KEY (id_user) REFERENCES users (id) )')

while True:
    
    conn = sqlite3.connect('book.db')
    cursor = conn.cursor()
    
    def add_user():
        name = input('Введите имя еонтакта = ')
        phone = input('Введите имя еонтакта = ')
        address = input('Введите имя еонтакта = ')
        mail = input('Введите имя еонтакта = ')
        cursor.execute('INSERT INTO users (name, address, mail) VALUES (?, ?, ?)', [name, address, mail])
        conn.commit()
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        cursor.execute('INSERT INTO phones (id_user, phone_number) VALUES ( ?, ?)', [nu , phone])
        conn.commit()
    
    def all_data():
        cursor.execute('SELECT name, address, mail,phone_number  FROM users,phones')
        all_result = cursor.fetchall()
        print(all_result)
        
    def delet():
        name = input('Введите имя контакта для удаления')
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        cursor.execute('DELETE FROM phones WHERE id_user = ?', [nu])
        cursor.execute('DELETE FROM users WHERE name = ?', [name])
        conn.commit()
        
    def search():
        name = input('Введите имя контакта для поиска')
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        print(all_result)
        
    def update():
        name = input('Введите имя контакта для поиска')
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        print(all_result)
        nu = input('Введите номер контакта для редактирования')
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        
    option = input("ddt = ")
    if option == '1':
        add_user()
    if option == '2':
        all_data()
    if option == '3':
        delet()
    if option == '4':
        search()
        
    conn.close()