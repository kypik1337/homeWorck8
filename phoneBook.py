import view

phone_book = []


def getPhoneBook ():
    global phone_book
    return phone_book


def setPhoneBook (newPhoneBook):
    global phone_book
    phone_book = newPhoneBook

def addContact(contact: list):
    global phone_book
    phone_book.append(contact)

def removeContact(id):
    global phone_book
    name = phone_book[id -1] [0]
    confirm = input(f'Вы действительно хотите удалить контакт: {name}? y/n ')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def ZamenaContact(id):
    global phone_book
    name = phone_book[id -1] [0]
    confirm = input(f'Вы действительно хотите изменить контакт: {name}? y/n ')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def findContact():
    global phone_book
    find_string = view.inputFind()
    not_find = True
    for id, contact in enumerate(phone_book):
        for item in contact:
            if find_string in item.lower():
                not_find = False
                print((id + 1), *contact)
    if not_find:
        print('По данным которые вы мне показываете я ничего не нашел:)')