import view
import phoneBook as pb 
import dataBase as db 

def main_nenu(choice: int):
    match choice:            # потипу ифа но только без перебора а присваиванием
        case 1 : 
            phoneBook = pb.getPhoneBook()
            view.printPhoneBook(phoneBook)   
        case 2 :
            db.loadDataBase()
            view.loadSuccess()
        case 3 :
            db.saveDataBase()
            view.saveSuccess()
        case 4 :
            contact = view.inputContact()
            pb.addContact(contact)
        case 5 :
            phoneBook = pb.getPhoneBook()
            view.printPhoneBook(phoneBook)
            print()
            id = view.inputRdactContact()
            contact = view.RedactContact()
            if pb.ZamenaContact(id):
                pb.addContact(contact)
                print()
                view.Izminemie()
        case 6 :
            phoneBook = pb.getPhoneBook()
            view.printPhoneBook(phoneBook)  
            id = view.inputRemoveContact()
            if pb.removeContact(id):
                view.removeSuccess() 
        case 7 :
            pb.findContact()
        case 0 :
            return True  # тут в единственном кейсе возвращает тру а в других пустату т.к выполняется комманда которая забита в кейсе приравниваются кейсы к фолс


def start():
    while True:
        choice = view.mainMenu()
        if main_nenu(choice):
            view.logOff()
            break
    
