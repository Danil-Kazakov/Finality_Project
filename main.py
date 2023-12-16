from collections import UserDict


# Клас Field - загальний клас для поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас Name успадковує клас Field і представляє поле з іменем
class Name(Field):
    pass


# Клас Address успадковує клас Field і представляє поле з адресою
class Address(Field):
    def __init__(self, value=''):
        super().__init__(value)

    def __str__(self):
        return f"Address: {self.value}"


# Клас Email успадковує клас Field і представляє поле з електронною поштою
class Email(Field):
    def __init__(self, value=''):
        super().__init__(value)

    def __str__(self):
        return f"Email: {self.value}"


# Клас Phone успадковує клас Field і представляє поле з номером телефону
class Phone(Field):
    def __init__(self, value=''):
        super().__init__(value)

    def __str__(self):
        return f"Phone number: {self.value}"

    def __getitem__(self):
        return self.value

    # ВАЛІДАЦІЯ НОМЕРА ТЕЛЕФОНА


# Клас Birthday успадковує клас Field і представляє поле з датою народження
class Birthday(Field):
    def __init__(self, value=''):
        super().__init__(value)

    def __str__(self):
        return f"Birthday: {self.value}"

    # ВАЛІДАЦІЯ ПОШТИ

class Note(Field):
    def __init__(self, value=''):
        super().__init__(value)

    def __str__(self):
        return self.value


# Клас Record представляє контакт, що містить ім'я, телефони, адресу, пошту та дату народження
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []  # Список телефонів для контакту
        self.address = None  # Адреса для контакту
        self.email = None  # Електронна пошта для контакту
        self.birthday = None  # Дата народження для контакту
        self.notes = []

    def __str__(self):
        # Повертає інформацію про контакт у вигляді рядка
        return f"Contact name: {self.name.value}\n{', '.join(str(p) for p in self.phones)}\n{self.email}\n{self.address}\n{self.birthday}\nNotes: {', '.join(str(note) for note in self.notes)}"



# Клас AddressBook успадковує UserDict і представляє адресну книгу
class AddressBook(UserDict):
    def add_record(self, record: Record):
        # Додає новий запис до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Повертає запис за іменем у випадку, якщо такий запис існує
        return self.data.get(name)

    # ДЕНЬ НАРОДЖЕННЯ КОНТАКТІВ ЧЕРЕЗ ЗАДАНУ КІЛЬКІСТЬ ДНІВ ВІД ПОТОЧНОЇ ДАТИ
    # ПОЩУК КОНТАКТІВ СЕРЕД КОНТАКТІВ КНИГИ
    # РЕДАГУВАТИ ТА ВИАЛЯТИ ЗАПИСИ З КНИГІ КОНТАКТІВ


# Основний код програми
if __name__ == "__main__":
    book = AddressBook()    # Створення адресної книги

    while True:

        command = input("Enter a command (add-name, add-phone, add-address, add-email, add-birthday, 'exit' for exit): ")
        parts = command.split()

        if len(parts) >= 2 and parts[0] == "add-name":
            # Команда для додавання імені до запису
            name = parts[1]
            record = book.find(name)
            if not record:
                new_record = Record(name)
                book.add_record(new_record)

        elif len(parts) >= 3 and parts[0] == "add-phone":
            # Команда для додавання номеру телефону до запису
            name = parts[1]
            phone = parts[2]
            record = book.find(name)
            if record:
                record.phones.append(Phone(phone))
            else:
                print("No such name found in the address book. Please add the name first.")

        elif len(parts) >= 2 and parts[0] == "add-address":
            # Команда для додавання адреси до запису
            name = parts[1]
            address = parts[2]
            record = book.find(name)
            if record:
                record.address = Address(address)
            else:
                print("No such name found in the address book. Please add the name first.")

        elif len(parts) >= 2 and parts[0] == "add-email":
            # Команда для додавання пошти до запису
            name = parts[1]
            email = parts[2]
            record = book.find(name)
            if record:
                record.email = Email(email)
            else:
                print("No such name found in the address book. Please add the name first.")

        elif len(parts) >= 2 and parts[0] == "add-birthday":
            # Команда для додавання дня народження до запису
            name = parts[1]
            birthday = parts[2]
            record = book.find(name)
            if record:
                record.birthday = Birthday(birthday)
            else:
                print("No such name found in the address book. Please add the name first.")

        elif len(parts) >= 2 and parts[0] == "add-note":
            # Команда для додавання нотатки до запису
            name = parts[1]
            note = " ".join(parts[2:])
            record = book.find(name)
            if record:
                record.notes.append(Note(note))
            else:
                print("No such name found in the address book. Please add the name first.")

        # КОМАНДА ДЛЯ ПОШУКУ, РЕДАГУВАННЯ, ВИДДАЛЕННЯ НОТАТОК

        # КОМАНА ДЛЯ ВИВЕДЕННЯ ДНЯ НАРОЖЕННЯ ЧЕРЕЗ N ДНІВ
        
        elif command.lower() == "show-all":
            # Виведення усіх записів в адресній книзі
            for name, record in book.data.items():
                print(record)

        elif command.lower() == "exit":
            # Вихід з програми
            break
        else:
            # Виведення повідомлення про невідому команду
            print("Invalid command")