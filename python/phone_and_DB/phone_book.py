import sqlite3
 
try:
    connection = sqlite3.connect('book.db')
    cursor = connection.cursor()
    print("База данных телефонного справочника успешно подключена к SQLite")
except:
    pass
try:
    cursor.execute( 'CREATE TABLE users ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name TEXT, \
        address TEXT, \
        mail TEXT)')
except:
    pass

try:
    cursor.execute( 'CREATE TABLE phones ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        id_user INTEGER, \
        phone_number TEXT, \
        FOREIGN KEY (id_user) REFERENCES users (id) )')
except:
    pass

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
        name = input('Введите имя контакта для удаления = ')
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        cursor.execute('DELETE FROM phones WHERE id_user = ?', [nu])
        cursor.execute('DELETE FROM users WHERE id = ?', [nu])
        conn.commit()
        print('данные удалены')
    
    def delete_number():
        name = input('Введите имя контакта для поиска = ')
        
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        print('===', nu)
        if not nu:
            print('Данный контакт отсутствует')
        else:
            cursor.execute( 'SELECT * FROM phones WHERE  id_user= ?', [nu])
            all_result2 = cursor.fetchall()
            print('===', all_result2)
            count = 0
            for j in all_result2:
                            if nu == j[1]:
                                buf_num = j[2]
                                count +=1
                                print(f'телефон {count} = ',buf_num)
            num = int(input('Выберите телефон который хотите заменить = '))
            phone_number1 = num - 1
            id_num_buf = all_result2[phone_number1]
            id_num_buf = id_num_buf[0]
            cursor.execute('DELETE FROM phones WHERE id = ?', [id_num_buf])
            conn.commit()
            print('номер удален')
        
        
    def search():
        name = input('Введите имя контакта для поиска = ')
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        if not all_result:
            print('Данный контакт отсутствует')
        else:
            for i in all_result:
                if name == i[1]:
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
        
        name = input('Введите имя контакта для поиска = ')
        
        cursor.execute('SELECT * FROM users WHERE name = ?', [name])
        all_result = cursor.fetchall()
        if not all_result:
            print('Данный контакт отсутствует')
        else:
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
                        
            num = int(input('Выберите телефон который хотите заменить = '))         
            name_new = input('Введите новое имя контакта = ')
            phone_new = input('Введите новый телефон = ')
            address_new = input('Введите адресс = ')
            mail_new = input('Введите почту = ')
            
            phone_number1 = num - 1
            id_num_buf = all_result2[phone_number1]
            id_num_buf = id_num_buf[0]
            
            
            if len(name_new) == 0:
                for i in all_result:
                    name_new = i[1]
            if len(address_new) == 0:
                for i in all_result:
                    address_new = i[2]
            if len(mail_new) == 0:
                for i in all_result:
                    mail_new = i[3]
            if len(phone_new) > 0:
                cursor.execute('UPDATE phones SET phone_number = ? WHERE id = ? ',[phone_new, id_num_buf])
                    
            cursor.execute('UPDATE users SET name = ?, address = ?, MAIL = ? WHERE id = ? ',[name_new, address_new, mail_new, id_buf])
            
            conn.commit()
            print("")
            print('данные изменены')
            
    def add_number():
        name = input('Введите имя контакта для поиска = ')
        
        cursor.execute('SELECT id FROM users WHERE name = ?', [name])
        nu = cursor.execute( 'SELECT id FROM users WHERE  name= ?', [name]).fetchone()[0]
        if not nu:
            print('Данный контакт отсутствует')
        else:
            phone = input('Введите номер телефона = ')
            
            cursor.execute('INSERT INTO phones (id_user, phone_number) VALUES ( ?, ?)', [nu , phone])
            conn.commit()
            print('телефон добавлен')
    
    def close_phone_book():
        connection.commit()
        cursor.close()
        connection.close()
        print("Телефонный справочник сохранён и закрыт")
    
    print ('')
    print ('Меню')
    print ('1-добавление контакта')
    print ('2-вывести список')
    print ('3-удаление контакта')
    print ('4-поиск контакта')
    print ('5-изменение контакта')
    print ('6-добавление телефона в контакт')
    print ('7-удаление выбранного номера в контакте')
    print ('8-сохранение')
    print ('')
    option = input("выбирете опцию = ")
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
    if option == '6':
        add_number()
    if option == '7':
        delete_number()
    if option == '8':
        close_phone_book()