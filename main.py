import sys

Contacts = {}


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
    if Contacts:
        for Name in Contacts:
            print(Contacts[Name])
    else:
        print('Contact list is empty\n')


def AddContact():
    sys.stdout.write('Name?\n')
    name_str = sys.stdin.readline().strip()

    sys.stdout.write('Phone?\n')
    phone_str = sys.stdin.readline().strip()
    try:
        int(phone_str)
    except ValueError:
        print('Invalid phone number\n')
        return

    sys.stdout.write('Email?\n')
    email_str = sys.stdin.readline().strip()

    sys.stdout.write('occupation?\n')
    occ_str = sys.stdin.readline().strip()

    Contacts[name_str] = Contact(name_str, int(phone_str), email_str, occ_str)


def FindContact():
    if Contacts:
        print('Name of contact to search?\n')
        input_str = sys.stdin.readline().strip().casefold()

        if input_str in Contacts:
            print(Contacts[input_str])
            return Contacts[input_str]
        else:
            print('Contact not found\n')

    else:
        print('Contact list is empty\n')

def SaveContacts():
    print('Name of new file?\n')
    filename = sys.stdin.readline().strip().casefold()
    try:
        with open(filename, 'w') as fp:
            for Name in Contacts:
                fp.write(Name + ',' + str(Contacts[Name].Phone) + ',' + Contacts[Name].Email + ',' + Contacts[Name].Occupation+'\n')

    except FileNotFoundError:
        print("Loading file failed\n")


def LoadContacts():
    print('Name of file to load?\n')
    filename = sys.stdin.readline().strip().casefold()
    load_count = 0
    try:
        global Contacts
        with open(filename) as fp:
            line = fp.readline()
            while line:
                line = line.split(',')
                Contacts[line[0]] = Contact(line[0], int(line[1]), line[2], line[3])
                line = fp.readline()
                load_count += 1
        print('Number of contacts loaded: {}\n'.format(load_count))

    except FileNotFoundError:
        print("File not found\n")


def DeleteContact():
    res = FindContact()

    if not res:
        return
    else:
        name = res.Name
        del Contacts[name]
        print(name + ' was deleted\n')


def DeleteAllContacts():
    Contacts.clear()
    print('All contacts deleted\n')


# Do not add () at the end of the function names!!!!
CommandList = {
    'print': PrintContacts,
    'add': AddContact,
    'find': FindContact,
    'save': SaveContacts,
    'load': LoadContacts,
    'delete': DeleteContact,
    'delete-all': DeleteAllContacts,
    'quit': quit
}


def UserInterface():
    global CommandList

    while True:
        print('Your options:')
        for cmd_name in CommandList:
            print(cmd_name)

        sys.stdout.write('\nCommand? ')
        command = sys.stdin.readline().strip().casefold()

        if command in CommandList:
            CommandList[command]()

        else:
            print('Invalid command\n')


UserInterface()
