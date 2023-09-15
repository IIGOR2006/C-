

sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'}, 'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}

while True:
    
    print('Что бы вывести список введите число 1')
    print('Что бы вывести список введите число 1')
    print('Что бы вывести список введите число 1')
    print('Что бы вывести список введите число 1')
    print('Что бы вывести список введите число 1')
    
    command = input('Введите номер команды = ')
    if command == '1':      # вывод всей книги
        print(sp)
        
    elif command == '2':        # создание контакта
        name = input('введите имя нового контакта')
        if name in sp:
            print('есть контакт с таким именем')
        else:
            coll = int(input('Сколько номеров вы хотите ввести: '))
            numbers = []
            for i in range(coll):
                number = input(f'Введите номер {i+1} : ')
                numbers.append(number)
            city = input('введите  город')
            status = input('введите статус')
        sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
        
    elif command == '3':        # добавление номера телефона в контакт
        name = input('введите имя контакта')
        if name not in sp:
            print('нет контакта')
        else:
            coll = int(input('Сколько номеров вы хотите добавить: '))
            for i in range(coll):
                number = input(f'Введите номер {i+1} : ')
                if number not in sp[name]['номер телефона']:
                    sp[name]['номер телефона'].append(number)
                else:
                    print('такой номер уже внесен')
    
    elif command == '4':    # вывод информации контакта
        name = input('введите имя контакта')
        if name not in sp:
            print('нет контакта')
        else:
            print(f'данные контакта {name} =',sp[name])
    
    elif command == '5': # редактирование внутренних данных
        name = input('введите имя контакта')
        if name not in sp:
            print('нет контакта')
        else:
            option = input('выберете пункт для замены старых данных на новые = ')
            if option == '1': # замена номера
                buf = input('введите название нового номера')
                sp[name]['номер телефона'] = buf
            if option == '2': # замена города
                buf = input('введите название нового города')
                sp[name]['город'] = buf
            if option == '3': # замена статуса
                buf = input('введите название нового статуса')
                sp[name]['Статус'] = buf
    
    elif command == '6': # удаление контакта
        name = input('введите имя контакта')
        if name not in sp:
            print('нет контакта')
        else:
            del sp[name]

    elif command == '7': # сохранение изменений
        