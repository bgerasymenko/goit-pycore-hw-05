# Декоратор для обробки помилок

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command"
    return inner

# Функція для розбору команди користувача
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Команду приводимо до нижнього регістру
    return cmd, *args

# Додаємо новий контакт до словника
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Змінюємо номер телефону для існуючого контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

# Показуємо номер телефону за іменем
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

# Виводимо всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

# Тестові команди замість input()
def main():
    contacts = {}  # Порожній словник контактів
    print("Welcome to the assistant bot!")

    # Імітація введення команд для тестування
    test_commands = [
        "add",
        "add Bob",
        "add Bob 123456",
        "phone",
        "phone Bob",
        "change Bob 654321",
        "phone Bob",
        "all",
        "exit"
    ]

    for user_input in test_commands:
        print(f"Input: {user_input}")
        if not user_input:
            print("Enter the argument for the command")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

# Запускаємо бот
if __name__ == "__main__":
    main()
