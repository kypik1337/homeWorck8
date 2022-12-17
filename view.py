


def mainMenu ():
    print('\nВыберите пункт menu:')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choiceMainMenu()       # сюда приходит число из проверки выбранного в мэин меню и возвращается в мэин меню. Т.е на данном этапе мэинМеню имеет какоето значение



def choiceMainMenu ():
    while True:
        try:
            choice = int(input('Выберите команду из меню от (0-7):= ')) # c 20- 24 программа ждет ввода цифры диапазано от 0-7 если вводится буква переход на 25 строку
            if choice in range (0, 8):
                print()
                return choice
            else:
                print('Такого пункта нету(')
        except:
            print(' Некоректно введены данные!)')     # если введена буква то цикл ваил перебрасывает в начало с выводом на экран некоректных данных и повторяется бесконечно 


def printPhoneBook (phoneBook: list):
    if len(phoneBook) > 0:
        for id, contact in enumerate (phoneBook, 1): # тоесть тут мы проходимся по списку в списке и получаем на выходе список из двух списков
            print(id, *contact)  # знаком умножить убираем скобки ковычки и делаем красивый вывод списка
    else:
        print('Телефонная книга пуста или не загружена((')


def logOff ():
    print('Пока друг дорогой!')

def Izminemie():
    print('Данные изменены и внесены в базу сяп за работу BRO)')

def loadSuccess():
    print ('Телефонная книга загружена)')

def saveSuccess():
    print('Телефонная книга сохранена!')


def RedactContact():
    name = input('Введите измененное имя контакта: ')
    phone = input('Введите измененный телефон контакта: ')
    comment = input('Введите измененный комментарий к контакту: ')
    return [name, phone, comment]



def inputContact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]

def inputRdactContact():
    id = int(input('Введите id контакта который желаете изменить: '))
    return id

def inputRemoveContact():
    id = int(input('Введите id контакта который желаете удалить: '))
    return id

def removeSuccess():
    print('Контакт успешно удален)')

def inputFind():
    find = input('Введите номер или несколько цифр номера телефона для поиска данных о контакте:) ').lower()
    return find
