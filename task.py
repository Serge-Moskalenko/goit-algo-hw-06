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
    def __init__(self, value:str):         
            if value.isdigit() and len(value)==10:
                super().__init__(value)
            else:
                raise ValueError(f"Phone is too short:{value}.Please put in 10 number") 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self,phone):
            try:
                self.phones.append(Phone(phone))
            except ValueError as e:
                 print(e)

    def edit_phone(self, old_phone, new_phone):
        try:
            for phone in self.phones:
                if phone.value == old_phone:
                    phone.value = new_phone
                    break
                else:
                    raise ValueError("Phone is not find")
        except ValueError as e:
             print(e)
             
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            else:"phone isn't find"
    
    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

class AddressBook(UserDict):

    def __str__(self):
        return '\n'.join(str(contact) for contact in self.data.values())
    
    def add_record(self,contact):
           self.data[contact.name.value]=contact

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        self.data=[c for c in self.data if self.data[name] != name]
    
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("123567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("7890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")

