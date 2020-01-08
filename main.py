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
    for Name in Contacts:
        print(Contacts[Name])


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
    input_str = sys.stdin.readline().strip().casefold()

    global Contacts
    if input_str in Contacts:
        print(Contacts[input_str])
    else:
        print('Contact not found')


def SaveContacts():
    print('Name of new file? ')
    filename = sys.stdin.readline().strip().casefold()
    try:
        global Contacts
        with open(filename, 'w') as fp:
            for Name in Contacts:
                fp.write(Name + ',' + str(Contacts[Name].Phone) + ',' + Contacts[Name].Email + ',' + Contacts[Name].Occupation)

    except FileNotFoundError:
        print("Loading file failed")


def LoadContacts():
    print('Name of file to load? ')
    filename = sys.stdin.readline().strip().casefold()
    load_count = 0
    try:
        with open(filename) as fp:
            line = fp.readline()
            while line:
                line = line.split(',')
                Contacts[line[0]] = Contact(line[0], int(line[1]), line[2], line[3])
                line = fp.readline()
                load_count += 1
        print('Number of contacts loaded: {}'.format(load_count))

    except FileNotFoundError:
        print("File not found")


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
