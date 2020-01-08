import sys

Contacts = {}
ContactNum = 0


class Contact:
    def __init__(self, Name, Phone, Email, Occupation):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
        self.Occupation = Occupation

    def __str__(self):
        return 'Name: ' + self.Name + '\n' + 'Phone: ' + str(
            self.Phone) + '\n' + 'Email: ' + self.Email + '\n' + 'Occupation: ' + self.Occupation


def PrintContacts():
    global Contacts
    for Con in Contacts:
        print(Contacts[Con])


def AddContact():
    sys.stdout.write('Name? ')
    name_str = sys.stdin.readline().strip()

    sys.stdout.write('Phone? ')
    phone_str = sys.stdin.readline().strip()
    try:
        int(phone_str)
    except ValueError:
        print('Invalid phone number')
        return

    sys.stdout.write('Email? ')
    email_str = sys.stdin.readline().strip()

    sys.stdout.write('occupation? ')
    occ_str = sys.stdin.readline().strip()

    Con = Contact(name_str, int(phone_str), email_str, occ_str)

    global Contacts
    Contacts[name_str] = Con

    global ContactNum
    ContactNum += 1


def FindContact():
    print('Name of contact to search? ')
    input_str = sys.stdin.readline().strip()

    global Contacts
    if Contacts.__contains__(input_str):
        print(Contacts[input_str])
    else:
        print('Contact not found')


def SaveContacts():
    try:
        with open('todo.txt', 'w') as fp:
            for Con in Contacts:
                print('SaveContacts')

    except FileNotFoundError:
        print("Loading file failed")


def LoadContacts():
    try:
        with open('contacts.txt') as fp:
            line = fp.readline()
            while line:
                line = line.split(',')
                name_str = line[0]
                phone_str = line[1]
                email_str = line[2]
                occ_str = line[3]
                Contacts[name_str] = Contact(name_str, int(phone_str), email_str, occ_str)
                line = fp.readline()

    except FileNotFoundError:
        print("loading file failed")


# Do not add () at the end of the function names!!!!
CommandList = {
    'print': PrintContacts,
    'add': AddContact,
    'find': FindContact,
    'save': SaveContacts,
    'load': LoadContacts,
    'quit': quit
}


def UserInterface():
    while True:
        sys.stdout.write('Command? ')
        command = sys.stdin.readline().strip().casefold()

        if CommandList.__contains__(command):
            CommandList[command]()

        else:
            print('Invalid command')


UserInterface()
