import phoneBook as pb
path = 'phoneBook.txt'

def loadDataBase():
    with open (path, 'r', encoding='UTF-8') as file :
        phoneBook = file.readlines()
    pb.setPhoneBook(strToList(phoneBook))

def strToList(phoneBook: list):
    newPhoneBook = []
    for contact in phoneBook:
        newPhoneBook.append(contact.strip().split(';')) # стрип обрезает с начала и с конца лишние файлы
    return newPhoneBook
    
def saveDataBase():

    with open(path, 'w', encoding='UTF-8' ) as file:
        file.write(listToStr())



def listToStr():
    phoneBook = pb.getPhoneBook()
    newPhoneBook = []
    for contact in phoneBook:
        newPhoneBook.append(';'.join(contact) + '\n')
    newPhoneBook[-1] = newPhoneBook[-1][:-1]
    return ''.join(newPhoneBook)
