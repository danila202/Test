import os

handbook_information = 'handbook_information.txt'


def create_entry():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    name_organization = input('Введите название организации: ')
    work_phone = input('Введите телефон рабочий: ')
    private_phone = input('Введите телефон личный: ')
    new_entry = f'{last_name} {first_name} {patronymic} {name_organization} {work_phone} {private_phone}'

    with open(handbook_information, "a") as file:
        file.writelines(new_entry + '\n')


def display_entries(entries:list):
    entry_on_page = 2
    for count in range(0, len(entries),entry_on_page):
        page = entries[count:count + entry_on_page]
        for entry in page:
            print(entry)
        if len(entries) > entry_on_page:
            print('________________________________________')


def edit_entry(line_in_handbook:int):
    try:
        edit_line = entries[line_in_handbook].split()
        edit_element = input('Выберите что бы Вы хотели изменить: ')
        new_element = input('ВВедите новую запись: ')
        index = edit_line.index(edit_element)
        edit_line[index] = new_element
        string = ' '.join(edit_line)
        entries[line_in_handbook] = string
        print(entries)
        with open(handbook_information,'w') as file:
            for entry in entries:
                file.write(entry + '\n')
    except IndexError:
        print('Такой записи не существует')


def search_entries():
    search_entry = input('Введите характеристики ,по которым Вы хотели найти записи: ').lower().split()
    result = []
    for entry in entries:
        for element in search_entry:
            if element in entry.lower():
                if entry not in result:
                    result.append(entry)

    display_entries(result) if result else print('Таких записей нет(((')


#Загрузка существующих записией из файла
if os.path.exists(handbook_information):
    with open(handbook_information, 'r') as file:
        entries = [line.strip() for line in file.readlines()]
else:
    entries = []


if __name__ == "__main__":
    print('1 - Добавить запись')
    print('2 - Редактировать запись')
    print('3 - Вывести записи постранично')
    print('4 - Поиск записей по параметрам')

    choice = int(input('Выберите действие: '))

    match choice:
        case 1:
            create_entry() # Функция на создание записи
        case 2:
            print('Количество записей',len(entries))
            index = int(input('Введите запись, которую хотите отредактировать: '))
            edit_entry(index) # Для редактирования записи нужно передать номер записи (Обратите внимание на количество записей)
        case 3:
            display_entries(entries)  # Функция на отображение постранично
        case 4:
            search_entries() # В функии на поиск записей нужно будет указать по каким характеристик\ам Вы собираетесь искать


