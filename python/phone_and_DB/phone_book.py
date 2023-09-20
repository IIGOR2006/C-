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
        name = input('Введите имя контакта = ')
        phone = input('Введите телефон = ')
        address = input('Введите адресс = ')
        mail = input('Введите почту = ')
        
        cursor.execute('SELECT *  FROM users')
        all_result = cursor.fetchall()
        
        for i in all_result:
            if i[1] == name:
                print('Данное имя уже существует. Рекомендуется задать другое имя, для лучшего ориентирования в списке контактов.')
            
        cursor.execute('INSERT INTO users (name, address, mail) VALUES (?, ?, ?)', [name, address, mail])
        conn.commit()
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        cursor.execute('INSERT INTO phones (id_user, phone_number) VALUES ( ?, ?)', [nu , phone])
        conn.commit()
      
    
    def all_data():
        cursor.execute('SELECT *  FROM users')
        all_result = cursor.fetchall()
        cursor.execute('SELECT *  FROM phones')
        all_result2 = cursor.fetchall()
        
        for i in all_result:
            print()
            buf = i[0]
            print(i[1], i[2],i[3])
            count = 0
            for j in all_result2:
                if buf == j[1]:
                    buf_num = j[2]
                    count +=1
                    print(f'телефон {count} = ',buf_num)
        
    def delete():
        name = input('Введите имя контакта для удаления')
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        cursor.execute('DELETE FROM phones WHERE id_user = ?', [nu])
        cursor.execute('DELETE FROM users WHERE id = ?', [nu])
        conn.commit()
        
    def search():
        name = input('Введите имя контакта для поиска')
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        id_buf = all_result[0]
        id_buf = id_buf[0]
        cursor.execute('SELECT * FROM phones WHERE id_user = ?', [id_buf])
        all_result2 = cursor.fetchall()
        for i in all_result:
            print()
            buf = i[0]
            print(i[1], i[2],i[3])
            count = 0
            for j in all_result2:
                if buf == j[1]:
                    buf_num = j[2]
                    count +=1
                    print(f'телефон {count} = ',buf_num)
        
    def update():
        
        name = input('Введите имя контакта для поиска')
        
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        id_buf = all_result[0]
        id_buf = id_buf[0]
        
        cursor.execute('SELECT * FROM phones WHERE id_user = ?', [id_buf])
        all_result2 = cursor.fetchall()
        
        for i in all_result:
            print()
            buf = i[0]
            print(i[1], i[2],i[3])
            count = 0
            
            for j in all_result2:
                if buf == j[1]:
                    buf_num = j[2]
                    count +=1
                    print(f'телефон {count} = ',buf_num)
                    
                    
        name_new = input('Введите имя контакта = ')
        phone_new = input('Введите телефон = ')
        address_new = input('Введите адресс = ')
        mail_new = input('Введите почту = ')
        
        
        if len(name_new) == 0:
            for i in all_result:
                name_new = i[1]
        if len(address_new) == 0:
            for i in all_result:
                address_new = i[2]
        if len(mail_new) == 0:
            for i in all_result:
                mail_new = i[3]
                
        cursor.execute('UPDATE users SET name = ?, address = ?, MAIL = ? WHERE id = ? ',[name_new, address_new, mail_new, id_buf])
        conn.commit()
        
    option = input("ddt = ")
    if option == '1':
        add_user()
    if option == '2':
        all_data()
    if option == '3':
        delete()
    if option == '4':
        search()
    if option == '5':
        update()
           
    conn.close()