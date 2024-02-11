def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and number please"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Enter the argument for the command"
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = int(phone)
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = int(phone)
    return "Contact changed"


@input_error
def show_contact(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def all_contacts(contacts):
    contact_strings = []
    if contacts:
        for name, phone in contacts.items():
            contact_strings.append(f"{name}: {phone}")
    else:
        contact_strings.append("No contacts available")
    return contact_strings


def main():

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print("Good bye!")
            break

        elif command == 'hello':
            print("How can I help you?")

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_contact(args, contacts))

        elif command == 'all':
            contacts_strings = all_contacts(contacts)
            for contact_string in contacts_strings:
                print(contact_string)

        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
