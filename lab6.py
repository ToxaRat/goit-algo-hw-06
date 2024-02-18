
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, name):
        pass

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    # додаемо тел
    def add_phone(self, tel: str): 
        self.phones.append(tel)
 
    def remove_phone(self):
        pass

    def edit_phone(self, oldtel: str, newtel: str):
        for i, v in enumerate(self.phones):
              if v == oldtel:
                self.phones[i] = newtel

    def find_phone(self, oldtel: str) -> str:
        for i, v in enumerate(self.phones):
              if v == oldtel:
                return oldtel
        return ""
   
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}"

class AddressBook(UserDict):
    def add_record(self, Rec: Record):
        self.data[Rec.name] = Rec

    def find(self, name: str):
        for n in self.data:
            if n.value == name:
                print('Find: Запис знайдено: ', name)
                found_status=True
                return self.data[n]
        print(f"Find: Запис на імʼя {name} не знайдено.")
        return Record('')
        
    def delete(self, name: str):
        for n in self.data:
            if n.value == name:
                print('Delete: Запис знайдено: ', name)
                del(self.data[n])
                return None
        print(f"Запис на імʼя {name} не знайдено.")
        return None

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
  
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
    
    # Видалення запису Jane
    book.delete("Jane") # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

if __name__ == "__main__":
    main()